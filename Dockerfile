FROM jonatkinson/python-poetry:3.7

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ADD pyproject.toml . 

RUN poetry install

WORKDIR /app

ADD secure_url .


RUN poetry run python manage.py makemigrations
RUN poetry run python manage.py migrate

CMD poetry run python manage.py runserver 0.0.0.0:8000

EXPOSE 8000