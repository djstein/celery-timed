from celery_config import app
from celery.schedules import crontab


@app.task
def test_function(arg):
    return print('Printing: '  + arg)
