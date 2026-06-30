"""AI clients for different providers (OpenCode, OpenAI, Ollama)."""
from abc import ABC, abstractmethod

import requests

from .config import (
    get_opencode_url,
    get_opencode_key,
    get_openai_key,
    get_ollama_url,
)
from .prompts import SYSTEM_PROMPT


class AIClient(ABC):
    """Abstract base for AI commit message generators."""

    @abstractmethod
    def generate(self, diff: str) -> str:
        """Generate a conventional commit message from the given diff."""


class OpenCodeClient(AIClient):
    """Client for OpenCode (OpenAI-compatible API)."""

    def __init__(self, api_url=None, api_key=None, model="opencode"):
        self.api_url = api_url or get_opencode_url()
        self.api_key = api_key or get_opencode_key()
        self.model = model

    def generate(self, diff: str) -> str:
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": diff},
            ],
            "temperature": 0.2,
            "max_tokens": 60,
        }
        resp = requests.post(
            self.api_url, headers=headers, json=payload, timeout=30
        )
        resp.raise_for_status()
        try:
            data = resp.json()
            return data["choices"][0]["message"]["content"].strip()
        except (KeyError, IndexError, requests.exceptions.JSONDecodeError) as e:
            raise RuntimeError(
                f"Unexpected response format from {self.model}: {e}"
            ) from e


class OpenAIClient(AIClient):
    """Client for OpenAI API."""

    def __init__(self, api_key=None, model="gpt-4o-mini"):
        self.api_key = api_key or get_openai_key()
        self.model = model

    def generate(self, diff: str) -> str:
        if not self.api_key:
            raise ValueError(
                "OpenAI API key not set. Use OPENAI_API_KEY env var."
            )
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": diff},
            ],
            "temperature": 0.2,
            "max_tokens": 60,
        }
        resp = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        try:
            data = resp.json()
            return data["choices"][0]["message"]["content"].strip()
        except (KeyError, IndexError, requests.exceptions.JSONDecodeError) as e:
            raise RuntimeError(
                f"Unexpected response format from OpenAI: {e}"
            ) from e


class OllamaClient(AIClient):
    """Client for Ollama API."""

    def __init__(self, api_url=None, model="llama3"):
        self.api_url = api_url or get_ollama_url()
        self.model = model

    def generate(self, diff: str) -> str:
        payload = {
            "model": self.model,
            "prompt": SYSTEM_PROMPT + "\n\n" + diff,
            "stream": False,
            "options": {"temperature": 0.2},
        }
        resp = requests.post(self.api_url, json=payload, timeout=60)
        resp.raise_for_status()
        try:
            data = resp.json()
            return data["response"].strip()
        except (KeyError, requests.exceptions.JSONDecodeError) as e:
            raise RuntimeError(
                f"Unexpected response format from Ollama: {e}"
            ) from e


def get_client(
    provider: str,
    model: str = None,
    api_url: str = None,
    api_key: str = None,
) -> AIClient:
    """Factory for AI clients."""
    provider = provider.lower()
    if provider == "opencode":
        return OpenCodeClient(
            api_url=api_url, api_key=api_key, model=model or "opencode"
        )
    elif provider == "openai":
        return OpenAIClient(api_key=api_key, model=model or "gpt-4o-mini")
    elif provider == "ollama":
        return OllamaClient(api_url=api_url, model=model or "llama3")
    else:
        raise ValueError(f"Unsupported provider: {provider}")
