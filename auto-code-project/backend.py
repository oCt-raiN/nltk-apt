# FastAPI backend for code prediction
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model.predict import CodePredictor

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

predictor = CodePredictor()

class PredictRequest(BaseModel):
    code: str

@app.post("/predict")
def predict(req: PredictRequest):
    suggestion = predictor.predict_next_token(req.code, max_new_tokens=20)
    return {"suggestion": req.code + suggestion}
