import requests
import xml.etree.ElementTree as ET

class RSSFetcher:
    def __init__(self):
        self.sources={
            "BBC": "https://feeds.bbci.co.uk/news/rss.xml",
            "NPR": "https://feeds.npr.org/1001/rss.xml",
            "Times of India": "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
            "NDTV": "https://feeds.feedburner.com/ndtvnews-top-stories",
            "The Hindu": "https://www.thehindu.com/news/feeder/default.rss"
        }

    def fetch(self,topic ,count=10):
        all_articles=[]

        for source_name, url in self.sources.items():
            try:

                headers = {"User-Agent": "SentiScope/1.0"}
                response = requests.get(url, timeout=5, headers=headers)
                root = ET.fromstring(response.content)
                
                for item in root.iter("item"):
                    title = item.find("title")
                    if title is not None and topic.lower() in title.text.lower():
                        all_articles.append({
                            "title": title.text,
                            "source": source_name
                        })
                        if len(all_articles) >= count:
                            break
                            
            except Exception as e:
                print(f"Error fetching {source_name}: {e}")
                continue
        
        return all_articles