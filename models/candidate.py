from pydantic import BaseModel, Field
from typing import Dict

class CandidateProfile(BaseModel):
    current_role: str = Field(default="")
    target_role: str = Field(default="")
    current_certification: str = Field(default="")
    target_certification: str = Field(default="")
    practice_score: int = Field(default=80)
    study_hours: int = Field(default=8)
    meeting_hours: int = Field(default=10)
    workload: str = Field(default="Medium")
    manager_goal: str = Field(default="")
    team_goal: str = Field(default="")
    question: str = Field(default="")
    assessment_results: Dict[str, int] = Field(default_factory=dict)

    def to_prompt(self) -> str:
        assessment = "\n".join([f"- {k}: {v}%" for k, v in self.assessment_results.items()])
        return f"""Candidate Profile

Current Role: {self.current_role}
Target Role: {self.target_role}
Current Certification: {self.current_certification}
Target Certification: {self.target_certification}
Practice Score: {self.practice_score}%
Study Hours Per Week: {self.study_hours}
Meeting Hours Per Week: {self.meeting_hours}
Workload: {self.workload}
Manager Goal: {self.manager_goal}
Team Goal: {self.team_goal}

Assessment Results:
{assessment}

Question:
{self.question}
"""
