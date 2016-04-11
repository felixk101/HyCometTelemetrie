import serial;
import binascii;

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
while(True):


    print('waiting')
    line = ser.readline()
    print(line)

    #binary = binascii.unhexlify(b'TELEM 22570954020800f207207401002f0bbbff320840ff8cff1200d2ffc50037ffa601f885a0')
    #print(binary)
