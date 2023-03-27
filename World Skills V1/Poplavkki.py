import RPi.GPIO as GPIO #- импорт библиотеки и краткое название
import  time #- импорт библиотеки

GPIO.setmode(GPIO.BCM) #- используемая нумерация пинов
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) # устанавливаем значение пина как ВХОД или ВЫХОД
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) # устанавливаем значение пина как ВХОД или ВЫХОД

while 1:
    if GPIO.input(27) == 1 and GPIO.input(22) == 1:
        print("HIGHT")
    elif GPIO.input(27) == 0 and GPIO.input(22) == 1:
        print("MID")
    elif GPIO.input(27) == 0 and GPIO.input(22) == 0:
        print("LOW")
    time.sleep(4)
    

