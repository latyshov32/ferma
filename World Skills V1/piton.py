import RPi.GPIO as GPIO
import time
from tkinter import *
import datetime
from gpiozero import LightSensor
import Adafruit_DHT
import time
import serial              
import time
import subprocess
import traceback
import getrpimodel
import struct
import platform
import argparse
import sys
import json
import os.path


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while 1:
    
    name_file = 'serial0'
    filepath = os.path.join('/dev', name_file)
    os.popen('sudo chmod 777 ' + filepath)

    class GPIO_Edge_Timeout(Exception):
      pass

    if os.path.exists('/dev/serial0'):
      partial_serial_dev = 'serial0'


    serial_dev = '/dev/%s' % partial_serial_dev

    p_ver = platform.python_version_tuple()[0]

    def start_getty():
      start_getty = ['sudo', 'systemctl', 'start', 'serial-getty@%s.service' % partial_serial_dev]
      p = subprocess.call(start_getty)

    def stop_getty():
      stop_getty = ['sudo', 'systemctl', 'stop', 'serial-getty@%s.service' % partial_serial_dev]
      p = subprocess.call(stop_getty)


    def connect_serial():
      return serial.Serial(serial_dev,
                            baudrate=9600,
                            bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            timeout=1.0)

    def mh_z19():
      try:
        ser = connect_serial()
        while 1:
            result=ser.write(b"\xff\x01\x86\x00\x00\x00\x00\x00\x79")
            s=ser.read(9)
          
            return {'co2': s[2]*256 + s[3]}
            break
      except:
         traceback.print_exc()

    def read(serial_console_untouched=False):
      if not serial_console_untouched:
        stop_getty()

      result = mh_z19()

      if not serial_console_untouched:
        start_getty()
      if result is not None:
        return result

    if __name__ == '__main__':

      parser = argparse.ArgumentParser (description='''return CO2 concentration as object as {'co2': 416}''')

      parser.add_argument("--serial_console_untouched")

      args = parser.parse_args()

      value = read(args.serial_console_untouched)
      print (json.dumps(value))
      
    sensor_args = { '11': Adafruit_DHT.DHT11,
                    '22': Adafruit_DHT.DHT22} 

    humidity, temperature = Adafruit_DHT.read_retry(22, 4)

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))  
    else:
        print('Failed to get reading. Try again!')
        
        
    
    if GPIO.input(27) == 1 and GPIO.input(22) == 1:
        print("HIGHT")
    elif GPIO.input(27) == 0 and GPIO.input(22) == 1:
        print("MID")
    elif GPIO.input(27) == 0 and GPIO.input(22) == 0:
        print("LOW")
        



    
