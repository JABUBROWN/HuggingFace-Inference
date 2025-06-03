# HuggingFace Inference Container Demo

This repository contains a Docker container for serving inference requests from HuggingFace models, with NGINX, Gunicorn, and Uvicorn for parallel request handling, and a Google Colab notebook for demonstrating parallel POST requests.

## Files
- `Dockerfile`: Builds the container using `tiangolo/uvicorn-gunicorn-fastapi:python3.11`.
- `requirements.txt`: Lists dependencies (`fastapi`, `transformers`, etc.).
- `app/main.py`: FastAPI app with `/predict` endpoint for sentiment analysis using DistilBERT.
- `nginx.conf`: NGINX configuration for proxying requests.
- `demo.ipynb`: Google Colab notebook for parallel POST requests.

## Model Choice
- Model: `distilbert-base-uncased-finetuned-sst-2-english`
- Reason: Lightweight (~260MB), fast for sentimental analysis.
- Larger models like bert-base-uncased (~440MB) or roberta-large (~1.3GB) were considered but rejected due to higher memory and latency requirements, which could strain the VM.

## Colab Notebook
Run the notebook: (https://colab.research.google.com/drive/14jCTBVR2ySq44y21LXSTG7f-uvDrs-PZ?usp=sharing)

## Setup Instructions
1. Build: `docker build -t hf-inference .`
2. Run: `docker run -d --name hf-app -v /tmp:/tmp hf-inference gunicorn -k uvicorn.workers.UvicornWorker -b uni>
3. Install NGINX: `sudo apt install nginx`
4. Configure NGINX: `sudo cp nginx.conf /etc/nginx/nginx.conf && sudo systemctl restart nginx`
5. Test(Locally): `curl -X POST "http://localhost/predict" -H "Content-Type: application/json" -d '{"text": "I >
6. Run `demo.ipynb` in Google Colab
