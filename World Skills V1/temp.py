#!/usr/bin/env python3
import Adafruit_DHT
import time

sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22} #- словарь

humidity, temperature = Adafruit_DHT.read_retry(22, 4)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))  # Вывод данных
elif temperature > 20:
    print("Warning")