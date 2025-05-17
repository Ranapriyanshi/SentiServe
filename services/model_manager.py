from transformers import AutoModelForSequenceClassification, AutoTokenizer
import os

MODEL_MAP = {
    "distilbert": "distilbert-base-uncased-finetuned-sst-2-english",
    "bert": "bert-base-uncased",
    "finbert": "ProsusAI/finbert"
}
# MODEL_ID = "j-hartmann/emotion-english-distilroberta-base"
# MODELS_DIR = os.path.join(os.path.abspath(__file__), '../..',"models")
c
class ModelManager:
    def __init__(self):
        self.models = {}

    def load_model(self, model_key=str):
        if model_key not in MODEL_MAP:
            raise ValueError(f"Model {model_key} not found in MODEL_MAP.")

        if model_key not in self.models:
            print("Loading model :{model_key}...", flush=True)
            tokenizer = AutoTokenizer.from_pretrained(MODEL_MAP[model_key])
            model = AutoModelForSequenceClassification.from_pretrained(MODEL_MAP[model_key])
            self.models[model_key] = (tokenizer, model)

        return self.models[model_key]
