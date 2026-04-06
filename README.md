# DevOps Demo App

A simple Flask web app with Docker and CI/CD pipeline.

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

## Run Tests

```bash
pytest tests/ -v
```

## Docker

```bash
# Build
docker build -t devops-demo-app .

# Run
docker run -p 5000:5000 devops-demo-app
```

## CI/CD Pipeline (GitHub Actions)

On every push to `main`:
1. **Test** — installs dependencies and runs pytest
2. **Build** — builds the Docker image and runs a smoke test

## Deploy to a VM

```bash
# On the VM, pull the repo and run:
docker build -t devops-demo-app .
docker run -d -p 5000:5000 --restart unless-stopped devops-demo-app
```
