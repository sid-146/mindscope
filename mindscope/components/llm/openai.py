from .base import BaseLLM
from openai import OpenAI, AzureOpenAI
from models import GenerationConfig


class OpenAIClient(BaseLLM):
    def __init__(
        self,
        provider: str,
        api_key: str,
        base_url: str,
        organization: str,
        model: str,
        GenerationConfig: GenerationConfig = GenerationConfig(),
    ):
        self.client = None
        self.provider = provider

        print("Open AI Client Created")

    def _get_client(self):
        if self.provider.lower() == "azure":
            self.client = AzureOpenAI()
        else:
            self.client = OpenAI()

    def chat(self, message):
        """
        chat(messages: List[dict], **kwargs) -> str
        For providers that use structured conversation format (OpenAI, Anthropic, etc.).

        Input: list of messages ({"role": "user"/"system"/"assistant", "content": "..."})

        Output: generated assistant message.
        """
