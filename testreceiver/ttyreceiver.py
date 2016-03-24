import serial;

ser = serial.Serial(
    port='/dev/pts/10',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS,
    rtscts=True,
    dsrdtr=True
)
while(True):
    print('waiting')
    line = ser.readline()
    print(line)