# Celery Timed
Celery task which deploys a function at a specified time.

## Install Project
```bash
# Clone project
git clone https://github.com/djstein/celery-timed.git

# Enter working directory
cd celery-timed

# Create a Python 3 virtual environment
virtualenv -p python3 .env

# Activate virtual environment 
.env/bin/activate

# Install Python Environment Requirement s
pip install -Ur requirements.txt
```

## Redis Installation on MacOS
```bash
# Install redis
brew install redis
```

## Running Project
In three terminals have a celery working, redis server running, and activate a celery task

### Terminal 1: Celery App
```bash
source .env/bin/activate
celery -A celery_config beat
```
### Terminal 2: Redis Server
```bash
redis-server

# When finished, shut down the server
redis-cli shutdown
```

### Terminal 3: Celery Worker
```bash
source .env/bin/activate
celery -A celery_config worker -B
```

Notice in the worker terminal the success and output of the test function

Change the times the scheduled worker uses a function by changing the time variable in celery_config.

### Time currently shown to print the test function every 10 seconds
time = 10.0

### This can be changed to work at any cron time, for example, midnight:
time = crontab(hour=0, minute=0)