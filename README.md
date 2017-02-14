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

## Redis Installation on Mac OS X
```bash
# Install redis
brew install redis
```

## Running Project
In three terminals have a celery working, redis server running, and activate a celery task

### Terminal 1: Celery Worker
```bash
source .env/bin/activate
celery -A celery_config worker --loglevel=info
```
### Terminal 2: Redis Server
```bash
redis-server
```

### Terminal 3: Celery Task
```bash
source .env/bin/activate
python
>>>from tasks import add
>>>add.delay(1,4)
```

Notice in the worker terminal the success and output of the add function