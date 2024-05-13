FROM python:3.12-alpine

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["/usr/bin/env", "python3", "app/app.py"]
