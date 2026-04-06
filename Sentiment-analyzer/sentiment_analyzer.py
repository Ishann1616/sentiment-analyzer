from textblob import TextBlob

class SentimentAnalyzer:
    def __init__(self):
        self.results=[]

    def analyze(self,text):
        blob= TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity> 0.1:
            sentiment="Positive ☺️"
        elif polarity < -0.1:
            sentiment="Negative 😳"
        else:
            sentiment="Neutral 😬"

        return {
            "text": text,
            "sentiment": sentiment,
            "score": round(polarity, 2)
        }