from celery import Celery
from celery.schedules import crontab

app = Celery(
    'celery_config',
    broker='redis://localhost:6379',
    include=['tasks']
)

app.conf.timezone = 'UTC'

# Time currently shown to print the test function every 10 seconds
time = 10.0

# This can be changed to work at any cron time, for example, midnight:
# time = crontab(hour=0, minute=0)

app.conf.beat_schedule = {
    'function-at-time': {
        'task': 'tasks.test_function',
        'schedule': time,
        'args': [str(time)],
    },
}


if __name__ == '__main__':
    app.start()
