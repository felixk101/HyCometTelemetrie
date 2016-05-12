class Logger:

    def __init__(self, file_name='HyComent_Telemetrie.txt'):
        self.file_name = file_name
        self.file = None

        self.open_file()

    def open_file(self):
        print(self.file_name)
        self.file = open(self.file_name,'a')

    def log_data(self, data):
        print(data)
        self.file.write(data.decode("utf-8")+'\n')

    def close_file(self):
        self.file.close()
