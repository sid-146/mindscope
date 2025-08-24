from abc import ABC, abstractmethod


class BaseLLM(ABC):
    def __init__(self, provider: str = "openai", **kwargs):
        self.provider = provider
        self.model_name = kwargs.get("model_name", "gpt-3.5-turbo")

    @abstractmethod
    def chat():
        raise NotImplementedError("Base class should implement this method.")

    @abstractmethod
    def generate_text():
        raise NotImplementedError("Base class should implement this method.")

    # def embed():
    #     raise NotImplementedError("Base class should implement this method.")
