web: gunicorn fake_csv.wsgi
worker: celery -A fake_csv.celery worker -B --loglevel=info