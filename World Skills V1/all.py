import RPi.GPIO as GPIO
import Adafruit_DHT
import datetime
from tkinter import *

GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, 1)
GPIO.output(20, 1)
GPIO.output(26, 1)

if GPIO.input(27) == 1 or GPIO.input(22) == 1:
    print("высокий")
elif GPIO.input(27) == 0 or GPIO.input(22) == 1:
    print("средний")
elif GPIO.input(27) == 0 or GPIO.input(22) == 0:
    print("низкий")

def ckl():
    GPIO.output(26, 0)

def ckl1():
    GPIO.output(20, 0)
    
def ckl2():
    GPIO.output(21, 0)
    
def ackl():
    GPIO.output(26, 1)

def ackl1():
    GPIO.output(20, 1)
    
def ackl2():
    GPIO.output(21, 1)

def cklickA():

    while 1:
            
        d = datetime.datetime.now()
            
        day = d.day
        hour = d.hour
        minut = d.minute
            
        if day == 14:
            if hour == 13 and minut == 42:
                GPIO.output(21, 1)
            elif hour == 15 and minut == 0:
                GPIO.output(21, 0)
        
        elif day == 5:
            if hour == 6 and minut == 0:
                GPIO.output(21, 1)
            elif hour == 6 and minut == 4:
                GPIO.output(21, 1)
                
        if day == 25:
            if hour == 0 and minut == 0:
                GPIO.output(26, 0)
                GPIO.output(20, 0)
            elif hour == 18 and minut == 0:
                GPIO.output(26, 1)
                GPIO.output(20, 1)
                
        
        
                      
window =Tk()
window.geometry ("300x100")

btn1 = Button(window, text = "start", bg ="red", fg = "black", command =ckl2) 
btn1.grid(column = 1, row = 1)             

btn2 = Button(window, text = "stop", bg ="red", fg = "black", command =ackl2) 
btn2.grid(column = 2, row = 1)
    
btn3 = Button(window, text = "time", bg ="red", fg = "black", command =cklickA) 
btn3.grid(column = 3, row = 1)

btn4 = Button(window, text = "svet_ON", bg ="red", fg = "black", command =ckl) 
btn4.grid(column = 1, row = 2)

btn5 = Button(window, text = "svet_OFF", bg ="red", fg = "black", command =ackl) 
btn5.grid(column = 2, row = 2)

btn6 = Button(window, text = "2svet_ON", bg ="red", fg = "black", command =ckl1) 
btn6.grid(column = 1, row = 3)

btn7 = Button(window, text = "2svet_OFF", bg ="red", fg = "black", command =ackl1) 
btn7.grid(column = 2, row = 3)
                    
window.mainloop