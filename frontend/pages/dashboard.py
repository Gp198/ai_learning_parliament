import streamlit as st
from models.candidate import CandidateProfile

def candidate_form() -> CandidateProfile:
    with st.sidebar:
        st.header("Candidate Profile")

        scenario = st.selectbox("Scenario", ["Positive Outcome", "Risk-Based Outcome", "Custom"])

        if scenario == "Positive Outcome":
            defaults = {
                "current_role": "Infrastructure Project Manager",
                "target_role": "AI Transformation Lead",
                "current_certification": "AI-900",
                "target_certification": "AI-102",
                "practice_score": 82,
                "study_hours": 8,
                "meeting_hours": 10,
                "workload": "Medium",
                "manager_goal": "Accelerate AI solution delivery",
                "team_goal": "Build internal AI engineering capability",
                "question": "Should AI-102 be pursued now? Run the full AI Learning Parliament process using only internal knowledge base sources.",
                "assessment": {
                    "Prompt Engineering": 82,
                    "Responsible AI": 86,
                    "Azure AI Search": 80,
                    "AI Agents": 78,
                    "Azure OpenAI": 84,
                    "Computer Vision": 81,
                }
            }
        elif scenario == "Risk-Based Outcome":
            defaults = {
                "current_role": "AI Engineer",
                "target_role": "Senior AI Engineer",
                "current_certification": "AI-900",
                "target_certification": "AI-102",
                "practice_score": 47,
                "study_hours": 4,
                "meeting_hours": 34,
                "workload": "High",
                "manager_goal": "Achieve AI-102 within 2 months",
                "team_goal": "Increase AI delivery capability",
                "question": "Should I pursue AI-102 now or delay preparation? Assess readiness, identify risks, evaluate workload sustainability and explain the decision.",
                "assessment": {
                    "Prompt Engineering": 35,
                    "Responsible AI": 40,
                    "Azure AI Search": 42,
                    "AI Agents": 30,
                    "Azure OpenAI": 60,
                    "Computer Vision": 62,
                }
            }
        else:
            defaults = {
                "current_role": "Data Engineer",
                "target_role": "AI Engineer",
                "current_certification": "AI-900",
                "target_certification": "AI-102",
                "practice_score": 80,
                "study_hours": 8,
                "meeting_hours": 10,
                "workload": "Medium",
                "manager_goal": "Accelerate AI solution delivery",
                "team_goal": "Build internal AI engineering capability",
                "question": "Should I pursue AI-102 now?",
                "assessment": {
                    "Prompt Engineering": 70,
                    "Responsible AI": 70,
                    "Azure AI Search": 70,
                    "AI Agents": 70,
                    "Azure OpenAI": 70,
                    "Computer Vision": 70,
                }
            }

        current_role = st.text_input("Current Role", value=defaults["current_role"])
        target_role = st.text_input("Target Role", value=defaults["target_role"])
        current_certification = st.text_input("Current Certification", value=defaults["current_certification"])
        target_certification = st.text_input("Target Certification", value=defaults["target_certification"])

        practice_score = st.slider("Practice Score", 0, 100, defaults["practice_score"])
        study_hours = st.number_input("Study Hours / Week", 0, 40, defaults["study_hours"])
        meeting_hours = st.number_input("Meeting Hours / Week", 0, 60, defaults["meeting_hours"])
        workload = st.selectbox("Workload", ["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(defaults["workload"]))

        manager_goal = st.text_input("Manager Goal", value=defaults["manager_goal"])
        team_goal = st.text_input("Team Goal", value=defaults["team_goal"])

        st.subheader("Assessment Results")
        assessment_results = {}
        for topic, value in defaults["assessment"].items():
            assessment_results[topic] = st.slider(topic, 0, 100, value)

        question = st.text_area("Question", value=defaults["question"], height=120)

    return CandidateProfile(
        current_role=current_role,
        target_role=target_role,
        current_certification=current_certification,
        target_certification=target_certification,
        practice_score=practice_score,
        study_hours=study_hours,
        meeting_hours=meeting_hours,
        workload=workload,
        manager_goal=manager_goal,
        team_goal=team_goal,
        question=question,
        assessment_results=assessment_results,
    )
