from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.results=[]
        print("Loading AI model....")
        self.model=pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
        print("Model ready!")
    
    def analyze(self,text):
        if not text or len(text.strip())==0:
            return{
                "text": text,
                "sentiment": "Neutral 😐",
                "score": 0.0
            }
        
        try:
            result = self.model(text[:512])[0]
            label = result["label"]
            confidence = round(result["score"], 2)
            
            if label == "POSITIVE":
                sentiment = "Positive 😊"
            else:
                sentiment = "Negative 😞"
                
            return {
                "text": text,
                "sentiment": sentiment,
                "score": confidence
            }
            
        except Exception as e:
            return {
                "text": text,
                "sentiment": "Neutral 😐",
                "score": 0.0
            }