backend/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime
from pymongo import MongoClient, errors

# --- MongoDB Connection ---
try:
    client = MongoClient("mongodb://admin:admin123@localhost:27017/", serverSelectionTimeoutMS=2000)
    db = client["autoroute"]
    detections_col = db["detections"]
    # check connection
    client.server_info()
    print("[DB] Connected to MongoDB successfully ✅")
except errors.ServerSelectionTimeoutError as e:
    print("[DB ERROR] Could not connect to MongoDB ❌", e)
    detections_col = None

# --- FastAPI App ---
app = FastAPI(title="AutoRoute Backend", version="1.0")

# --- Schemas ---
class Detection(BaseModel):
    cls: int
    conf: float
    xyxy: List[float]

class DetectionPayload(BaseModel):
    junction_id: str
    ts: float
    detections: List[Detection]
    counts: Dict[str, int]

# --- Routes ---
@app.post("/detections")
def receive_detections(payload: DetectionPayload):
    """Receive AI detections from edge device"""
    if detections_col is None:
        raise HTTPException(status_code=500, detail="Database not available")

    doc = {
        "junction_id": payload.junction_id,
        "ts": datetime.fromtimestamp(payload.ts),
        "detections": [d.dict() for d in payload.detections],
        "counts": payload.counts
    }

    try:
        detections_col.insert_one(doc)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database insert failed: {e}")

    return {
        "status": "ok",
        "stored": True,
        "counts": payload.counts
    }

@app.get("/")
def root():
    return {"msg": "SmartFlow Backend Running 🚦"}