from fastapi import APIRouter
from pydantic import BaseModel
import pickle
from pathlib import Path

# Load once
model = pickle.load(open(Path(__file__).parent.parent / "model" / "model.pkl", "rb"))
vectorizer = pickle.load(open(Path(__file__).parent.parent / "model" / "vectorizer.pkl", "rb"))

router = APIRouter()

class InputText(BaseModel):
    text: str

@router.post("/predict")
def predict_sentiment(input: InputText):
    vec = vectorizer.transform([input.text])
    pred = model.predict(vec)[0]
    return {"sentiment": "positive" if pred == 1 else "negative"}
