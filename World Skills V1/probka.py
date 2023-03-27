import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(0) 
GPIO.setup(20, GPIO.OUT) 
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

HourLightOn = 6
MinuteLightOn = 00 
HourLightOff = 22
MinuteLightOff = 00

HourPumpOn1 = 10
MinutePumpOn1 = 35
HourPumpOff1 = 10
MinutePumpOff1 =40

HourPumpOn2 = 12
MinutePumpOn2 = 30
HourPumpOff2 = 12
MinutePumpOff2 =35

HourPumpOn3 = 18
MinutePumpOn3= 30
HourPumpOff3 = 18
MinutePumpOff3 = 34


while 1:
    
    d = datetime.datetime.now()
    print(d)
    
    year = (d.year)
    month = (d.month)
    day = (d.day)
    hour = (d.hour)
    minute = (d.minute)
    second = (d.second)

    if hour >= HourLightOn and minute >= MinuteLightOn:
        GPIO.output(20, 0)
        GPIO.output(26, 0)
    elif hour >= HourLightOff and minute >= HourLightOff:
        GPIO.output(20, 1)
        GPIO.output(26, 1)
        
    if hour >= HourPumpOn1 and minute >= MinutePumpOn1 and minute < MinutePumpOff1:
        GPIO.output(21, 1)

    elif hour >= HourPumpOff1 and minute >= MinutePumpOff1:
        GPIO.output(21, 0)

        
    if hour >= HourPumpOn2 and minute >= MinutePumpOn2:
        GPIO.output(21, 0)

    elif hour >= HourPumpOff2 and minute >= MinutePumpOff2:
        GPIO.output(21, 1)

        
    if hour >= HourPumpOn3 and minute >= MinutePumpOn3:
        GPIO.output(21, 0)

    elif hour >= HourPumpOff3 and minute >= MinutePumpOff3:
        GPIO.output(21, 1)

    