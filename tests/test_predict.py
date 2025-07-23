from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_positive():
    response = client.post("/predict", json={"text": "I love this!"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"
