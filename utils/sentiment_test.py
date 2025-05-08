from fastapi import APIRouter
from services import ModelManager
from pydantic import BaseModel
import torch

tokenizer, model = ModelManager().load_model()
sentiment_router = APIRouter()

class SentimentRequest(BaseModel):
    text: str

@sentiment_router.post("/sentiment")
def get_sentiment(input: SentimentRequest):
    """
    Dummy sentiment analysis function.
    In a real-world scenario, this would call a sentiment analysis model.
    """
    inputs = tokenizer(input.text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=1).item()
    # indentifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", return_all_scores=True)
    # result = indentifier(text)
    return {"text": input.text, "sentiment": predictions}