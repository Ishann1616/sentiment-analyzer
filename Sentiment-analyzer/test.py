from news_fetcher import NewsFetcher
from sentiment_analyzer import SentimentAnalyzer

nf = NewsFetcher("5c805add9ccc4c93816e65bda43de9d7")
sa = SentimentAnalyzer()

articles = nf.fetch("artificial intelligence")

for article in articles:
    result = sa.analyze(article["title"])
    print(f"{result['sentiment']} | {result['score']} | {article['title']}")