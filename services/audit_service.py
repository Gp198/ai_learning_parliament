import json
from datetime import datetime
from pathlib import Path

AUDIT_DIR = Path("audit")
AUDIT_DIR.mkdir(exist_ok=True)

def save_audit_record(record: dict) -> Path:
    stamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    path = AUDIT_DIR / f"decision_{stamp}.json"
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    return path
