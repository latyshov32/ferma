import RPi.GPIO as GPIO
import datetime
from tkinter import *
from tkinter import messagebox
import Adafruit_DHT
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
GPIO.setwarnings(0)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) # устанавливаем значение пина как ВХОД или ВЫХОД
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(21, 1)

def clickl1():
    GPIO.output (20, 1)

def clickedl1():
    GPIO.output (20, 0)

def clicktl1():

     while 1:
        d=datetime.datetime.now()
        z = d.day
        x = d.hour
        y = d.minute
        print(d)


        if z == 25:
            if x == 8 and y == 0:
                GPIO.output (20, 1)

            elif x == 22 and y == 0:
                GPIO.output (20, 0)

        elif z == 9:
            if x == 8 and y == 0:
                GPIO.output (20, 1)

            elif x == 20 and y == 0:
                GPIO.output (20, 0)

        elif z == 16:
            if x == 8 and y == 0:
                GPIO.output (20, 1)

            elif x == 18 and y == 0:
                GPIO.output (20, 0)


def clickl2():
    GPIO.output (26, 1)

def clickedl2():
    GPIO.output (26, 0)

def clicktl2():

    while 1:

        d=datetime.datetime.now()
        z = d.day
        x = d.hour
        y = d.minute
        print(d)

        if z == 25:
            if x == 8 and y == 0:
                GPIO.output (26, 1)

            elif x == 8 and y == 52:
                GPIO.output (26, 0)

        elif z == 9:
            if x == 8 and y == 0:
                GPIO.output (26, 1)

            elif x == 20 and y == 0:
                GPIO.output (26, 0)

        elif z == 16:
            if x == 8 and y == 0:
                GPIO.output (26, 1)

            elif x == 18 and y == 0:
                GPIO.output (26, 0)


def click():
    GPIO.output (21, 1)


def clicked():
    GPIO.output (21, 0)

def clickt():
    while 1:

        d=datetime.datetime.now()
        z = d.day
        x = d.hour
        y = d.minute
        print(d)

        if z == 25 or z == 9 or z == 23:

            if x == 12 or x == 38 or x == 14 or x == 18 or x == 22 or x == 2 and y == 20:
                GPIO.output (21, 0)

            elif x == 10 or x == 39 or x == 14 or x == 18 or x == 22 and y == 4:
                GPIO.output (21, 1)

        if z == 2 or z == 16:

            if x == 12 or x == 5 or x == 9 or x == 13 or x == 17 or x == 21 and y == 21:
                GPIO.output (21, 0)

            elif x == 1 or x == 5 or x == 9 or x == 13 or x == 17 or x == 21 and y == 3:
                GPIO.output (21, 1)



window = Tk()
window.title('bla-bla-bla')

window.geometry('800x600')

btn1 = Button(window, text='start', fg='red', bg='black', command=clicked)
btn1.grid(column=0, row=0)

btn2 = Button(window, text='time', fg='red', bg='black',command=clickt)
btn2.grid(column=1, row=0)

btn3 = Button(window, text='stop', fg='red', bg='black',command=click)
btn3.grid(column=2, row=0)

btn4 = Button(window, text='start_light', fg='red', bg='black', command=clickedl1)
btn4.grid(column=0, row=1)

btn5 = Button(window, text='auto', fg='red', bg='black',command=clicktl1)
btn5.grid(column=1, row=1)

btn6 = Button(window, text='stop_light', fg='red', bg='black',command=clickl1)
btn6.grid(column=2, row=1)


btn7 = Button(window, text='start_light2', fg='red', bg='black', command=clickedl2)
btn7.grid(column=0, row=2)

btn8 = Button(window, text='auto2', fg='red', bg='black',command=clicktl2)
btn8.grid(column=1, row=2)

btn9 = Button(window, text='stop_light2', fg='red', bg='black',command=clickl2)
btn9.grid(column=2, row=2)

btn10 = Button(window, text="exit", command=window.destroy).grid(column=1, row=3)

sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22} #- словарь

humidity, temperature = Adafruit_DHT.read_retry(22, 4)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))  # Вывод данных
else:
    print('Failed to get reading. Try again!')

if GPIO.input(27) == 1 and GPIO.input(22) == 1:
    print("HIGHT")
    b = 'Hight'
elif GPIO.input(27) == 0 and GPIO.input(22) == 1:
    print("MID")
    b = 'Mid'
elif GPIO.input(27) == 0 and GPIO.input(22) == 0:
    print("LOW")
    b = 'low'

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

        global m
        m = {'co2': s[2]*256 + s[3]}

        return m
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



lab = Label(window, text = 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity), font=("arial italic", 14) )
lab.grid(column = 3, row = 5)

labt = Label(window, text = b, font=("arial italic", 14) )
labt.grid(column = 3, row = 6)

labc = Label(window, text = m, font=("arial italic", 14) )
labc.grid(column = 3, row = 7)

labc = Label(window, text = d, font=("arial italic", 14) )
labc.grid(column = 3, row = 8)

window.update()

window.mainloop()

