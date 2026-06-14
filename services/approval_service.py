import re
from datetime import datetime
from typing import Dict, Any


def extract_recommended_plan(speaker_output: str) -> str:
    match = re.search(r"Recommended Plan:\s*(.+)", speaker_output or "", re.IGNORECASE)
    if not match:
        return "Insufficient Data"
    plan = match.group(1).strip().replace("*", "").replace("`", "").strip()
    return plan or "Insufficient Data"


def extract_final_decision(speaker_output: str) -> str:
    match = re.search(r"Final Decision:\s*(.+)", speaker_output or "", re.IGNORECASE)
    if not match:
        return "Not Available"
    return match.group(1).strip().replace("*", "").replace("`", "").strip()


def extract_decision_confidence(speaker_output: str) -> str:
    match = re.search(r"Decision Confidence:\s*(.+)", speaker_output or "", re.IGNORECASE)
    if not match:
        return "Not Available"
    return match.group(1).strip().replace("*", "").replace("`", "").strip()


def build_approved_learning_plan(candidate_context: str, speaker_output: str) -> Dict[str, Any]:
    return {
        "approval_status": "APPROVED",
        "approved_at_utc": datetime.utcnow().isoformat(),
        "approved_by": "Human Reviewer",
        "created_by": ["Gonçalo Pedro", "André Collares Rodrigues"],
        "final_decision": extract_final_decision(speaker_output),
        "decision_confidence": extract_decision_confidence(speaker_output),
        "recommended_plan": extract_recommended_plan(speaker_output),
        "candidate_context": candidate_context,
        "speaker_decision": speaker_output
    }
