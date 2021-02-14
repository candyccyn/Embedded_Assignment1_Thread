import machine,utime
led = machine.Pin(15, machine.Pin.OUT)
touch_sensor = machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_DOWN)
ON = 1
OFF = 0
def toggle_led():
    led.value(ON)
    utime.sleep(1)
    led.value(OFF)
    utime.sleep(1)  
def Touch_handler(pin):
    print("touch detected")
    toggle_led()
touch_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=Touch_handler)
while True:
    pass
