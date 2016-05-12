import serial

class Receiver:
    def __init__(self, logger, port = '/dev/pts/20', baudrate=9600):
        self.ser = None
        self.logger = logger
        self.port = port
        self.baudrate = baudrate
        self.running = True


    def start(self):
        self.start_receiver(self.port, self.baudrate)
        self.start_reading()

    def start_receiver(self, port, baudrate):
        self.ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS,
            rtscts=True,
            dsrdtr=True
        )

    def close_receiver(self):
        self.running = False
        self.ser.close()

    def start_reading(self):
        while(self.running):
            print('reading')
            input = self.ser.readline()
            self.logger.log_data(input)