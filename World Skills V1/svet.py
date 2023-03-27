from gpiozero import LightSensor #- импорт модуля из библиотеки
import RPi.GPIO as GPIO #- импорт библиотеки и краткое название

GPIO.setmode(GPIO.BCM) #- используемая нумерация пинов
GPIO.setwarnings(False) #- показ ошибок
GPIO.setup(20, GPIO.OUT) #- вход или выход
GPIO.setup(26, GPIO.OUT) #- вход или выход


sensor = LightSensor(17) #- переименование модуля + пин с которым работаем

while 1:
    sensor.wait_for_light() # обращенеи к Модулю lightSensor и к его функции wait_for_light()
    GPIO.output(20, 0) # устанавливаем значение для пина 17 (есть сигнал или нет сигнала) в нашем случае сигнал есть
    GPIO.output(26, 0) # устанавливаем значение для пина 26 (есть сигнал или нет сигнала) в нашем случае сигнал есть
    print("It's light! :)") # вывести на экран то, что в скобках
    sensor.wait_for_dark() # Все аналогично
    GPIO.output(20, 1)
    GPIO.output(26, 1)
    print("It's dark :(")
    


