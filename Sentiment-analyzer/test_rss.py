from rss_fetcher import RSSFetcher

rf = RSSFetcher()
articles = rf.fetch("trump")

for article in articles:
    print(article)