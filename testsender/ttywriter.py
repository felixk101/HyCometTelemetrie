import time
import serial
import random
import termios

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/pts/26',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS,
    rtscts=True,
    dsrdtr=True
)

#ser.isOpen()
sendList = ['HyComent speed : 50 ',
            'HyComent height: 40',
            'HyComent acceleration: 100',
            'HyComent temperature(inner): 20',
            'HyComent temperature(outer): 22',
            ]
while 1 :

    # send the character to the device
    # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)

    ser.write((sendList[random.randint(0,len(sendList)-1)]+"\r\n").encode('latin-1'))
    print('Message sent')
    out = ''
    # let's wait one second before reading output (let's give device time to answer)
    time.sleep(1)
