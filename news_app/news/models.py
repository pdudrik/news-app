from django.db import models


class NewsSource(models.Model):
    name = models.CharField()
    rss_url = models.URLField(unique=True)
    active = models.BooleanField()

    def __str__(self):
        return self.name


class Article(models.Model):
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE)
    title = models.CharField()
    link = models.URLField(unique=True)
    published = models.DateTimeField()
    summary = models.TextField()

    def __str__(self):
        return self.title


class Digest(models.Model):
    name = models.CharField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DigestArticle(models.Model):
    digest = models.ForeignKey(Digest, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="digest_article")

    def __str__(self):
        return f"{self.digest}-{self.article}"
