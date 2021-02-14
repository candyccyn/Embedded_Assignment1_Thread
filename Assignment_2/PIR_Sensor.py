import machine,utime
led = machine.Pin(15, machine.Pin.OUT)
PIR_sensor = machine.Pin(28,machine.Pin.IN,machine.Pin.PULL_DOWN)
buzzer = machine.Pin(14, machine.Pin.OUT)
ON = 1
OFF = 0
def toggle_led():
    led.value(ON)
    utime.sleep(1)
    led.value(OFF)
    utime.sleep(1)  
def PIR_handler(pin):
    print("motion detected")
    toggle_led()
    for i in range(50):
        buzzer.toggle()
        utime.sleep_ms(50) 
PIR_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=PIR_handler)
led.value(OFF)
while True:
    utime.sleep(5)
   
