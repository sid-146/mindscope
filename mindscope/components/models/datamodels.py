from pydantic import BaseModel


class GenerationConfig(BaseModel):
    temperature: float = 0.8
    model: str = "gpt-4o-mini"
    provider: str = "openai"
    max_token: int | None = None
    top_k: int = 25
    top_p: float = 1.0

    # add more as you understand more


class Message(BaseModel):
    role: str
    content: str
