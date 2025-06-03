from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import os

app = FastAPI()

# Load model and tokenizer
model_name = os.getenv("MODEL_NAME", "distilbert-base-uncased-finetuned-sst-2-english")
try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load model: {str(e)}")

class TextInput(BaseModel):
    text: str

@app.post("/predict")
async def predict(input: TextInput):
    try:
        # Tokenize input
        inputs = tokenizer(input.text, return_tensors="pt", truncation=True, padding=True, max_length=512)
        # Perform inference
        with torch.no_grad():
            outputs = model(**inputs)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=1).item()
        label = "positive" if prediction == 1 else "negative"
        return {"text": input.text, "sentiment": label}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference failed: {str(e)}")

@app.get("/health")
async def health():
    return {"status": "healthy"}