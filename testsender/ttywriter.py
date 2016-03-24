import time
import serial
import termios

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/pts/13',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS,
    rtscts=True,
    dsrdtr=True
)

#ser.isOpen()

print('Enter your commands below.\r\nInsert "exit" to leave the application.')
while 1 :
    # get keyboard input
    userInput = input()
    #userInput = raw_input()
        # Python 3 users
        # input = input(">> ")
    if userInput == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        output=(userInput+'\r\n')
        print(output)
        ser.write(output.encode('latin-1'))
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)
        if out != '':
            print( ">>" + out)
