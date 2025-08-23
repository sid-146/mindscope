from typing import List, Any

from pydantic import BaseModel


class GenerationConfig(BaseModel):
    temperature: float = 0.8
    model_name: str | None = None
    provider: str = "openai"
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
