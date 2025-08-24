import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from datetime import date
import pytest
import polars as pl
from mindscope.components import Summarizer
from dotenv import load_dotenv

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

logger.info(f"Loaded ENV File : {load_dotenv()}")


@pytest.fixture
def sample_df():
    # data = {
    #     "product_id": [101, 102, 103, 104],
    #     "price": [19.99, 25.50, 9.95, None],
    #     "category": ["A", "B", "A", "C"],
    #     "in_stock": [True, False, True, True],
    #     "launch_date": [date(2024, 1, 15), date(2023, 5, 20), None, date(2024, 1, 15)],
    #     "last_order": ["2025-08-10", "2025-07-22", "invalid-date", "2025-08-11"],
    #     "status": pl.Series(
    #         ["active", "inactive", "active", "discontinued"], dtype=pl.Categorical
    #     ),
    # }
    df = pl.read_csv("test\\1000_rows_dataset.csv")
    return df


def test_summarizer_initialization(sample_df):
    summarizer = Summarizer(data=sample_df, filename="1000_rows_dataset.csv")
    assert summarizer.N_ROWS == 1000
    assert summarizer.N_COLUMNS == 7
    assert summarizer.filename == "1000_rows_dataset.csv"


def test_numeric_column_properties(sample_df: pl.DataFrame):
    summarizer = Summarizer(data=sample_df)
    summary = summarizer.summarize()

    # Find price column properties
    price_props = next(col for col in summary["columns"] if col["column"] == "price")

    assert price_props["type"] == "numeric"
    assert price_props["dtype"] == sample_df["price"].dtype.__class__.__name__
    assert price_props["min"] == sample_df["price"].min()
    assert price_props["max"] == sample_df["price"].max()
    assert price_props["null_count"] == sample_df["price"].null_count()


def test_categorical_column_properties(sample_df: pl.DataFrame):
    summarizer = Summarizer(data=sample_df)
    summary = summarizer.summarize()

    # Find category column properties
    cat_props = next(col for col in summary["columns"] if col["column"] == "category")

    assert cat_props["type"] == "categorical string"
    assert cat_props["categories"] == sample_df["category"].unique().sort().to_list()
    assert cat_props["n_categories"] == sample_df["category"].n_unique()
    assert cat_props["null_count"] == sample_df["category"].null_count()


def test_boolean_column_properties(sample_df: pl.DataFrame):
    summarizer = Summarizer(data=sample_df)
    summary = summarizer.summarize()

    # Find in_stock column properties
    bool_props = next(col for col in summary["columns"] if col["column"] == "in_stock")

    assert bool_props["type"] == "boolean"
    assert bool_props["true_count"] == sample_df["in_stock"].sum()
    assert (
        bool_props["false_count"]
        == sample_df["in_stock"].count() - sample_df["in_stock"].sum()
    )
    assert bool_props["null_count"] == sample_df["in_stock"].null_count()


def test_temporal_column_properties(sample_df: pl.DataFrame):
    summarizer = Summarizer(data=sample_df)
    summary = summarizer.summarize()

    # Find launch_date column properties
    date_props = next(
        col for col in summary["columns"] if col["column"] == "launch_date"
    )

    assert date_props["type"] == "date-like string"
    assert date_props["min_date"].strftime("%Y-%m-%d") == sample_df["launch_date"].min()
    assert date_props["max_date"].strftime("%Y-%m-%d") == sample_df["launch_date"].max()
    assert date_props["null_count"] == sample_df["launch_date"].null_count()


def test_date_like_string_column_properties(sample_df):
    summarizer = Summarizer(data=sample_df)
    summary = summarizer.summarize()

    # Find last_order column properties
    date_str_props = next(
        col for col in summary["columns"] if col["column"] == "last_order"
    )

    assert date_str_props["type"] == "date-like string"
    assert "parsed_success_rate" in date_str_props
    assert date_str_props["null_count"] == 0


def test_empty_dataframe():
    empty_df = pl.DataFrame()
    summarizer = Summarizer(data=empty_df)
    summary = summarizer.summarize()

    assert summarizer.N_ROWS == 0
    assert summarizer.N_COLUMNS == 0
    assert len(summary["columns"]) == 0


def test_samples_in_summary(sample_df):
    summarizer = Summarizer(data=sample_df)
    summary = summarizer.summarize()

    for column_props in summary["columns"]:
        assert "samples" in column_props
        assert len(column_props["samples"]) <= 5  # Default sample size


def test_enrich_summary(sample_df):
    summarizer = Summarizer(data=sample_df)
    summary = summarizer.summarize(enrich=True)
    print(f"Summary {summary}")

    # Currently _enrich is a pass-through, so just verify it doesn't break
    assert summary is not None
    assert "columns" in summary
