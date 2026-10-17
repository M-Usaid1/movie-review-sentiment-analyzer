
from pathlib import Path

import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Find the saved model relative to this Python file.
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "distilbert_model"

# Use GPU if available; otherwise, use CPU.
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the tokenizer and trained model once when the API starts.
if not MODEL_DIR.is_dir():
    raise FileNotFoundError(
        f"Model folder not found: {MODEL_DIR}"
    )

tokenizer = AutoTokenizer.from_pretrained(str(MODEL_DIR))
model = AutoModelForSequenceClassification.from_pretrained(str(MODEL_DIR))
model.to(DEVICE)
model.eval()

app = FastAPI(
    title="DistilBERT Sentiment Analysis API",
    description="Predicts whether a movie review is positive or negative.",
    version="1.0.0",
)


class ReviewRequest(BaseModel):
    review: str = Field(min_length=1, max_length=10000)


@app.get("/")
def home():
    return {
        "message": "DistilBERT Sentiment Analysis API is running!",
        "device": str(DEVICE),
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": "DistilBERT",
        "device": str(DEVICE),
    }


@app.post("/predict")
def predict_sentiment(request: ReviewRequest):
    review = request.review.strip()

    if not review:
        raise HTTPException(
            status_code=400,
            detail="Please provide a non-empty review.",
        )

    inputs = tokenizer(
        review,
        return_tensors="pt",
        truncation=True,
        max_length=256,
    )

    inputs = {key: value.to(DEVICE) for key, value in inputs.items()}

    with torch.inference_mode():
        outputs = model(**inputs)
        probabilities = torch.softmax(outputs.logits, dim=1)[0]

    predicted_class = int(torch.argmax(probabilities).item())

    # Your training labels: 0 = negative, 1 = positive.
    sentiment = "Positive" if predicted_class == 1 else "Negative"

    return {
        "review": review,
        "sentiment": sentiment,
        "confidence": round(float(probabilities[predicted_class].item()), 4),
        "positive_probability": round(float(probabilities[1].item()), 4),
        "negative_probability": round(float(probabilities[0].item()), 4),
    }
