from django.contrib import admin
from .models import Article, NewsSource, Digest, DigestArticle


# Register your models here.
admin.site.register(Article)
admin.site.register(NewsSource)
admin.site.register(Digest)
admin.site.register(DigestArticle)