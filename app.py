from fastapi import FastAPI
import json, os

app = FastAPI(title="AB Test Metrics")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    if not os.path.exists("metrics.json"):
        return {"available": False, "error": "metrics.json not found"}
    with open("metrics.json") as f:
        data = json.load(f)
    return {"available": True, "metrics": data}