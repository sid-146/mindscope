from typing import Dict

from openai import OpenAI, AzureOpenAI

from .base import BaseLLM
from ..models import GenerationConfig


class OpenAIClient(BaseLLM):
    def __init__(
        self,
        provider: str,
        api_key: str,
        base_url: str = "",
        organization: str = "",
        model: str = "gpt-4o-mini",
        GenerationConfig: GenerationConfig = GenerationConfig(),
    ):
        self.client = None
        self.provider = provider

        print("Open AI Client Created")

    @property
    def capabilities(self) -> Dict[str, bool]:
        """Defines the capabilities of the OpenAI Client class."""
        return {"chat": True, "completion": True, "embedding": False}

    def _get_client(self) -> None:
        if self.provider.lower() == "azure":
            # self.client = AzureOpenAI()
            print("Azure Client Created")
        else:
            self.client = OpenAI()
            print("OpenAI Client Created")

    def chat(self, message: str):
        """
        chat(messages: List[dict], **kwargs) -> str
        For providers that use structured conversation format (OpenAI, Anthropic, etc.).

        Input: list of messages ({"role": "user"/"system"/"assistant", "content": "..."})

        Output: generated assistant message.
        """
        return "This is chat function called."

    def generate_text(self, prompt: str):
        return "This is generate text function called"
