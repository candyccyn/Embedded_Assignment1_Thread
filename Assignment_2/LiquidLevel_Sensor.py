import machine,utime
buzz = machine.Pin(14, machine.Pin.OUT)
liquid_level_sensor = machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_DOWN)

def Level_handler(pin):
    print("Water exceeded the limit")
    for i in range(50):
        buzz.toggle()
        utime.sleep_ms(30)
liquid_level_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=Level_handler)
while True:
    pass
   
