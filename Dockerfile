FROM balenalib/raspberry-pi2-python:build

RUN install_packages python3-pip
RUN sudo pip install Adafruit_DHT --install-option="--force-pi2"

COPY sensor.py sensor.py

CMD ["python", "sensor.py"]