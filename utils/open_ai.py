import openai


def set_api_key(key: str) -> None:
    openai.api_key = key
