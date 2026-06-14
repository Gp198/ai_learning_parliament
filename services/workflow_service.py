import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from typing import Dict

from agents.manager_agent import agent as manager_agent
from agents.career_growth_agent import agent as career_growth_agent
from agents.readiness_agent import agent as readiness_agent
from agents.capacity_agent import agent as capacity_agent
from agents.future_skills_agent import agent as future_skills_agent
from agents.critic_agent import agent as critic_agent
from agents.speaker_agent import agent as speaker_agent
from services.blob_kb_service import load_kb

STAKEHOLDER_AGENTS = {
    "Manager-Agent": manager_agent,
    "Career-Growth-Agent": career_growth_agent,
    "Readiness-Agent": readiness_agent,
    "Capacity-Agent": capacity_agent,
    "Future-Skills-Agent": future_skills_agent,
}

def run_stakeholder_agents(user_context: str, kb: str) -> Dict[str, str]:
    max_workers = int(os.getenv("MAX_AGENT_WORKERS", "5"))
    results: Dict[str, str] = {}

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(agent.run, user_context, kb): name
            for name, agent in STAKEHOLDER_AGENTS.items()
        }

        for future in as_completed(futures):
            name = futures[future]
            try:
                results[name] = future.result()
            except Exception as exc:
                results[name] = f"ERROR: {exc}"

    # Return in Foundry workflow order
    return {name: results.get(name, "") for name in STAKEHOLDER_AGENTS.keys()}

def build_critic_input(user_context: str, stakeholder_results: Dict[str, str]) -> str:
    return f"""Proposal:
{user_context}

Manager Agent Response:
{stakeholder_results.get("Manager-Agent", "")}

Career Growth Agent Response:
{stakeholder_results.get("Career-Growth-Agent", "")}

Readiness Agent Response:
{stakeholder_results.get("Readiness-Agent", "")}

Capacity Agent Response:
{stakeholder_results.get("Capacity-Agent", "")}

Future Skills Agent Response:
{stakeholder_results.get("Future-Skills-Agent", "")}

Validate stakeholder outputs and provide the Critic verdict.
"""

def build_speaker_input(user_context: str, stakeholder_results: Dict[str, str], critic_result: str) -> str:
    return f"""Proposal:
{user_context}

Manager Agent Response:
{stakeholder_results.get("Manager-Agent", "")}

Career Growth Agent Response:
{stakeholder_results.get("Career-Growth-Agent", "")}

Readiness Agent Response:
{stakeholder_results.get("Readiness-Agent", "")}

Capacity Agent Response:
{stakeholder_results.get("Capacity-Agent", "")}

Future Skills Agent Response:
{stakeholder_results.get("Future-Skills-Agent", "")}

Critic Agent Response:
{critic_result}

Generate the final AI Learning Parliament Decision using only stakeholder outputs and Critic verdict above.
"""

def run_parliament(user_context: str) -> dict:
    started_at = datetime.utcnow().isoformat()
    kb = load_kb()

    stakeholder_results = run_stakeholder_agents(user_context, kb)

    critic_input = build_critic_input(user_context, stakeholder_results)
    critic_result = critic_agent.run(critic_input, kb="")

    speaker_input = build_speaker_input(user_context, stakeholder_results, critic_result)
    speaker_result = speaker_agent.run(speaker_input, kb="")

    finished_at = datetime.utcnow().isoformat()

    return {
        "started_at": started_at,
        "finished_at": finished_at,
        "stakeholders": stakeholder_results,
        "critic": critic_result,
        "speaker": speaker_result,
    }
