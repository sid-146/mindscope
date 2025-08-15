import copy
import logging
import random

import polars as pl

logger = logging.getLogger(__name__)


"""
Sample

```python

from datetime import date, datetime
import pprint

# Create a sample Polars DataFrame with diverse column types
data = {
    "product_id": [101, 102, 103, 104, 105, 106, 101],
    "price": [19.99, 25.50, 9.95, 19.99, 50.0, None, 19.99],
    "category": ["A", "B", "A", "C", "B", "A", "A"],
    "in_stock": [True, False, True, True, False, True, True],
    "launch_date": [date(2024, 1, 15), date(2023, 5, 20), date(2024, 1, 15), None, date(2022, 9, 1), date(2024, 2, 28), date(2024, 1, 15)],
    "last_order_str": ["2025-08-10", "2025-07-22", "2025-08-11", "invalid-date", "2025-06-15", "2025-08-10", "2025-08-10"],
    "region_code": ["US-W", "EU-C", "US-W", "AS-E", "EU-C", "US-W", "US-W"],
    "description": ["Product Alpha", "Product Beta", "Product Gamma", "Product Delta", "Product Epsilon", "Product Zeta", "Product Alpha"],
    "status": pl.Series(["active", "inactive", "active", "active", "discontinued", "active", "active"], dtype=pl.Categorical),
    "timestamp": [datetime(2025,8,15,10,0), datetime(2025,8,14,11,30), None, datetime(2025,8,15,12,0), datetime(2025,8,13,9,0), datetime(2025,8,15,14,45), datetime(2025,8,15,10,0)],
}

df = pl.DataFrame(data)

# Generate properties for the dataframe
column_analysis = get_column_properties(df)

# Pretty print the results for better readability
pprint.pprint(column_analysis)
```


"""


