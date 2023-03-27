import datetime
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, 0)

Hour1 = int(input("Hour_On: "))
Minute1 = int(input("Minute_On: "))
Hour2 = int(input("Hour_Off: "))
Minute2 = int(input("Minute_Off: "))

while 1:
    d = datetime.datetime.now()

    year = (d.year)
    month = (d.month)
    day = (d.day)
    hour = (d.hour)
    minute = (d.minute)
    second = (d.second)
    print(d)
    
    
    
    if hour >= Hour1 and minute >= Minute1:
        GPIO.output(26, 1)   
        print('ON')
    elif hour >= Hour2 and minute >= Minute2:
        GPIO.output(26, 0)
        print('OFF')
    

