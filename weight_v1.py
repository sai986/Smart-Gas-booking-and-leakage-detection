import serial
def weight_read():
    ser=serial.Serial('/dev/ttyAMA0',9600,timeout=1)    
    ser.flush()
    num=ser.inWaiting()
    if(num != 0):
      s=ser.read(num)
      print s
    ser.close()




while True :
   try:
     weight_read()
   except:
    print "error"
 
      


