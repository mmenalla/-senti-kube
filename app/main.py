from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from pathlib import Path

app = FastAPI(title="SentiKube")

# Load model & vectorizer
model_dir = Path(__file__).parent / "model"
model = pickle.load(open(model_dir / "model.pkl", "rb"))
vectorizer = pickle.load(open(model_dir / "vectorizer.pkl", "rb"))

class InputText(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "SentiKube API - use /predict"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(input: InputText):
    vec = vectorizer.transform([input.text])
    pred = model.predict(vec)[0]
    sentiment = "positive" if pred == 1 else "negative"
    return {"sentiment": sentiment}
