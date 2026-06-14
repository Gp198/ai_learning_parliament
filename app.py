import streamlit as st
from dotenv import load_dotenv
import html

load_dotenv()

from frontend.components.styles import load_styles, section_header, metric_card
from frontend.pages.dashboard import candidate_form
from services.workflow_service import run_parliament
from services.blob_kb_service import list_kb_files
from services.audit_service import save_audit_record

st.set_page_config(page_title="AI Learning Parliament", page_icon="🏛️", layout="wide")
load_styles()

st.markdown("""
<div class="hero">
  <div class="main-title">AI Learning Parliament</div>
  <div class="subtitle">Enterprise multi-agent system for evidence-based certification decisions, powered by Azure AI Foundry, GPT-4.1 and Blob Storage Knowledge Base.</div>
  <div class="creator-line">Created by <span class="creator-pill">Gonçalo Pedro</span><span class="creator-pill">André Collares Rodrigues</span></div>
</div>
""", unsafe_allow_html=True)

candidate = candidate_form()

m1, m2, m3, m4 = st.columns(4)
with m1:
    metric_card("Target Certification", candidate.target_certification)
with m2:
    metric_card("Practice Score", f"{candidate.practice_score}%")
with m3:
    metric_card("Study Hours", f"{candidate.study_hours}/week")
with m4:
    metric_card("Meeting Hours", f"{candidate.meeting_hours}/week")

with st.expander("Knowledge Base Files", expanded=False):
    try:
        files = list_kb_files()
        st.markdown(f"<div class='kb-success'>✅ {len(files)} knowledge files loaded from Azure Blob Storage.</div>", unsafe_allow_html=True)
        st.write(files)
    except Exception as exc:
        st.error(f"Could not load KB files: {exc}")

run_col, info_col = st.columns([1, 3])
with run_col:
    run_clicked = st.button("Run AI Learning Parliament", type="primary", use_container_width=True)
with info_col:
    st.markdown("""
    <span class="status-ribbon">Foundry GPT-4.1</span>
    <span class="status-ribbon">Blob KB</span>
    <span class="status-ribbon">Parallel Agents</span>
    <span class="status-ribbon">Human Approval</span>
    """, unsafe_allow_html=True)

if run_clicked:
    user_context = candidate.to_prompt()
    with st.spinner("Running stakeholder agents, Critic Agent and Speaker Agent..."):
        result = run_parliament(user_context)
        st.session_state["parliament_result"] = result
        st.session_state["candidate_context"] = user_context

result = st.session_state.get("parliament_result")

def agent_avatar(name: str) -> str:
    return {
        "Manager-Agent": "👔",
        "Career-Growth-Agent": "🚀",
        "Readiness-Agent": "🎓",
        "Capacity-Agent": "⏱️",
        "Future-Skills-Agent": "💡",
    }.get(name, "🤖")

def agent_color(name: str) -> str:
    return {
        "Manager-Agent": "#0F6CBD",
        "Career-Growth-Agent": "#107C10",
        "Readiness-Agent": "#5C2D91",
        "Capacity-Agent": "#CA5010",
        "Future-Skills-Agent": "#0078D4",
    }.get(name, "#0F6CBD")

def render_agent_card(name: str, output: str):
    safe_name = html.escape(name)
    safe_output = html.escape(output).replace("\n", "<br/>")
    avatar = agent_avatar(name)
    color = agent_color(name)
    st.markdown(f"""
    <div class="agent-card" style="--agent-color:{color};">
      <div class="agent-card-header">
        <div class="agent-avatar" style="background:{color};">{avatar}</div>
        <div>
          <div class="agent-title">{safe_name}</div>
          <div class="agent-role">Stakeholder Agent</div>
        </div>
      </div>
      <div class="agent-output">{safe_output}</div>
    </div>
    """, unsafe_allow_html=True)

if result:
    section_header("👥", "Stakeholder Agents")
    cols = st.columns(5)
    for idx, (name, output) in enumerate(result["stakeholders"].items()):
        with cols[idx]:
            render_agent_card(name, output)

    section_header("🛡️", "Critic Agent")
    st.markdown('<div class="critic-panel">', unsafe_allow_html=True)
    st.markdown(result["critic"])
    st.markdown('</div>', unsafe_allow_html=True)

    section_header("🏛️", "Speaker Agent Decision")
    st.markdown('<div class="decision-panel">', unsafe_allow_html=True)
    st.markdown(result["speaker"])
    st.markdown('</div>', unsafe_allow_html=True)

    section_header("✅", "Human Approval")
    st.markdown('<div class="approval-panel">', unsafe_allow_html=True)
    left, right = st.columns(2)

    with left:
        if st.button("APPROVE", type="primary", use_container_width=True):
            audit_path = save_audit_record({
                "status": "APPROVED",
                "candidate": st.session_state.get("candidate_context"),
                "result": result,
                "created_by": ["Gonçalo Pedro", "André Collares Rodrigues"],
            })
            st.success(f"Approved learning plan. Audit saved: {audit_path}")

    with right:
        if st.button("REQUEST_CHANGES", use_container_width=True):
            audit_path = save_audit_record({
                "status": "REQUEST_CHANGES",
                "candidate": st.session_state.get("candidate_context"),
                "result": result,
                "created_by": ["Gonçalo Pedro", "André Collares Rodrigues"],
            })
            st.warning(f"Changes requested. Audit saved: {audit_path}")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    <b>AI Learning Parliament</b> · Created by <b>Gonçalo Pedro</b> and <b>André Collares Rodrigues</b> · Azure AI Foundry · GPT-4.1 · Multi-Agent Governance
</div>
""", unsafe_allow_html=True)
