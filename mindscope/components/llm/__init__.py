from .openai import OpenAIClient


def llm(provider: str):
    if provider.lower() == "openai":
        client = OpenAIClient()
        return client
    else:
        raise ValueError("Provider not supported.")


__all__ = ["llm"]
