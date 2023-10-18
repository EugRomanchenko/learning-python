# For build and run execute command:
# docker build -t app .
# docker run -p 127.0.0.1:8080:8000 -it app
FROM python:3.11.6-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install "poetry==1.6.1" && \
    poetry config virtualenvs.create false --local

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
