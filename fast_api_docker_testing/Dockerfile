FROM python:3.9

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app /src

CMD ["python", "/src/main.py"]