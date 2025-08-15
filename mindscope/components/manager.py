import os
from typing import Callable, Dict, Hashable

import pandas as pd
from llmx import TextGenerator, llm

# types
LoaderDict = Dict[Hashable, Callable[[], pd.DataFrame]]
EMPTY_DF = pd.DataFrame()


# Errors
class FileReadError(BaseException):
    pass


def get_dataframe_from_filepath(filepath: str, encoding: str = "utf-8"):
    if not os.path.exists(filepath):
        raise FileNotFoundError("Given file not found..")

    extn = filepath.split(".")[-1]
    mapping: LoaderDict = {
        "csv": lambda: pd.read_csv(filepath, encoding=encoding),
        "xlsx": lambda: pd.read_excel(filepath, encoding=encoding),
        "xls": lambda: pd.read_excel(filepath, encoding=encoding),
        "parquet": lambda: pd.read_parquet(filepath),
        "json": lambda: pd.read_json(filepath, orient="records", encoding=encoding),
    }

    if extn not in mapping:
        raise KeyError(
            f"Given extension {extn} not in mapping \
            available extensions are : {list(mapping.keys())}"
        )

    try:
        df: pd.DataFrame = mapping[extn]()
    except Exception as e:
        message = f"Not able to read file : {e.__class__} : {e}"
        raise FileReadError(message)

    if df.empty:
        raise pd.errors.EmptyDataError("File loaded but no data found.")

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
        data: pd.DataFrame = EMPTY_DF,
        filepath: str = "",
        text_generator: TextGenerator = None,
    ):
        """
        Takes dataframe or file_path as argument if both given then dataframe will be prioritized.

        Requires tabular format for now.
        """
        if isinstance(data, pd.DataFrame) and not data.empty:
            self.data = data
        elif filepath:
            self.data = get_dataframe_from_filepath(filepath)
            self.filepath = filepath
        else:
            raise ValueError("Either data or filepath must be provided.")
