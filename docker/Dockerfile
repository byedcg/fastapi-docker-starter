FROM python:3.8-slim

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY ./requirements.txt $APP_HOME/requirements.txt

RUN pip install --no-cache-dir --upgrade -r $APP_HOME/requirements.txt

COPY ./app /code/app

# CMD uvicorn app.main:app --host 0.0.0.0 --port 80
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 app.main:app
