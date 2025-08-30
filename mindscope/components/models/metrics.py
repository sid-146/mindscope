from typing import List

from pydantic import BaseModel


class MetricModel(BaseModel):
    name: str
    definition: str
    importance: str
    formula: str
    steps: str
    code_string: str | None = None


class Metrics(BaseModel):
    metrics: List[MetricModel]
