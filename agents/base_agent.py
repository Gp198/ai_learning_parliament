from pathlib import Path
from services.openai_service import ask_gpt

class BaseAgent:
    def __init__(self, name: str, prompt_file: str, use_kb: bool = True):
        self.name = name
        self.prompt_file = prompt_file
        self.use_kb = use_kb

    @property
    def instructions(self) -> str:
        return Path("prompts", self.prompt_file).read_text(encoding="utf-8")

    def run(self, context: str, kb: str = "") -> str:
        if self.use_kb:
            prompt = f"""AGENT NAME:
{self.name}

AGENT INSTRUCTIONS:
{self.instructions}

ATTACHED KNOWLEDGE BASE:
{kb}

USER / WORKFLOW CONTEXT:
{context}
"""
        else:
            prompt = f"""AGENT NAME:
{self.name}

AGENT INSTRUCTIONS:
{self.instructions}

WORKFLOW CONTEXT:
{context}
"""
        return ask_gpt(prompt)
