from celery_config import app
from celery.schedules import crontab


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         test.s(' Mondays!'),
#     )

@app.task
def test_function(arg):
    return print('Printing: '  + arg)
