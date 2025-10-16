import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_app.settings')    # copied from manage.py
app = Celery("news_app")
app.config_from_object("django.conf:settings", namespace="CELERY")


@app.task
def add_numbers():
    return


app.autodiscover_tasks()