"""
Todo:
    - Update file structure
    - move non class functions to their correct position
"""

import os
from typing import Callable, Dict, Hashable

import polars as pl

# from llmx import TextGenerator, llm

# types
LoaderDict = Dict[Hashable, Callable[[], pl.DataFrame]]
EMPTY_DF = pl.DataFrame()


# Errors
class FileReadError(BaseException):
    pass


def get_dataframe_from_filepath(filepath: str, encoding: str = "utf-8"):
    if not os.path.exists(filepath):
        raise FileNotFoundError("Given file not found..")

    extn = filepath.split(".")[-1]
    mapping: LoaderDict = {
        "csv": lambda: pl.read_csv(filepath, encoding=encoding),
        "xlsx": lambda: pl.read_excel(filepath, encoding=encoding),
        "xls": lambda: pl.read_excel(filepath, encoding=encoding),
        "parquet": lambda: pl.read_parquet(filepath),
        "json": lambda: pl.read_json(filepath, orient="records", encoding=encoding),
    }

    if extn not in mapping:
        raise KeyError(
            f"Given extension {extn} not in mapping \
            available extensions are : {list(mapping.keys())}"
        )

    try:
        df: pl.DataFrame = mapping[extn]()
    except Exception as e:
        message = f"Not able to read file : {e.__class__} : {e}"
        raise FileReadError(message)

    if df.empty:
        raise pl.errors.EmptyDataError("File loaded but no data found.")

    return df


class Manager:
    """
    Manager Responsible for execution of different components.
    Managers handles a single file at a time.
    Responsible for data loading and checking for empty dataframes.

    - Components:
        - Summarizer
    """

    def __init__(
        self,
        data: pl.DataFrame = EMPTY_DF,
        filepath: str = "",
        # text_generator: TextGenerator = None,
    ):
        """
        Takes dataframe or file_path as argument if both given then dataframe will be prioritized.

        Requires tabular format for now.
        """
        if isinstance(data, pl.DataFrame) and not data.empty:
            self.data = data
        elif filepath:
            self.data = get_dataframe_from_filepath(filepath)
            self.filepath = filepath
        else:
            raise ValueError("Either data or filepath must be provided.")
