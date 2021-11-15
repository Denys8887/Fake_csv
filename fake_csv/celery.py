from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fake_csv.settings')
# BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://redis:6379/0')

app = Celery('fake_csv')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# app.conf.broker_url = BASE_REDIS_URL
