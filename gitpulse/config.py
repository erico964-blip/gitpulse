"""Configuration from environment variables."""
import os


def get_opencode_url() -> str:
    return os.environ.get(
        "OPENCODE_API_URL", "http://localhost:8080/v1/chat/completions"
    )


def get_opencode_key() -> str:
    return os.environ.get("OPENCODE_API_KEY", "")


def get_openai_key() -> str:
    return os.environ.get("OPENAI_API_KEY", "")


def get_ollama_url() -> str:
    return os.environ.get("OLLAMA_API_URL", "http://localhost:11434/api/generate")
