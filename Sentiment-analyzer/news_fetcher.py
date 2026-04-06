import requests

class NewsFetcher:
    def __init__(self,api_key):
        self.api_key=api_key
        self.base_url = "https://newsapi.org/v2/everything"
    
    def fetch(self, topic ,count=20):
        params={
            "q": topic,
            "apiKey": self.api_key,
            "language": "en",
            "pageSize": count,
            "sortBy": "publishedAt"
        }
    
        response=requests.get(self.base_url, params=params)
        data =response.json()

        articles=[]
        for article in data.get("articles",[]):
            articles.append({
                "title":article["title"],
                "source": article["source"]["name"]
            })

        return articles