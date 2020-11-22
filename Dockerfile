# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8 AS build

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install poetry
ENV POETRY_VERSION=1.1.0
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /app

ADD poetry.lock .
ADD pyproject.toml .

# Install project dependencies
RUN poetry install --no-dev

RUN poetry export -E server --without-hashes -f requirements.txt -o /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt \
    && rm -rf /requirements.txt


ADD secure_url .

CMD gunicorn secure_url.wsgi --bind :8000 --chdir=/app

EXPOSE 8000

# FROM build AS testing

# RUN poetry install

# RUN poetry run pytest

FROM build
