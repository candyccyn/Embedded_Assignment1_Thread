from machine import Pin
import utime
trigger = Pin(15, Pin.OUT)
echo = Pin(14, Pin.IN,Pin.PULL_DOWN)
speedOfSound = 0.0343 #0.0343 cm/microsecond
ledOnBoard = Pin(25, Pin.OUT)
def turnOn_LED(distance):
    if(distance < 0.8):
        for i in range(2):
            ledOnBoard.value(1)
            utime.sleep(0.04)
            ledOnBoard.value(0)
            utime.sleep(0.04)
    else:
        ledOnBoard.value(0)        
def func_ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(6)
   trigger.low()
   while echo.value() == 0:
       signalOff = utime.ticks_us()
   while echo.value() == 1:
       signalOn = utime.ticks_us()
   timePassed = signalOn - signalOff
   distance = (timePassed *speedOfSound ) / 2
   return distance

while True:
   distance = func_ultra()
   print("The distance from object is ",distance,"cm")
   turnOn_LED(func_ultra())
   utime.sleep(1)
