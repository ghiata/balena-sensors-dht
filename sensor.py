#!/usr/bin/python

import Adafruit_DHT

sensor = Adafruit_DHT.DHT22

pin = 17

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print(temperature, humidity)
else:
    print('Failed to get reading. Try again!')