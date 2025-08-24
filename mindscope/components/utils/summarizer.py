import logging
from datetime import datetime, timedelta

import polars as pl

logger = logging.getLogger(__name__)


def try_generic_string_parse(column_data: pl.Series):
    return {
        "column": column_data.name,
        "type": "string",
        "dtype": str(column_data.dtype),
        "null_count": column_data.null_count(),
        "not_null_count": column_data.count(),
        "n_unique": column_data.n_unique(),
    }


def try_categorical_parse(column_data: pl.Series):
    return {
        "column": column_data.name,
        "type": "categorical string",
        "dtype": str(column_data.dtype),
        "categories": column_data.unique().sort().to_list(),
        "n_categories": column_data.n_unique(),
        "null_count": column_data.null_count(),
        "not_null_count": column_data.count() - column_data.null_count(),
    }


def _parse_dates(data: pl.Series):
    common_formats = ["%Y-%m-%d", "%d-%m-%Y", "%Y/%m/%d", "%d/%m/%Y"]
    for fmt in common_formats:
        try:
            parsed_dates = data.str.to_datetime(fmt, strict=False).drop_nulls()
            if parsed_dates.len() > 0:
                return parsed_dates
        except Exception:
            continue
    return data.str.to_datetime(
        format=None, strict=False, ambiguous="earliest", cache=False
    ).drop_nulls()


def try_parse_dates(column_data: pl.Series, date_like_threshold: float):
    not_null_count = column_data.count()
    try:
        if not_null_count > 0:
            logger.debug(f"Trying to parse date column : {column_data.name}")
            not_null_data = column_data.drop_nulls()
            parsed_dates: pl.Series = _parse_dates(not_null_data)

            # Check if it majority elements are date or not
            is_majority = (
                parsed_dates.len() > 0
                and parsed_dates.len() / not_null_data.len() >= date_like_threshold
            )
            if is_majority:
                return {
                    "column": column_data.name,
                    "dtype": str(column_data.dtype),
                    "type": "date-like string",
                    "min_date": parsed_dates.min(),
                    "max_date": parsed_dates.max(),
                    "null_count": column_data.null_count(),
                    "not_null_count": column_data.count(),
                    "min_max_diff": parsed_dates.max() - parsed_dates.min(),
                    "parsed_success_rate": parsed_dates.len() / not_null_count,
                }
    except Exception as e:
        logger.debug(
            f"Failed to parse date column : {column_data.name} for reason : {e.__class__} : {e}"
        )
    return None


def datetime_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, timedelta):
        return str(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
