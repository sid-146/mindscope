from pydantic import BaseModel, ConfigDict
from typing import Any, List


class Column(BaseModel):
    column: Any
    type: str = ""
    dtype: str = ""
    min: float | None = None
    max: float | None = None
    mean: float | None = None
    median: float | None = None
    std: float | None = None
    null_count: int
    not_null_count: int
    samples: List[Any] = []
    summary: str = ""

    model_config: ConfigDict = ConfigDict(extra="allow")


class Summary(BaseModel):
    filename: str = ""
    name: str = ""
    description: str = None
    columns: List[Column] = []

    model_config: ConfigDict = ConfigDict(extra="allow")
