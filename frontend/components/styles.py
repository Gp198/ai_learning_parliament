import streamlit as st

def load_styles():
    st.markdown("""
    <style>
    :root{--ms-blue:#0F6CBD;--ms-green:#107C10;--ms-red:#D13438;--ms-border:#E1E7EF;--ms-text:#1B1A19;--ms-muted:#605E5C;}
    html,body,[class*="css"]{font-family:"Segoe UI",Arial,sans-serif;}
    .block-container{padding-top:2rem;padding-bottom:3rem;max-width:1500px;}
    [data-testid="stSidebar"]{background:linear-gradient(180deg,#F8FBFF 0%,#F3F6FA 100%);border-right:1px solid var(--ms-border);}
    .hero{background:radial-gradient(circle at top left,rgba(15,108,189,.18),transparent 30%),linear-gradient(135deg,#FFF 0%,#F1F7FF 100%);border:1px solid #CFE4FA;border-radius:22px;padding:28px 32px;margin-bottom:22px;box-shadow:0 10px 28px rgba(15,108,189,.08);}
    .main-title{font-size:44px;line-height:1.05;font-weight:850;color:var(--ms-blue);letter-spacing:-.8px;margin:0;}
    .subtitle{color:#3B556F;font-size:15px;margin-top:8px;max-width:980px;}
    .creator-line{margin-top:14px;color:#31425A;font-size:14px;font-weight:600;}
    .creator-pill{display:inline-block;background:#EAF4FF;color:#084E8A;border:1px solid #BBDCF8;padding:5px 10px;border-radius:999px;margin-left:6px;font-weight:700;}
    .metric-card{background:#FFF;border:1px solid var(--ms-border);border-radius:18px;padding:18px 20px;box-shadow:0 6px 18px rgba(0,0,0,.04);min-height:112px;}
    .metric-label{font-size:12px;text-transform:uppercase;letter-spacing:.6px;font-weight:800;color:var(--ms-muted);}
    .metric-value{font-size:34px;font-weight:850;color:var(--ms-text);margin-top:6px;}
    .section-header{display:flex;align-items:center;gap:10px;margin-top:32px;margin-bottom:14px;}
    .section-icon{width:34px;height:34px;border-radius:10px;display:inline-flex;align-items:center;justify-content:center;background:#EAF4FF;color:var(--ms-blue);font-weight:900;border:1px solid #CFE4FA;}
    .section-title{font-size:25px;font-weight:850;color:var(--ms-text);letter-spacing:-.3px;}
    .agent-card{position:relative;background:#FFF;border:1px solid var(--ms-border);border-radius:18px;padding:18px 16px;min-height:385px;box-shadow:0 8px 22px rgba(0,0,0,.045);overflow:hidden;}
    .agent-card:before{content:"";position:absolute;top:0;left:0;height:5px;width:100%;background:var(--agent-color,var(--ms-blue));}
    .agent-card-header{display:flex;align-items:center;gap:12px;margin-bottom:14px;}
    .agent-avatar{width:42px;height:42px;border-radius:50%;color:white;display:flex;align-items:center;justify-content:center;font-size:21px;box-shadow:0 8px 18px rgba(0,0,0,.15);}
    .agent-title{font-size:15px;font-weight:850;color:#242424;line-height:1.1;}
    .agent-role{font-size:11px;color:var(--ms-muted);font-weight:700;text-transform:uppercase;letter-spacing:.5px;margin-top:3px;}
    .agent-output{font-size:13px;line-height:1.48;color:#252423;word-break:break-word;}
    .critic-panel{background:linear-gradient(135deg,#FFF7F7 0%,#FFF 100%);border:1px solid #F2B8BA;border-left:8px solid var(--ms-red);border-radius:18px;padding:22px 24px;box-shadow:0 8px 22px rgba(209,52,56,.07);font-size:15px;}
    .decision-panel{background:linear-gradient(135deg,#F3FFF3 0%,#FFF 100%);border:1px solid #BFE8BF;border-left:8px solid var(--ms-green);border-radius:18px;padding:24px 26px;box-shadow:0 8px 22px rgba(16,124,16,.08);font-size:15px;}
    .approval-panel{background:#FFF;border:1px solid var(--ms-border);border-radius:18px;padding:20px;box-shadow:0 8px 22px rgba(0,0,0,.04);margin-top:10px;}
    .status-ribbon{display:inline-flex;align-items:center;gap:8px;padding:8px 12px;border-radius:999px;font-size:13px;font-weight:800;background:#EAF4FF;color:#084E8A;border:1px solid #BBDCF8;margin-right:8px;}
    .kb-success{padding:14px 16px;background:#F3FFF3;border:1px solid #BFE8BF;border-radius:14px;color:#107C10;font-weight:700;}
    .footer{margin-top:44px;padding:18px 22px;border-top:1px solid var(--ms-border);color:var(--ms-muted);font-size:13px;text-align:center;}
    .footer b{color:#323130;}
    div[data-testid="stButton"]>button[kind="primary"]{background:linear-gradient(135deg,#0F6CBD 0%,#084E8A 100%);border:0;border-radius:10px;font-weight:800;height:42px;box-shadow:0 6px 14px rgba(15,108,189,.20);}
    div[data-testid="stButton"]>button{border-radius:10px;font-weight:700;height:42px;}
    @media(max-width:1200px){.agent-card{min-height:auto;}}
    @media(max-width:700px){.main-title{font-size:34px;}}
    </style>
    """, unsafe_allow_html=True)

def section_header(icon: str, title: str):
    st.markdown(f'<div class="section-header"><div class="section-icon">{icon}</div><div class="section-title">{title}</div></div>', unsafe_allow_html=True)

def metric_card(label: str, value: str):
    st.markdown(f'<div class="metric-card"><div class="metric-label">{label}</div><div class="metric-value">{value}</div></div>', unsafe_allow_html=True)
