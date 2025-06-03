FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy application code
COPY ./app /app

# Set environment variables for model and Gunicorn configuration
ENV MODEL_NAME=distilbert-base-uncased-finetuned-sst-2-english
ENV GUNICORN_WORKERS=4
ENV GUNICORN_TIMEOUT=120

# Expose port (Gunicorn/Uvicorn uses a UNIX socket for NGINX)
EXPOSE 8000
