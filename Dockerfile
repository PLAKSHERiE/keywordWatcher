FROM python:3.10

WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src .
COPY .env .

CMD ["python", "main.py"]