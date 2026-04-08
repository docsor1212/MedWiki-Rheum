"""
MedWiki-Rheum Clinical Tools API
统一入口 - FastAPI 单文件，端口 8000
启动: python3 api/server.py
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime
from pathlib import Path
import json, uvicorn

app = FastAPI(title="MedWiki-Rheum Clinical Tools API", version="1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

HISTORY_DIR = Path(__file__).parent.parent / "data" / "history"

# ─── SLEDAI-2000 ───────────────────────────────────────────

SLEDAI_CRITERIA = {
    "发热": 1, "PLT低": 1, "WBC低": 1,
    "脱发": 2, "皮疹": 2, "黏膜溃疡": 2, "胸膜炎": 2, "心包炎": 2, "低补体": 2, "dsDNA阳性": 2,
    "关节炎": 4, "肌炎": 4, "管型尿": 4, "血尿": 4, "蛋白尿": 4, "脓尿": 4,
    "癫痫": 8, "精神症状": 8, "器质性脑病": 8, "视觉障碍": 8, "颅神经病": 8, "狼疮头痛": 8, "CVA": 8, "脉管炎": 8,
}

class SLEDAIRequest(BaseModel):
    patient_id: str
    selected_items: List[str]
    notes: Optional[str] = None

@app.post("/api/sledai/calculate")
async def sledai_calc(req: SLEDAIRequest):
    item_scores = {}
    total = 0
    for item in req.selected_items:
        s = SLEDAI_CRITERIA.get(item, 0)
        if s > 0:
            item_scores[item] = s
            total += s

    if total <= 4:
        level, color = ("无疾病活动" if total == 0 else "基本无活动"), "green"
    elif total <= 9:
        level, color = "轻度活动", "orange"
    elif total <= 14:
        level, color = "中度活动", "red"
    else:
        level, color = "重度活动", "darkred"

    ts = datetime.now().isoformat()
    result = {"patient_id": req.patient_id, "total_score": total, "activity_level": level,
              "activity_color": color, "item_scores": item_scores, "timestamp": ts, "notes": req.notes}
    _save(req.patient_id, "sledai_2000", result)
    return result

# ─── APS分类 ───────────────────────────────────────────────

class APSRequest(BaseModel):
    patient_id: str
    clinical_domains: Dict[str, int]
    lab_domains: Dict[str, int]
    notes: Optional[str] = None

@app.post("/api/aps/classify")
async def aps_classify(req: APSRequest):
    cs = sum(req.clinical_domains.values())
    ls = sum(req.lab_domains.values())
    meets = cs >= 3 and ls >= 3
    ts = datetime.now().isoformat()
    result = {"patient_id": req.patient_id, "clinical_score": cs, "lab_score": ls,
              "meets_criteria": meets, "diagnosis": "符合APS分类标准" if meets else "不符合APS分类标准",
              "clinical_domains": req.clinical_domains, "lab_domains": req.lab_domains,
              "timestamp": ts, "notes": req.notes}
    _save(req.patient_id, "aps_classification", result)
    return result

# ─── SLE分类 ───────────────────────────────────────────────

class SLEClassifyRequest(BaseModel):
    patient_id: str
    ana_positive: bool
    clinical_domains: Dict[str, int]
    immuno_domains: Dict[str, int]
    notes: Optional[str] = None

@app.post("/api/sle/classify")
async def sle_classify(req: SLEClassifyRequest):
    cs = sum(req.clinical_domains.values())
    ims = sum(req.immuno_domains.values())
    total = cs + ims
    has_clinical = len(req.clinical_domains) > 0

    if not req.ana_positive:
        diagnosis = "ANA阴性，不符合分类标准"
        meets = False
    elif total < 10:
        diagnosis = f"积分不足({total}<10)，不符合分类标准"
        meets = False
    elif not has_clinical:
        diagnosis = "缺少临床标准，不符合分类标准"
        meets = False
    else:
        diagnosis = "符合SLE分类标准"
        meets = True

    ts = datetime.now().isoformat()
    result = {"patient_id": req.patient_id, "ana_positive": req.ana_positive,
              "total_score": total, "has_clinical": has_clinical, "meets_criteria": meets,
              "diagnosis": diagnosis, "clinical_domains": req.clinical_domains,
              "immuno_domains": req.immuno_domains, "timestamp": ts, "notes": req.notes}
    _save(req.patient_id, "sle_classification", result)
    return result

# ─── 历史记录 ──────────────────────────────────────────────

@app.get("/api/history/{patient_id}")
async def get_history(patient_id: str, tool: Optional[str] = None, limit: int = 20):
    history = _load_all(patient_id)
    if tool:
        history = [r for r in history if r.get("tool") == tool]
    return {"patient_id": patient_id, "count": len(history), "history": history[-limit:]}

@app.get("/api/history/{patient_id}/{tool}")
async def get_history_tool(patient_id: str, tool: str, limit: int = 20):
    records = _load(patient_id, tool)
    return {"patient_id": patient_id, "tool": tool, "count": len(records), "history": records[-limit:]}

@app.delete("/api/history/{patient_id}")
async def clear_history(patient_id: str, tool: Optional[str] = None):
    if tool:
        f = HISTORY_DIR / f"{patient_id}_{tool}.json"
        if f.exists(): f.unlink()
    else:
        for f in HISTORY_DIR.glob(f"{patient_id}_*.json"):
            f.unlink()
    return {"status": "cleared"}

# ─── 根路由 ────────────────────────────────────────────────

@app.get("/")
async def root():
    return {"service": "MedWiki-Rheum Clinical Tools API", "version": "1.0",
            "endpoints": {
                "sledai": ["/api/sledai/calculate (POST)", "/api/history/{pid}/sledai_2000 (GET)"],
                "aps": ["/api/aps/classify (POST)", "/api/history/{pid}/aps_classification (GET)"],
                "sle": ["/api/sle/classify (POST)", "/api/history/{pid}/sle_classification (GET)"],
                "history": ["/api/history/{pid} (GET)", "/api/history/{pid}/{tool} (GET)", "/api/history/{pid} (DELETE)"],
            }}

@app.get("/health")
async def health():
    return {"status": "healthy", "history_files": len(list(HISTORY_DIR.glob("*.json")))}

# ─── 存储层 ────────────────────────────────────────────────

def _save(patient_id: str, tool: str, record: dict):
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    f = HISTORY_DIR / f"{patient_id}_{tool}.json"
    records = json.loads(f.read_text("utf-8")) if f.exists() else []
    record["tool"] = tool
    records.append(record)
    f.write_text(json.dumps(records, ensure_ascii=False, indent=2), "utf-8")

def _load(patient_id: str, tool: str) -> list:
    f = HISTORY_DIR / f"{patient_id}_{tool}.json"
    return json.loads(f.read_text("utf-8")) if f.exists() else []

def _load_all(patient_id: str) -> list:
    all_records = []
    for f in HISTORY_DIR.glob(f"{patient_id}_*.json"):
        all_records.extend(json.loads(f.read_text("utf-8")))
    all_records.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
    return all_records

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
