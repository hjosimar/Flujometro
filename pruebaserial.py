import serial
from datetime import datetime
ser=serial.Serial('COM5')
a=10
b=0
filename="data1.txt"
file= open(filename,"w")
while a>b:
    file.write("{},Data".format(datetime.now().strftime('%Y/%m/%d,%H:%M:%S')))
    for i in range(0,9):
        ser.read(3)
        file.write(str(ser.read(6)))
        ser.read(2)
    file.write('\n')
    b=b+1
file.close()
ser.close()