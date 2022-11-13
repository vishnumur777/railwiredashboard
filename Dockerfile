FROM python:3.10-slim

EXPOSE 8501

COPY . /app

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential software-properties-common git && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

ENTRYPOINT ["./runner.sh","--server.port=8501","--server.address=0.0.0.0"]

CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT ./runner.sh:app

