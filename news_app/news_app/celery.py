import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_app.settings')    # copied from manage.py
app = Celery("news_app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.timezone = "Europe/Bratislava"
app.conf.enable_utc = True
app.autodiscover_tasks()