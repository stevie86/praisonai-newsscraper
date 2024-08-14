import feedparser
from agent import Agent

class RSSScraperAgent(Agent):
    def __init__(self, feed_urls):
        super().__init__()
        self.feed_urls = feed_urls

    def run(self, data=None):
        articles = []
        for url in self.feed_urls:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                articles.append({
                    'title': entry.title,
                    'link': entry.link,
                    'summary': entry.summary,
                    'published': entry.published
                })
        return articles
