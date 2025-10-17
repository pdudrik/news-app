from django.urls import path
from . import views


app_name = "news"

urlpatterns = [
    path("", views.news_home_view, name="news-home"),
    path("update/", views.update, name="update"),
    path("schedule/", views.schedule_task, name="schedule"),
]