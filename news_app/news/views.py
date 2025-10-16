from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, DigestArticle, Digest


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
