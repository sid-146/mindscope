from .openai import OpenAIClient


def llm(provider: str, **kwargs):
    if provider.lower() == "openai":
        # fix this they all should either given generation config or kwargs
        client = OpenAIClient(provider=provider, **kwargs)
        return client
    else:
        raise ValueError("Provider not supported.")


__all__ = ["llm"]
