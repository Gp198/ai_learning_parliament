# AI Learning Parliament

## Multi-Agent AI System for Evidence-Based Certification Decisions

AI Learning Parliament is an enterprise-grade multi-agent decision intelligence platform built with **Azure AI Foundry**, **GPT-4.1**, **Azure Blob Storage**, and **Streamlit**.

The platform helps organizations determine whether an employee is truly ready to pursue a certification by evaluating readiness, business impact, workload sustainability, career growth alignment, and future skill relevance.

Instead of relying on a single AI response, the system simulates a structured stakeholder review process where multiple specialized agents independently assess evidence and contribute to a final recommendation.

---

# Architecture Overview

<img width="1613" height="953" alt="image" src="https://github.com/user-attachments/assets/878c11a1-c632-4c3c-9187-ae2338d19af0" />

The solution implements a multi-agent governance model inspired by executive decision-making processes.

## Core Components

### Presentation Layer

* Streamlit Enterprise Application
* Interactive Candidate Assessment Dashboard
* Human Approval Workflow
* Evidence Visualization
* Stakeholder Decision Cards

### AI Orchestration Layer

* Workflow Orchestrator
* Parallel Agent Execution
* Critic Validation Layer
* Speaker Synthesis Layer
* Human-in-the-Loop Approval

### Knowledge Layer

* Azure Blob Storage
* Foundry IQ Knowledge Base
* Role Mapping Frameworks
* Certification Guides
* Learning History
* Assessment Frameworks
* Learning Plans

### AI Reasoning Layer

* Azure AI Foundry
* GPT-4.1
* Prompt-Based Agent Specialization
* Source-Grounded Reasoning

---

# Multi-Agent Parliament

The system is composed of seven specialized agents.

## Manager Agent

Evaluates:

* Business alignment
* Team capability
* Delivery impact
* Organizational priorities

Knowledge Sources:

* manager-framework.md
* manager-goals-ai-delivery.md
* certification-role-mapping.md

---

## Career Growth Agent

Evaluates:

* Career progression
* Professional growth
* Long-term value
* Role alignment

Knowledge Sources:

* career-growth-framework.md
* certification-role-mapping.md
* role_mappings.json

---

## Readiness Agent

Evaluates:

* Practice assessments
* Knowledge gaps
* Exam readiness
* Prerequisites

Knowledge Sources:

* readiness-framework.md
* assessment-framework.md
* ai102-overview.md
* dp700.md
* ai900.md

---

## Capacity Agent

Evaluates:

* Study hours
* Meeting load
* Workload risk
* Feasibility

Knowledge Sources:

* capacity-framework.md
* study-hours-guidance.md
* workload-risk-framework.md

---

## Future Skills Agent

Evaluates:

* Future relevance
* Market demand
* Strategic importance
* Skill longevity

Knowledge Sources:

* future-skills-analysis.md
* certification-role-mapping.md

---

## Critic Agent

Responsible for:

* Contradiction detection
* Evidence quality review
* Risk identification
* Recommendation validation

The Critic Agent acts as an independent governance layer that challenges all stakeholder recommendations.

---

## Speaker Agent

Responsible for:

* Evidence synthesis
* Decision generation
* Confidence scoring
* Recommendation creation

The Speaker Agent generates the final parliament decision using the outputs from all stakeholder agents and the Critic Agent.

---

# Human Approval Layer

AI Learning Parliament incorporates Human-in-the-Loop governance.

Possible actions:

* APPROVE
* REQUEST_CHANGES

After approval, the system generates:

* Approved Learning Plan
* Study Path
* Milestones
* Timeline
* Audit Record

---

# Decision Framework

The platform can produce four outcomes.

| Outcome               | Description                                          |
| --------------------- | ---------------------------------------------------- |
| Start Now             | Candidate is ready                                   |
| Start With Conditions | Candidate can proceed after addressing specific gaps |
| Delay                 | Candidate requires additional preparation            |
| Do Not Pursue         | Certification does not currently align with goals    |

---

# Knowledge Base

The solution uses an Azure Blob Storage-backed enterprise knowledge base.

## Current Assets

### Certification Content

* ai102-overview.md
* ai900.md
* dp700.md

### Assessment Frameworks

* assessment-framework.md
* readiness-framework.md

### Capacity Frameworks

* capacity-framework.md
* workload-risk-framework.md
* study-hours-guidance.md

### Career Frameworks

* career-growth-framework.md
* certification-role-mapping.md

### Strategic Frameworks

* future-skills-analysis.md
* manager-goals-ai-delivery.md

### Learning Plans

* learning-plans.md

### Datasets

* learners.json
* learning_history.json

---

# Technology Stack

## Frontend

* Streamlit

## AI Platform

* Azure AI Foundry
* GPT-4.1

## Knowledge Base

* Azure Blob Storage

## Backend

* Python 3.11+

## Libraries

* openai
* azure-storage-blob
* streamlit
* python-dotenv
* pandas

---

# Project Structure

```text
ai-learning-parliament/
│
├── agents/
│   ├── manager_agent.py
│   ├── career_growth_agent.py
│   ├── readiness_agent.py
│   ├── capacity_agent.py
│   ├── future_skills_agent.py
│   ├── critic_agent.py
│   └── speaker_agent.py
│
├── prompts/
│   ├── manager_prompt.txt
│   ├── career_growth_prompt.txt
│   ├── readiness_prompt.txt
│   ├── capacity_prompt.txt
│   ├── future_skills_prompt.txt
│   ├── critic_prompt.txt
│   └── speaker_prompt.txt
│
├── services/
│   ├── openai_service.py
│   ├── workflow_service.py
│   ├── blob_kb_service.py
│   └── approval_service.py
│
├── frontend/
│   ├── pages/
│   ├── components/
│   └── styles/
│
├── audit/
│
├── app.py
├── requirements.txt
└── README.md
```

# Local Execution

```bash
git clone https://github.com/<repo>/AI-Learning-Parliament.git

cd AI-Learning-Parliament

python -m venv .venv

source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

# Environment Variables

```env
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_DEPLOYMENT=gpt-4.1

AZURE_STORAGE_CONNECTION_STRING=
AZURE_STORAGE_CONTAINER=ai-learning-parliament
```

---

# Key Features

✅ Multi-Agent Decision Intelligence

✅ Evidence-Based Certification Recommendations

✅ Azure AI Foundry Integration

✅ GPT-4.1 Reasoning

✅ Azure Blob Storage Knowledge Base

✅ Human-in-the-Loop Governance

✅ Audit Trail Generation

✅ Approved Learning Plan Generation

✅ Enterprise-Ready Architecture

✅ Source-Grounded Recommendations

---

# Future Roadmap

### Phase 1

* Azure Blob Storage Knowledge Base
* Multi-Agent Workflow
* Human Approval

### Phase 2

* Azure AI Search Integration
* Semantic Retrieval
* Advanced Grounding

### Phase 3

* Real Azure AI Foundry Agents
* Agent-to-Agent Communication
* Tracing and Evaluation

### Phase 4

* Microsoft Teams Integration
* Enterprise Authentication
* Certification Analytics Dashboard

---

# Authors

**Gonçalo Pedro**
AI Tech Lead 

**André Collares Rodrigues**
AI Transformation Leader

Built for the Microsoft Agents League Hackathon and AI Skills Fest using Azure AI Foundry and GPT-4.1.

