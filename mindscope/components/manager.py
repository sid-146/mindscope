"""
Todo:
    - Update file structure
    - move non class functions to their correct position
"""

import polars as pl

from .core import EMPTY_DF
from .utils.manager import get_dataframe_from_filepath

# Errors


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
