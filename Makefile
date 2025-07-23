.PHONY: all install train run docker-build docker-run predict

LOCAL_REGISTRY = localhost:5000
IMAGE_NAME = megi/sentikube
TAG = latest

all: install train run
install:
	pip install -r requirements.txt

train:
	python app/model/train_model.py

run:
	uvicorn app.main:app --reload

docker-build:
	docker build -t megi/sentikube .

docker-run:
	docker run -p 8000:8000 megi/sentikube

predict:
	curl -X POST http://localhost:8000/predict \
	  -H "Content-Type: application/json" \
	  -d '{"text": "This is amazing!"}' | jq
