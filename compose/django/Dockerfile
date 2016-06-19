FROM python:3.5
MAINTAINER Manu Phatak <bionikspoon@gmail.com>

ENV PYTHONUNBUFFERED 1

RUN groupadd -r django && useradd -r -g django django

COPY ./requirements /requirements
RUN pip install -r /requirements/production.txt

COPY . /app
RUN chown -R django /app

COPY ./compose/django/gunicorn.sh /gunicorn.sh
RUN chmod +x /gunicorn.sh && chown django /gunicorn.sh

COPY ./compose/django/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && chown django /entrypoint.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
