FROM python:3.8-slim

ENV DOCKER_HOME=/home/app/webapp

RUN mkdir -p $DOCKER_HOME

WORKDIR $DOCKER_HOME

COPY requirements.txt $DOCKER_HOME

RUN pip install --no-cache-dir -r $DOCKER_HOME/requirements.txt

COPY . $DOCKER_HOME

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]