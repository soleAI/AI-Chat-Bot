FROM python:3.11-slim-buster
RUN python3.11 -m pip install --upgrade pip
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
RUN pip install --upgrade numpy

CMD  ["python", "main.py"]