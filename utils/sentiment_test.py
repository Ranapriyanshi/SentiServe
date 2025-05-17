from fastapi import APIRouter
from services import ModelManager
from pydantic import BaseModel
import torch
from transformers import pipeline

sentiment_router = APIRouter()
model_manager = ModelManager()
class SentimentRequest(BaseModel):
    text: str
    model: str

@sentiment_router.post("/sentiment")
def get_sentiment(request: SentimentRequest):
    print(f"🔍 Requested model: {request.model}", flush=True)
    print(f"📝 Text: {request.text}", flush=True)

    try:
        tokenizer, model = model_manager.load_model(request.model)
        classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
        result = classifier(request.text)
        return {"text": request.text, "model": request.model, "sentiment": result}
    except Exception as e:
        print("❌ Error:", str(e), flush=True)
        return {"error": str(e)}


# classifier = pipeline("zero-shot-classification")

# # NEWS CATEGORIZATION OF ZEROSHOT CLASSIFICATION
# sentences = [
#     "India Beat Germany in a game of hockey by 3 goals",
#     "It started pouring heavy rain in multiple cities of haryana including Amabal, Rohtak, Sonipat.",
#     "Tension on Pak-india border is continuosly growing and things are getting bad after pak voilated ceasefire.",
# ]
# labels = ["Sports", "GeoPolitical", "Weather", "Politics", "Economy"]
# for sentence in sentences:
#     result = classifier(sentence, candidate_labels=labels)
#     print(result)
