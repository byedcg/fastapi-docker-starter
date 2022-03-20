FROM python:3.8-slim

ENV PYTHONUNBUFFERED True

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app 

# one process per container paradigm. Handling replication at the cluster level.
CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT

# manage the worker processes and distributes on the cpu: requires gunicorn
# CMD exec gunicorn --bind :80 --workers 1 --worker-class uvicorn.workers.UvicornWorker --threads 8 app.main:app
