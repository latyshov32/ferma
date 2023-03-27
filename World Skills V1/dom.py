import RPi.GPIO as GPIO
import datetime
from tkinter import *

GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.output(20, 1)
GPIO.output(21, 1)
GPIO.output(26, 1)

def clickO():
    GPIO.output(21, 0)
    
def clickF():
    GPIO.output(21, 1)
    
def clickA():
    while 1:
        
        d = datetime.datetime.now()
        day = d.day
        hour = d.hour
        minn = d.minute
        
        if day == 1:
            if hour == 2 or hour == 3 and minn == 0:
                GPIO.output(21, 0)
              
        if day == 1:
            if hour == 2 or hour == 3 and minn == 5:
                GPIO.output(21, 0) 

        if day == 1:
            if hour == 6 and minn == 0:
                GPIO.output(26, 0)
                GPIO.output(20, 0) 
              
        if day == 1:
            if hour == 24 and minn == 0:
                GPIO.output(26, 1)
                GPIO.output(20, 1) 
        
if GPIO.input(27) == 1 and GPIO.input(22) == 1:
    print ("vysoko")
elif GPIO.input(27) == 0 and GPIO.input(22) == 1:
    print ("srednya")
elif GPIO.input(27) == 0 and GPIO.input(22) == 0:
    print ("k_n_")
    GPIO.output(21, 1)
            
win = Tk()
win.title("денис и леша")
win.geometry("200x200")

btn1 = Button(win, text = 'start' , bg = 'red', fg = 'green', command = clickO)
btn1.grid(column = 0, row = 0)

btn1 = Button(win, text = 'auto' , bg = 'red', fg = 'green', command = clickA)
btn1.grid(column = 1, row = 0)

btn1 = Button(win, text = 'stop' , bg = 'red', fg = 'green', command = clickF)
btn1.grid(column = 2, row = 0)
            
        
