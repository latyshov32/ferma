from gpiozero import LightSensor
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
sensor = LightSensor(17)

while 1:
    sensor.wait_for_light()
wait_for_light()
    GPIO.output(17,1)
    GPIO.output(26,1)
    print("It's light!")
    sensor.wait_for_dark()
    GPIO.output(17,0)
    GPIO.output(26,0)
    print("It's dark")