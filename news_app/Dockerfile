FROM python:3.13.7-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]