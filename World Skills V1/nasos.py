import RPi.GPIO as GPIO
import time
from tkinter import *
import datetime

GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, 0)




def clicked():
    GPIO.output(21, 0)

def click():
    GPIO.output(21, 1)

HourONt = input("Hour On: ")
MinuteONt = input("Minute On: ")
HourOFFt = input("Hour Off: ")
MinuteOFFt = input("Minute Off: ")
    
HourON = int(HourONt)
MinuteON = int(MinuteONt)
HourOFF = int(HourOFFt)
MinuteOFF = int(MinuteOFFt)

def clicks():
    while 1: 
                
        d = datetime.datetime.now()

        year = (d.year)
        month = (d.month)
        day = (d.day)
        hour = (d.hour)
        minute = (d.minute)
        second = (d.second)
        print(d)
                
        
        if hour >= HourON and minute >= MinuteON:
            GPIO.output(21, 1)   
            print('ON')
        elif hour >= HourOFF and minute >= MinuteON:
            GPIO.output(21, 0)
            print('OFF')
    





window = Tk()

window.geometry('300x200')

btn1 = Button(window, text='start', fg='red', bg='black', command=clicked)
btn1.grid(column=0, row=0)

btn2 = Button(window, text='time', fg='red', bg='black',command=clicks)
btn2.grid(column=1, row=0)

btn3 = Button(window, text='stop', fg='red', bg='black',command=click)
btn3.grid(column=2, row=0)





