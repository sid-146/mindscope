import copy
import json
import logging

import polars as pl

from mindscope.components.models import LLMResponse, GenerationConfig, Summary
from mindscope.components.llm import llm
from .utils.summarizer import (
    try_parse_dates,
    try_generic_string_parse,
    try_categorical_parse,
    datetime_serializer,
)
from .prompts.summarizer import SUMMARIZER_ENRICH_SYSTEM_PROMPT, SUMMARIZER_USER_PROMPT

logger = logging.getLogger(__name__)


class Summarizer:
    # Todo: Should be move the data into a new class named Dataset.
    def __init__(self, data: pl.DataFrame, filename: str = ""):
        """
        Initialize the summarizer with a polars dataframe.
        """
        self.summary: dict = {
            "filename": filename,
            "name": "",  # Dataset name should be given by LLM maximum 3 word if not given by user.
            "description": "",  # LLM should generate this if not given by user.
        }
        self.data = data
        self.N_ROWS: int = self.data.height
        self.N_COLUMNS: int = self.data.width
        self.filename = filename
        # Threshold for identifying categorical columns
        self.CATEGORICAL_THRESHOLD: float = 0.05
        # Threshold for identifying date-like columns
        self.DATE_LIKE_THRESHOLD: float = 0.9
        self.CATEGORICAL_UNIQUE_LIMIT: int = 50

    def _is_categorical(self, n_unique):
        check = (
            self.N_ROWS > 0
            and (n_unique / self.N_ROWS) < self.CATEGORICAL_THRESHOLD
            and (n_unique < self.CATEGORICAL_UNIQUE_LIMIT)
        )
        return check

    def _handle_numeric_column(self, column_data: pl.Series):
        logger.debug(f"_handle_numeric_column called for column : {column_data.name}")
        return {
            "column": column_data.name,
            "type": "numeric",
            "dtype": str(column_data.dtype),
            "min": column_data.min(),
            "max": column_data.max(),
            "mean": column_data.mean(),
            "median": column_data.median(),
            "std": column_data.std(),
            "null_count": column_data.null_count(),
            "not_null_count": column_data.count(),
        }

    def _handle_temporal_column(self, column_data: pl.Series):
        logger.debug(f"_handle_temporal_column called for column : {column_data.name}")
        return {
            "column": column_data.name,
            "type": "date",
            "dtype": str(column_data.dtype),
            "min_date": column_data.min(),
            "max_date": column_data.max(),
            "null_count": column_data.null_count(),
            "not_null_count": column_data.count(),
            "min_max_diff": column_data.max() - column_data.min(),
        }

    def _handle_boolean_column(self, column_data: pl.Series):
        logger.debug(f"_handle_boolean_column called for column : {column_data.name}")
        return {
            "column": column_data.name,
            "type": "boolean",
            "dtype": str(column_data.dtype),
            "true_count": column_data.sum(),
            "false_count": column_data.count() - column_data.sum(),
            "null_count": column_data.null_count(),
            "not_null_count": column_data.count(),
        }

    def _handle_categorical_column(self, column_data: pl.Series):
        logger.debug(
            f"_handle_categorical_column called for column : {column_data.name}"
        )
        return {
            "column": column_data.name,
            "dtype": str(column_data.dtype),
            "type": "categorical",
            "categories": column_data.unique().sort().to_list(),
            "n_categories": column_data.n_unique(),
            "null_count": column_data.null_count(),
            "not_null_count": column_data.count(),
        }

    def _handle_string_column(self, column_data: pl.Series):
        properties = try_parse_dates(column_data, self.DATE_LIKE_THRESHOLD)
        if properties is not None:
            return properties

        if self._is_categorical(column_data.n_unique()):
            properties = try_categorical_parse(column_data)

        if properties is not None:
            return properties

        properties = try_generic_string_parse(column_data)
        if properties is not None:
            return properties
        else:
            {
                "column": column_data.name,
                "type": "string",
                "dtype": str(column_data.dtype),
                "null_count": column_data.null_count(),
                "not_null_count": column_data.count(),
                "n_unique": column_data.n_unique(),
            }
        return

    def _handle_other_column(self, column_data: pl.Series):
        return {
            "column": column_data.name,
            "dtype": str(column_data.dtype),
            "type": "other",
            "null_count": column_data.null_count(),
            "not_null_count": column_data.count(),
        }

    # Check data type and call respective handle function.
    def _handle_column(self, dtype: pl.DataType, column_data: pl.Series):
        if dtype.is_numeric():
            properties = self._handle_numeric_column(column_data)
        elif dtype.is_temporal():
            properties = self._handle_temporal_column(column_data)
        elif isinstance(dtype, pl.Boolean):
            properties = self._handle_boolean_column(column_data)
        elif isinstance(dtype, pl.Categorical):
            properties = self._handle_categorical_column(column_data)
        elif isinstance(dtype, pl.Utf8):
            properties = self._handle_string_column(column_data)
        else:  # handle other
            properties = self._handle_other_column(column_data)

        return properties

    def _column_properties(self, n_samples):
        data = copy.deepcopy(self.data)
        property_list = []

        for column in data.columns:
            logger.debug(f"Running for : {column}")
            dtype = data[column].dtype
            column_data = data[column]

            properties = self._handle_column(dtype, column_data)
            samples: pl.Series = column_data.sample(
                n_samples, with_replacement=False, shuffle=True
            )
            properties["samples"] = samples.to_list()
            property_list.append(properties)

        return property_list

    def _enrich(self, summary: dict):
        """
        # Docstring will go here.

        Todo:
        - add feature to give custom input for enrich summary generator.
        - Add response format validator.
        - Add Generation Config handler.
        """
        llm_client = llm(provider="openai")
        prompt = SUMMARIZER_USER_PROMPT.format(
            json.dumps(summary, default=datetime_serializer)
        )
        messages = [
            {"role": "system", "content": SUMMARIZER_ENRICH_SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ]

        gen_config = GenerationConfig(max_tokens=4028, temperature=0.2)
        response: LLMResponse = llm_client.generate_text(
            messages,
            gen_config=gen_config,
            # response_format=Summary,
        )
        content = (response.text[0].content).strip()
        try:
            content = json.loads(content)
        except Exception as e:
            print(f"Failed to parse to json, returning string. : {e}")
        content = Summary(**content)
        return content

    def summarize(self, n_samples=3, enrich=False):
        summary = copy.deepcopy(self.summary)
        column_properties = self._column_properties(n_samples=n_samples)

        if "columns" not in summary:
            summary["columns"] = column_properties
        else:
            columns: list = summary["columns"]
            columns.extend(column_properties)
            summary["columns"] = columns
        if enrich:
            summary = self._enrich(summary)

        self.summary = summary
        return summary
