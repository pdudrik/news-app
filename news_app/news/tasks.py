import feedparser
from celery import shared_task
from .models import NewsSource



@shared_task
def fetch_new_rss_data():
    articles = []
    for source in NewsSource.objects.all():
        parsed_feed = feedparser.parse(source.rss_url)

        for article_raw in parsed_feed["entries"]:
            article_data = {
                "title": article_raw["title"],
                "link": article_raw["link"],
                "published": article_raw["published"],
                "source": source.rss_url
            }

            feed_entries = article_raw.keys()
            if "summary" in feed_entries:
                article_data["summary"] = article_raw["summary"]
            
            elif "description" in feed_entries:
                article_data["summary"] = article_raw["description"]
            
            else:
                article_data["summary"] = None
            
            articles.append(article_data)
    
    for article in articles:
        print(f"TITLE: {article['title']}")
    
    return "Task completed!"

