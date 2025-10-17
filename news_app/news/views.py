import json
from django.shortcuts import render
from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from .models import Article, DigestArticle, Digest
from .tasks import fetch_new_rss_data


# Create your views here.
def news_home_view(request):
    articles_data = Article.objects.all().order_by("-published")
    articles = []
    for article_data in articles_data:
        article = {
            "title": article_data.title,
            "source_name": article_data.source.name,
            "published": article_data.published,
            "link": article_data.link,
            "summary": article_data.summary
        }
        print(f"Article: {article['title']}")
        digestarticle = article_data.digest_article.first()

        if digestarticle is None:
            print("Digest not set")
            article["digest"] = None
            
        
        else:
            digest = digestarticle.digest
            print(f"Digest: {digest.name}")
            article["digest"] = digest.name
        
        print()
        articles.append(article)
    
    print(articles)

    return render(request, "news/home.html", { "articles": articles })
    # return HttpResponse("Testing response")


def update(request):
    fetch_new_rss_data.delay()
    return HttpResponse("Task started!")


def schedule_task(request):
    interval, _ = IntervalSchedule.objects.get_or_create(
        every=60,
        period=IntervalSchedule.SECONDS,
    )

    PeriodicTask.objects.create(
        interval=interval,
        name="my-schedule",
        task="news.tasks.fetch_new_rss_data",
        # args=json.dumps([1, 3]),
        # one_off=True
    )

    return HttpResponse("Task scheduled!")
