import os
from openai import OpenAI

def _client() -> OpenAI:
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")

    if not endpoint:
        raise ValueError("AZURE_OPENAI_ENDPOINT is missing. Use the Foundry endpoint ending in /openai/v1.")
    if not api_key:
        raise ValueError("AZURE_OPENAI_API_KEY is missing.")

    return OpenAI(base_url=endpoint, api_key=api_key)

def ask_gpt(prompt: str, model: str | None = None, temperature: float = 0.1) -> str:
    deployment = model or os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4.1")
    response = _client().responses.create(
        model=deployment,
        input=prompt,
        temperature=temperature,
    )
    return response.output_text
