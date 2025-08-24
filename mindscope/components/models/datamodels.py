from typing import List, Any

from pydantic import BaseModel, ConfigDict


class GenerationConfig(BaseModel):
    temperature: float = 0.8
    model_name: str | None = None
    provider: str | None = None
    max_tokens: int | None = 250
    top_k: int = 25
    top_p: float = 1.0

    # add more as you understand more


class Message(BaseModel):
    role: str
    content: str


class LLMResponse(BaseModel):
    text: List[Message]
    config: Any
    logprobs: Any | None = None  # logprobs if available
    usage: Any | None = None  # usage statistics from the provider
    response: Any | None = None  # full response from the provider


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
