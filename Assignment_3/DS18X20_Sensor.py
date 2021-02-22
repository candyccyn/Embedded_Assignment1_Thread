import machine, onewire, ds18x20, time
led = machine.Pin(25, machine.Pin.OUT)
dsPin = machine.Pin(16)
dsSensor = ds18x20.DS18X20(onewire.OneWire(dsPin))
 
roms = dsSensor.scan()
print('Found a ds18x20 device')
data=0

while True:
  dsSensor.convert_temp()
  time.sleep_ms(500)
  for rom in roms:
    data =dsSensor.read_temp(rom)
    print("TEMPERATURE: ", data)
    if(data > 32.0):
        led.value(1)
    else:
        led.value(0)
  time.sleep(2)