class Summarizer:
    """
    summarizer responsible for generating summaries of a given dataframe.

    `summarize` method to generate a summary of the dataframe.

    """

    def __init__(self, data: pl.DataFrame, filename: str = ""):
        """
        Initialize the summarizer with a polars dataframe.
        """
        self.summary: dict = {
            "filename": filename,
            "name": filename,
        }
        self.data = data
        self.N_ROWS: int = self.data.height
        self.N_COLUMNS: int = self.data.width
        self.filename = filename
        self.CATEGORICAL_THRESHOLD: float = (
            0.05  # Threshold for identifying categorical columns
        )
        self.CATEGORICAL_UNIQUE_LIMIT: int = 50
        self.DATE_LIKE_THRESHOLD: float = (
            0.9  # Threshold for identifying date-like columns
        )

    def _check_type(self, dtype: str, value):
        pass

    def _columns_properties(self, n_samples: int = 5):
        """
        Generate properties for each column in the dataframe.

        - Iterate over each column in the dataframe.
        - If number column, then calculate min, max, mean, median, std.
        - if string/object column, then check if it is a date column, if not then check if it is categorical. else it is string.
        - if boolean column.
        - if column any date type then column of type date.
        - if type is categorical then categorical.
        """

        # Initialize all variables to use
        data = copy.deepcopy(self.data)
        property_list = []

        for column in data.columns:
            dtype = data[column].dtype
            col = data[column]
            # Handling numeric columns
            properties = {}
            if dtype.is_numeric():
                properties = {
                    "column": column,
                    "type": "numeric",
                    "dtype": str(dtype),
                    "min": col.min(),
                    "max": col.max(),
                    "mean": col.mean(),
                    "median": col.median(),
                    "std": col.std(),
                    "null_count": col.null_count(),
                    "not_null_count": col.count() - col.null_count(),
                }

            # Handling date/time columns
            elif dtype.is_temporal():
                properties = {
                    "column": column,
                    "type": "date",
                    "dtype": str(dtype),
                    "min_date": col.min(),
                    "max_date": col.max(),
                    "null_count": col.null_count(),
                    "not_null_count": col.count() - col.null_count(),
                    "min_max_diff": col.max() - col.min(),
                }

            # Handling boolean columns
            elif isinstance(dtype, pl.Boolean):
                properties = {
                    "column": column,
                    "type": "boolean",
                    "dtype": str(dtype),
                    "true_count": col.sum(),
                    "false_count": col.count() - col.sum(),
                    "null_count": col.null_count(),
                    "not_null_count": col.count() - col.null_count(),
                }

            # Handling Categories
            elif isinstance(dtype, pl.Categorical):
                properties = {
                    "column": column,
                    "dtype": str(dtype),
                    "type": "categorical",
                    "categories": col.unique().sort().to_list(),
                    "n_categories": col.n_unique(),
                    "null_count": col.null_count(),
                    "not_null_count": col.count() - col.null_count(),
                }

            # Handling String columns
            elif isinstance(dtype, pl.Utf8):
                null_count = col.null_count()
                not_null = col.drop_nulls()
                n_unique = col.n_unique()

                # Check if the column is a date column
                if not_null.len() > 0:
                    # Try to parse to check date like values; Strict=True to return null on failure
                    parsed_dates = not_null.str.to_datetime(
                        format=None,
                        strict=False,
                    ).drop_nulls()

                    # Ratio is above then threshold then it can be said as date-like column
                    if parsed_dates.len() / not_null.len() >= self.DATE_LIKE_THRESHOLD:
                        properties = {
                            "type": "date-like string",
                            "min_date": parsed_dates.min(),
                            "max_date": parsed_dates.max(),
                            "null_count": null_count,
                            "not_null_count": col.count() - null_count,
                            "min_max_diff": parsed_dates.max() - parsed_dates.min(),
                            "parsed_success_rete": parsed_dates.len() / not_null.len(),
                        }

                    else:  # Not a date-like string
                        pass  # Check if it is categorical

                # Check if it is categorical
                # Todo: This logic can be improved
                if not properties:
                    is_categorical = (
                        self.N_ROWS > 0  # There should at least one row
                        and (n_unique / self.N_ROWS)
                        < self.CATEGORICAL_THRESHOLD  # if unique values are less than threshold then they are not considered as categorical
                    ) or (
                        n_unique < self.CATEGORICAL_UNIQUE_LIMIT
                    )  # Max unique values limit
                    if is_categorical:
                        properties = {
                            "type": "categorical string",
                            "dtype": str(dtype),
                            "categories": col.unique().sort().to_list(),
                            "n_categories": n_unique,
                            "null_count": null_count,
                            "not_null_count": col.count() - null_count,
                        }
                    else:
                        # String Column
                        properties = {
                            "type": "string",
                            "dtype": str(dtype),
                            "null_count": null_count,
                            "not_null_count": col.count() - null_count,
                            "n_unique": n_unique,
                        }

            # Handling other types
            else:
                properties = {"type": f"{dtype}"}
                properties.update(
                    {
                        "null_count": col.null_count(),
                        "not_null_count": col.count() - col.null_count(),
                    }
                )

            samples = random.sample(
                col.unique().to_list(), k=min(n_samples, len(col.unique()))
            )
            properties["samples"] = samples
            property_list.append(properties)

        return property_list

    def _enrich(self, summary: dict):
        """
        Enrich the summary with additional information by passing the locally generated summary to an llm.
        """
        pass

    def summarize(self, enrich: bool = False):
        """
        Generate a summary of the dataframe.
        Read docs/summarizer.md for more details on the summary format.
        """
        summary: dict = copy.deepcopy(self.summary)
        column_properties = self._columns_properties()

        if "columns" not in summary:
            summary["columns"] = column_properties
        else:
            columns: list = summary["columns"]
            columns.extend(column_properties)
            summary["columns"] = columns
        if enrich:
            summary = self._enrich(summary)

        # Update only after processing all columns
        self.summary = summary

        # return a copy to prevent external modifications
        return summary
