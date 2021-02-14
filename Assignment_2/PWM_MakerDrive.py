import machine,time

M1A = machine.PWM(machine.Pin(2))
M1B = machine.PWM(machine.Pin(3))
M1A.freq(1000)
M1B.freq(1000)
while(1):
    for i in range(0,65536):
        M1A.duty_u16(i)  
    for i in range(0,65536):
        M1B.duty_u16(i)