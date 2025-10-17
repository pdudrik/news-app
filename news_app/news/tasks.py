import feedparser
from django.db import IntegrityError, transaction
from celery import shared_task
from .models import NewsSource, Article
from .utils import parse_entry_datetime


@shared_task
def fetch_new_rss_data():
    new_articles = 0
    sources = NewsSource.objects.all()
    for source in sources:
        parsed_feed = feedparser.parse(source.rss_url)

        for article_raw in parsed_feed["entries"]:
            article = Article()
            article.title = article_raw["title"]
            article.link = article_raw["link"]
            article.source = source

            parsed_dt = parse_entry_datetime(article_raw["published"])
            if parsed_dt is None:
                continue
            
            article.published = parsed_dt

            feed_entries = article_raw.keys()
            if "summary" in feed_entries:
                article.summary = article_raw["summary"]
            
            elif "description" in feed_entries:
                article.summary = article_raw["description"]
            
            else:
                article.summary = ""
            
            try:
                with transaction.atomic():
                    article.save(force_insert=True)
                    new_articles += 1
            
            except IntegrityError:
                pass

    
    return f"Task completed! Added new articles: {new_articles}"

