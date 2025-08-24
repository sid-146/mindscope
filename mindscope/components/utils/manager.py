import os

import polars as pl

from mindscope.components.core import LoaderDict, FileReadError


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

    if df.is_empty():
        raise pl.errors.EmptyDataError("File loaded but no data found.")

    return df
