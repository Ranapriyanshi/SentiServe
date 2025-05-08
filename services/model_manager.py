from transformers import AutoModelForSequenceClassification, AutoTokenizer
import os

MODEL_ID = "j-hartmann/emotion-english-distilroberta-base"
MODELS_DIR = os.path.join(os.path.abspath(__file__), '../..',"models")

class ModelManager:
    def __init__(self):
        self.tokenizer = None
        self.model = None

    def load_model(self):
        if self.model is None or self.tokenizer is None:
            print("Loading model and tokenizer...")
            self.tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, cache_dir=MODELS_DIR)
            self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID, cache_dir=MODELS_DIR)
            self.model.eval()  # Optional: switch to inference mode
        return self.tokenizer, self.model
