import RPi.GPIO as GPIO
import datetime
from tkinter import *
from tkinter import messagebox

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.output(21, 1)

while 1:
        
    d=datetime.datetime.now()
    z = d.day
    x = d.hour 
    y = d.minute
    print(d)
       
    if z == 25:     
        if x == 9 and y == 40:
            GPIO.output (20, 0)
                
        elif x == 9 and y == 41:
            GPIO.output (20, 1)
        
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
            
    if z == 25:     
        if x == 8 and y == 0:
            GPIO.output (26, 1)
                
        elif x == 22 and y == 0:
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
                       
    if z == 25 or z == 9 or z == 23:      
            
        if x == 6 or x == 10 or x == 14 or x == 18 or x == 22 or x == 2 and y == 0:
            GPIO.output (21, 0)
                
        elif x == 6 or x == 10 or x == 14 or x == 18 or x == 22 and y == 4:
            GPIO.output (21, 1)
        
    if z == 2 or z == 16:
            
        if x == 1 or x == 5 or x == 9 or x == 13 or x == 17 or x == 21 and y == 0:
            GPIO.output (21, 0)
                
        elif x == 1 or x == 5 or x == 9 or x == 13 or x == 17 or x == 21 and y == 3:
            GPIO.output (21, 1)
                