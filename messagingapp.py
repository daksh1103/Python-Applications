import serial
import time
from threading import Thread
s1=serial.Serial(
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)
def check_ports():
    while(1):
        try:
            g=input()
            s1.write(g.encode('ascii'))
        except Exception as e:
            print(e)

def check():
    while(1):
        try:
            g1=s1.readline().decode('ascii')
            if(len(g1)>0):
                print('RECEIVED: '+g1)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    a=0
    s1.port='/dev/ttyUSB0'
    s1.open()
    Thread(target = check_ports).start()
    Thread(target = check).start()
