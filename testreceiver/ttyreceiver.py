# -*- coding: utf-8 -*-
import serial;
import binascii;


ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
print('reading 10 bytes at a time:')

while(True):

    print('--------------------')
    line = ser.read(10)
    print([x for x in line])
    print(line.decode('utf-8'))

    

