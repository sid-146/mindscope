from abc import ABC, abstractmethod


class BaseLLM(ABC):
    def __init__(self):
        return

    @abstractmethod
    def chat():
        raise NotImplementedError("Base class should implement this method.")

    @abstractmethod
    def embed():
        raise NotImplementedError("Base class should implement this method.")

    @abstractmethod
    def generate_text():
        raise NotImplementedError("Base class should implement this method.")
