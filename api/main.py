"""
MedWiki-Rheum Clinical Tools API
FastAPI backend exposing static calculator logic as REST endpoints.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import math

app = FastAPI(
    title="MedWiki-Rheum Clinical Tools API",
    description="儿科风湿免疫临床工具API — 仅供临床参考，不构成诊疗建议",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Models ───────────────────────────────────────────────

class JADASInput(BaseModel):
    joints: int = Field(..., ge=0, le=71, description="活动关节数")
    phga: float = Field(..., ge=0, le=10, description="医生整体评估 PhGA")
    ptga: float = Field(..., ge=0, le=10, description="患者/家长整体评估 PtGA")
    esr: float = Field(0, ge=0, description="ESR (mm/h)")

class BSAInput(BaseModel):
    weight: float = Field(..., gt=0, description="体重 (kg)")
    height: float | None = Field(None, gt=0, description="身高 (cm), Mosteller/Haycock需要")

class MTXInput(BaseModel):
    weight: float = Field(..., gt=0, description="体重 (kg)")
    route: str = Field("oral", pattern="^(oral|sc|im)$", description="给药途径")

class ESRInput(BaseModel):
    esr: float = Field(..., ge=0, description="ESR (mm/h)")
    age: int = Field(..., ge=0, le=18, description="年龄")

class CRPInput(BaseModel):
    crp: float = Field(..., ge=0, description="CRP (mg/L)")
    age: int = Field(..., ge=0, le=18, description="年龄")

class BMIInput(BaseModel):
    weight: float = Field(..., gt=0, description="体重 (kg)")
    height: float = Field(..., gt=0, description="身高 (cm)")
    age: float = Field(..., ge=2, le=20, description="年龄")
    sex: str = Field(..., pattern="^(male|female)$", description="性别")

class SLEDAIInput(BaseModel):
    """SLEDAI-2K: each field is 0 or 1 for presence/absence."""
    seizure: int = Field(0, ge=0, le=1)
    psychosis: int = Field(0, ge=0, le=1)
    organic_brain: int = Field(0, ge=0, le=1)
    visual_disturbance: int = Field(0, ge=0, le=1)
    cranial_neuropathy: int = Field(0, ge=0, le=1)
    lupus_headache: int = Field(0, ge=0, le=1)
    cerebrovascular: int = Field(0, ge=0, le=1)
    vasculitis: int = Field(0, ge=0, le=1)
    arthritis: int = Field(0, ge=0, le=1)
    myositis: int = Field(0, ge=0, le=1)
    urinary_casts: int = Field(0, ge=0, le=1)
    hematuria: int = Field(0, ge=0, le=1)
    proteinuria: int = Field(0, ge=0, le=1)
    pyuria: int = Field(0, ge=0, le=1)
    rash: int = Field(0, ge=0, le=1)
    alopecia: int = Field(0, ge=0, le=1)
    mucosal_ulcer: int = Field(0, ge=0, le=1)
    pleurisy: int = Field(0, ge=0, le=1)
    pericarditis: int = Field(0, ge=0, le=1)
    low_complement: int = Field(0, ge=0, le=1)
    anti_dsDNA: int = Field(0, ge=0, le=1)
    fever: int = Field(0, ge=0, le=1)
    thrombocytopenia: int = Field(0, ge=0, le=1)
    leukopenia: int = Field(0, ge=0, le=1)

class CHAQInput(BaseModel):
    """CHAQ: 30 items across 8 domains, each 0-3."""
    dressing: list[float] = Field(..., min_length=1, max_length=5)
    rising: list[float] = Field(..., min_length=1, max_length=5)
    eating: list[float] = Field(..., min_length=1, max_length=5)
    walking: list[float] = Field(..., min_length=1, max_length=5)
    hygiene: list[float] = Field(..., min_length=1, max_length=5)
    reach: list[float] = Field(..., min_length=1, max_length=5)
    grip: list[float] = Field(..., min_length=1, max_length=5)
    activities: list[float] = Field(..., min_length=1, max_length=5)

# ─── Endpoints ────────────────────────────────────────────

@app.get("/")
def root():
    return {
        "service": "MedWiki-Rheum Clinical Tools API",
        "version": "1.0.0",
        "endpoints": [
            "/jadas27", "/jadas71", "/das28", "/cdai", "/sdai",
            "/bsa", "/mtx-dose", "/esr", "/crp", "/bmi",
            "/sledai2k", "/chaq",
        ],
        "disclaimer": "本API仅供临床参考，不构成诊疗建议",
    }


@app.post("/jadas27")
def calc_jadas27(d: JADASInput):
    """JADAS-27: joints(0-27) + PhGA + PtGA + ESR归一化"""
    esr_norm = 0 if d.esr <= 20 else min(10, d.esr / 10)
    score = d.joints + d.phga + d.ptga + esr_norm
    if score <= 1.0:
        status, color = "不活动", "#22a87e"
    elif score <= 3.8:
        status, color = "低活动度", "#20a39e"
    elif score <= 10.5:
        status, color = "中活动度", "#d4892a"
    else:
        status, color = "高活动度", "#d45050"
    return {
        "score": round(score, 2),
        "components": {"joints": d.joints, "phga": d.phga, "ptga": d.ptga, "esr_norm": round(esr_norm, 2)},
        "status": status,
        "color": color,
        "disclaimer": "仅供临床参考，不构成诊疗建议",
    }


@app.post("/jadas71")
def calc_jadas71(d: JADASInput):
    """JADAS-71: same formula, joints max=71"""
    return calc_jadas27(d)  # Same formula, different joint count range


class DAS28Input(BaseModel):
    tender: int = Field(..., ge=0, le=28, description="压痛关节数")
    swollen: int = Field(..., ge=0, le=28, description="肿胀关节数")
    esr: float = Field(..., ge=0, description="ESR (mm/h)")
    ptga: float = Field(..., ge=0, le=100, description="患者整体评估 VAS 0-100")

@app.post("/das28")
def calc_das28(d: DAS28Input):
    """DAS28-ESR"""
    score = 0.56 * math.sqrt(d.tender) + 0.28 * math.sqrt(d.swollen) + 0.7 * math.log(d.esr + 1) + 0.014 * d.ptga
    if score < 2.6:
        status = "缓解"
    elif score < 3.2:
        status = "低活动度"
    elif score <= 5.1:
        status = "中活动度"
    else:
        status = "高活动度"
    return {"score": round(score, 2), "status": status, "disclaimer": "仅供临床参考，不构成诊疗建议"}


@app.post("/bsa")
def calc_bsa(d: BSAInput):
    """BSA计算 — 5种公式，含中国教材分段公式"""
    results = {}
    w, h = d.weight, d.height

    # 中国教材分段公式（诸福棠）
    if w <= 30:
        cn = w * 0.035 + 0.1
    else:
        cn = (w - 30) * 0.02 + 1.05
    results["chinese_textbook"] = {"bsa": round(cn, 4), "unit": "m²",
        "warning": "30kg处存在0.08m²断崖(Lam TK 2022 PMID:36160791)" if w >= 28 and w <= 33 else None}

    if h:
        hm = h / 100
        # Mosteller: sqrt(w_kg * h_cm / 3600)
        results["mosteller"] = {"bsa": round(math.sqrt(w * h / 3600), 4), "unit": "m²"}
        # Haycock: 0.024265 * w^0.5378 * h^0.3964 (h in cm)
        results["haycock"] = {"bsa": round(0.024265 * (w ** 0.5378) * (h ** 0.3964), 4), "unit": "m²"}
        # DuBois: 0.007184 * w^0.425 * h^0.725 (h in cm)
        results["dubois"] = {"bsa": round(0.007184 * (w ** 0.425) * (h ** 0.725), 4), "unit": "m²"}
        # Costeff
        results["costeff"] = {"bsa": round((4 * w + 7) / (90 + w), 4), "unit": "m²"}
    else:
        # Costeff (weight-only)
        results["costeff"] = {"bsa": round((4 * w + 7) / (90 + w), 4), "unit": "m²"}

    return {"weight_kg": w, "height_cm": h, "formulas": results,
            "recommended": "haycock 或 mosteller（中国儿童精度最高，PMID:36160791）",
            "disclaimer": "仅供临床参考，不构成诊疗建议"}


@app.post("/mtx-dose")
def calc_mtx(d: MTXInput):
    """MTX剂量计算"""
    # 标准起始: 10-15 mg/m² (oral), 10-20 mg/m² (sc/im)
    # 用Mosteller估算BSA (需身高，这里用简化体重公式)
    bsa_approx = (4 * d.weight + 7) / (90 + d.weight)
    
    route = d.route
    if route == "oral":
        dose_low = round(bsa_approx * 10, 1)
        dose_high = round(bsa_approx * 15, 1)
        dose_target = round(bsa_approx * 12.5, 1)
    else:  # sc/im
        dose_low = round(bsa_approx * 10, 1)
        dose_high = round(bsa_approx * 20, 1)
        dose_target = round(bsa_approx * 15, 1)

    # 胃复安预处理建议
    antiemetic = dose_target >= 15

    return {
        "weight_kg": d.weight,
        "bsa_approx_m2": round(bsa_approx, 3),
        "route": route,
        "dose_range_mg": {"low": dose_low, "high": dose_high, "target": dose_target},
        "folic_acid": "1mg/day (非MTX日)",
        "antiemetic_recommended": antiemetic,
        "monitoring": ["CBC", "LFT", "Cr", "每4-8周"],
        "disclaimer": "仅供临床参考，不构成诊疗建议",
    }


@app.post("/esr")
def calc_esr(d: ESRInput):
    """ESR儿科参考范围判读"""
    # 儿科ESR正常上限近似: (age + 2) / 2 (简化)
    upper = max(10, (d.age + 2) // 2) if d.age < 12 else 15
    if d.esr <= upper:
        status, level = "正常", "normal"
    elif d.esr <= upper * 2:
        status, level = "轻度升高", "mild"
    elif d.esr <= upper * 4:
        status, level = "中度升高", "moderate"
    else:
        status, level = "显著升高", "severe"
    return {"esr": d.esr, "age": d.age, "upper_limit": upper,
            "status": status, "level": level,
            "disclaimer": "仅供临床参考，不构成诊疗建议"}


@app.post("/crp")
def calc_crp(d: CRPInput):
    """CRP儿科参考范围判读"""
    if d.crp < 5:
        status, level = "正常", "normal"
    elif d.crp < 20:
        status, level = "轻度升高", "mild"
    elif d.crp < 60:
        status, level = "中度升高", "moderate"
    else:
        status, level = "显著升高", "severe"
    return {"crp_mg_L": d.crp, "age": d.age, "status": status, "level": level,
            "disclaimer": "仅供临床参考，不构成诊疗建议"}


@app.post("/bmi")
def calc_bmi(d: BMIInput):
    """BMI + Z-score（WHO参考，简化版）"""
    hm = d.height / 100
    bmi = d.weight / (hm * hm)
    return {"bmi": round(bmi, 2), "weight_kg": d.weight, "height_cm": d.height,
            "note": "完整Z-score需WHO生长曲线查表，建议使用WHO AnthroPlus",
            "disclaimer": "仅供临床参考，不构成诊疗建议"}


@app.post("/sledai2k")
def calc_sledai2k(d: SLEDAIInput):
    """SLEDAI-2K评分"""
    weights = {
        "seizure": 8, "psychosis": 8, "organic_brain": 8,
        "visual_disturbance": 8, "cranial_neuropathy": 8, "lupus_headache": 8,
        "cerebrovascular": 8, "vasculitis": 8,
        "arthritis": 4, "myositis": 4,
        "urinary_casts": 4, "hematuria": 4, "proteinuria": 4, "pyuria": 4,
        "rash": 2, "alopecia": 2, "mucosal_ulcer": 2,
        "pleurisy": 2, "pericarditis": 2,
        "low_complement": 2, "anti_dsDNA": 2,
        "fever": 1, "thrombocytopenia": 1, "leukopenia": 1,
    }
    score = sum(getattr(d, k) * v for k, v in weights.items())
    active_items = [k for k, v in weights.items() if getattr(d, k)]
    if score == 0:
        status = "无活动"
    elif score <= 4:
        status = "轻度活动"
    elif score <= 10:
        status = "中度活动"
    else:
        status = "重度活动"
    return {"score": score, "active_items": active_items, "status": status,
            "disclaimer": "仅供临床参考，不构成诊疗建议"}


class CDAIInput(BaseModel):
    tender: int = Field(..., ge=0, le=28, description="压痛关节数")
    swollen: int = Field(..., ge=0, le=28, description="肿胀关节数")
    ptga: float = Field(..., ge=0, le=10, description="患者整体评估 0-10")
    phga: float = Field(..., ge=0, le=10, description="医生整体评估 0-10")

@app.post("/cdai")
def calc_cdai(d: CDAIInput):
    """CDAI (Clinical Disease Activity Index)"""
    score = d.tender + d.swollen + d.ptga + d.phga
    if score <= 2.8:
        status = "缓解"
    elif score <= 10:
        status = "低活动度"
    elif score <= 22:
        status = "中活动度"
    else:
        status = "高活动度"
    return {"score": round(score, 2), "status": status,
            "disclaimer": "仅供临床参考，不构成诊疗建议"}


class SDAIInput(BaseModel):
    tender: int = Field(..., ge=0, le=28, description="压痛关节数")
    swollen: int = Field(..., ge=0, le=28, description="肿胀关节数")
    ptga: float = Field(..., ge=0, le=10, description="患者整体评估 0-10")
    phga: float = Field(..., ge=0, le=10, description="医生整体评估 0-10")
    crp: float = Field(..., ge=0, description="CRP mg/dL (注意单位)")

@app.post("/sdai")
def calc_sdai(d: SDAIInput):
    """SDAI (Simplified Disease Activity Index)"""
    score = d.tender + d.swollen + d.ptga + d.phga + d.crp
    if score <= 3.3:
        status = "缓解"
    elif score <= 11:
        status = "低活动度"
    elif score <= 26:
        status = "中活动度"
    else:
        status = "高活动度"
    return {"score": round(score, 2), "status": status,
            "disclaimer": "仅供临床参考，不构成诊疗建议"}


# ─── Run ──────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
