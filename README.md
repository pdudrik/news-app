# News App
MVP version of simple Django RSS news aggregator.

## Setup docker
Build docker container:
```docker compose up -d --build```

Check if services are running:
```docker ps```
Four services need to be running: ```news-app-django```, ```news-app-celery```, ```news-app-celery_beat```, ```redis:7.0.11-alpine```

Check for all (also offline):
```docker ps -a```

Check for logs of Django Celery for number of added feeds:
```docker logs --since=1h <container ID>```

## Web application
Control panel via ```/admin/``` route (```localhost:8001:/admin/``` or ```127.0.0.1:8001:/admin/```).
Celery task runs every 60 seconds in backgrounds and triggers task (function) ```fetch_new_rss_data``` (```news-app/news_app/news/tasks.py```).
It can be also manully triggered by loading web route ```/news/update``` (```localhost:8001:/news/update``` or ```127.0.0.1:8001:/news/update```).

## Debug
If Celery beat does not triggers as it should (every 60 seconds), then load route ```/news/schedule``` to trigger clock. If still does not work, then clean databse (via ```/admin``` route), at least everything from section ```Periodic tasks``` except ```CRONTAB```. After that load ```/news/schedule``` route.