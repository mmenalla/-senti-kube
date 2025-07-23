# SentiKube

>  Real-time sentiment analysis served via FastAPI and Docker.

![SentiKube Banner](https://img.shields.io/badge/FastAPI-brightgreen?style=flat-square)
![Dockerized](https://img.shields.io/badge/Docker-ready-blue?style=flat-square)
![Kubernetes](https://img.shields.io/badge/K8s-deployable-blueviolet?style=flat-square)

---

## 📖 What is SentiKube?

**SentiKube** is a containerized ML inference API for **sentiment analysis**. It's built for fun, learning, and deploying on **Kubernetes**.
---

## 🧰 Tech Stack

| Tool          | Purpose                          |
|---------------|----------------------------------|
| **FastAPI**   | High-performance inference API   |
| **Scikit-learn** | Trained sentiment model        |
| **Docker**    | Containerize the app             |
| **Makefile**  | Dev workflow automation          |
| **Pickle**    | Model packaging format           |
| **Kubernetes**| (Next phase!) Cluster deployment |

---

##  Quickstart (Local)

### 1. Train the Model
```bash
make train
```
### 2. Run the fastapi server
```bash
make run
```
#### 3. Make a prediction
```bash
make predict
```

### 4. To see the API docs go to:
```bash
http://localhost:8000/docs
```