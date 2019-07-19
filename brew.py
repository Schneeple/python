import temp
import RPi.GPIO as GPIO
from time import sleep
pin_ = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(pin_ , GPIO.OUT) 

x = temp.tempRead()


#print('Temperature is: '+ str(T[1]) + ' F.')

while True:
    T = x.read_temp()
    if T[1] > 100:
        GPIO.output(pin_ , True)
        
    else:
        GPIO.output(pin_ , False)
    print('Temperature is: '+ str(T[1]) + ' F.')
    sleep(1)


