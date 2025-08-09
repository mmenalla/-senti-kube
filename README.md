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
```
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product!"}'

```


## Deploy and Run on minikube
```
brew install minikube
minikube start --driver=docker
```

Use Local Docker for Building Images
Tell Kubernetes to use the local Docker daemon so you don’t have to push to a remote registry every time:

````
eval $(minikube docker-env)
````

Now, when you run:
```
docker build -t sentikube:latest .
```
the image will be available directly inside Minikube.

```
kubectl apply -f ....yaml
kubectl port-forward svc/sentikube-service 8000:80

kubectl apply -f configmap.yaml
kubectl rollout restart deployment sentikube-deployment
```
```
http://localhost:8000/docs
```
```
echo -n "secret_api_key" | base64
echo -n "c2VjcmV0X2FwaV9rZXk=" | base64 --decode
```

Horizontal Pod Autoscaler
Check the status of the Horizontal Pod Autoscaler:
```
kubectl get hpa sentikube-hpa
```

To test autoscaling, enable metrics-server in Minikube:
```bash
minikube addons enable metrics-server
```
Stress Test with Hey
```
brew install hey
```
```
hey -z 1m -c 20 -m POST -H "Content-Type: application/json" -d '{"text":"I love this product!"}' http://localhost:8000/predict
```


#### RBAC: Roles and RoleBindings
RBAC controls what actions the SA can perform on which resources in the cluster.

### Ingress Controller addon to minukube cluster 
```
minikube addons enable ingress
```

Check:
```
kubectl port-forward -n ingress-nginx svc/ingress-nginx-controller 8080:80
curl -H "Host: sentikube.local" http://localhost:8080/docs
```
