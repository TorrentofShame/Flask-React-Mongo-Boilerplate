FROM python:3.9.0
LABEL maintainer="simon@torrentofshame.com"

RUN mkdir -p /home/backend/app/

WORKDIR /home/backend/app

COPY requirements.txt ./


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV LOGGING_LOCATION=/var/log/flask-base.log

ENTRYPOINT [ "python" ]
CMD ["-m", "server", "--host=0.0.0.0", "--port=5000"]
