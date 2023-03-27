import RPi.GPIO as GPIO
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, 1)



while 1:    
    d = datetime.datetime.now()
    x = d.hour 
    y = d.minute
    print (d)

    if x == 9 or x == 11 or x == 13 or x == 8  and y == 13:
        GPIO.output(21, 0)
        
    elif x == 9 or x == 11 or x == 13 or x == 8 and y == 14: 
        GPIO.output(21, 1)







