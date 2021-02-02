FROM python:3.9.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENTRYPOINT [ "python" ]
CMD ["-m", "server", "--host=0.0.0.0", "--port=5000"]
