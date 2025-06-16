FROM python:3.10-slim

WORKDIR /app

COPY . /app

CMD ["python3", "app.py"]
