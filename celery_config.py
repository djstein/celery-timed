from celery import Celery

app = Celery(
    'celery_config',
    broker='redis://localhost:6379',
    include=['tasks']
)

if __name__ == '__main__':
    app.start()
