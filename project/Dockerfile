FROM python:3.10

WORKDIR /code/project

COPY ./requirements.txt /code/project/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/project/requirements.txt

COPY . /code/project