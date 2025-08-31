import os
from typing import Dict, List, Any

from openai import OpenAI, AzureOpenAI
from openai.types.chat import ChatCompletion

from .base import BaseLLM
from ..models import GenerationConfig, Message, LLMResponse


"""
Todo:
- add token counter.
- Add cache service for same question
"""

"""
Bugs:
- Not able to read api key when load_dotenv used in notebook in python api
"""


class OpenAIClient(BaseLLM):
    def __init__(
        self,
        api_key: str = None,
        provider: str = "openai",
        base_url: str = "",
        organization: str = "",
        api_version: str = None,
        azure_endpoint: str = None,
        model_name: str = "gpt-4o-mini",
    ):
        self.client = None
        self.provider = provider

        super().__init__(provider=provider, model_name=model_name)

        self.api_key = api_key if api_key else os.environ["OPENAI_API_KEY"]

        self.client_args = {
            "api_key": self.api_key,
            "organization": organization,
            "api_version": api_version,
            "azure_endpoint": azure_endpoint,
        }

        self.client_args = {k: v for k, v in self.client_args.items() if v}

        if not self.api_key:
            raise ValueError(
                "OpenAI key not set. Either pass pass to function or set environment variable `OPENAI_API_KEY` "
            )

        self.client = self._get_client()

    @property
    def capabilities(self) -> Dict[str, bool]:
        """Defines the capabilities of the OpenAI Client class."""
        return {"chat": True, "completion": True, "embedding": False}

    def _set_model(self, config: GenerationConfig):
        config.model_name = self.model_name
        return config

    def _get_client(self) -> None:
        if self.provider.lower() == "azure":
            self.client: AzureOpenAI
            return AzureOpenAI()

        else:
            self.client: OpenAI
            return OpenAI()

    def chat(
        self, messages: List[Message], gen_config: GenerationConfig = GenerationConfig()
    ):
        """
        chat(messages: List[dict], **kwargs) -> str
        For providers that use structured conversation format (OpenAI, Anthropic, etc.).

        Input: list of messages ({"role": "user"/"system"/"assistant", "content": "..."})

        Output: generated assistant message.
        """
        if gen_config.model_name is None:
            gen_config = self._set_model(gen_config)

        api_call_config = {
            "model": gen_config.model_name,
            "temperature": gen_config.temperature,
            "max_tokens": gen_config.max_tokens,
            "top_p": gen_config.top_p,
            # "top_k": gen_config.top_k,
            "messages": messages,
        }

        # Review: Chat completion needs to maintain chat history, should we move to responses api
        api_response: ChatCompletion = self.client.chat.completions.create(
            **api_call_config
        )

        # print(api_response)

        response = LLMResponse(
            text=[
                Message(**choice.message.model_dump())
                for choice in api_response.choices
            ],
            config=gen_config,
            usage=dict(api_response.usage),
        )

        return response

        # return "This is chat functison called."

    def generate_text(
        self,
        prompt: List[Message],
        gen_config: GenerationConfig = GenerationConfig(),
        response_format: Any = None,
    ) -> LLMResponse:
        if gen_config.model_name is None:
            gen_config = self._set_model(gen_config)

        api_call_config = {
            "model": gen_config.model_name,
            "temperature": gen_config.temperature,
            "max_tokens": gen_config.max_tokens,
            "top_p": gen_config.top_p,
            # "top_k": gen_config.top_k,
            "messages": prompt,
        }

        if response_format is not None:
            api_call_config["response_format"] = response_format
            api_response: ChatCompletion = self.client.chat.completions.parse(
                **api_call_config
            )
        else:
            api_response: ChatCompletion = self.client.chat.completions.create(
                **api_call_config
            )

        response = LLMResponse(
            text=[
                Message(**choice.message.model_dump())
                for choice in api_response.choices
            ],
            config=gen_config,
            usage=dict(api_response.usage),
        )

        return response
