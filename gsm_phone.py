import serial,time

def call_number(phnum):
    ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
    ser.flush()
    print "Calling ...",phnum
    ser.write('ATD',phnum,';\r')
    time.sleep(10)
    ser.write('ATH\r')
    ser.close()

call_number("9666261963")
