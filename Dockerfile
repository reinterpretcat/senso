FROM seblucas/alpine-python3:3.14

WORKDIR /app

RUN pip3 install influxdb-client

COPY src/main.py src/stats.py src/bme280.py ./

CMD [ "python3" , "main.py"]