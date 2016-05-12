import receiver
import logger
import signal
import sys
#from r import Receiver
#from logger import Logger
from multiprocessing import Pool
from threading import Thread

def dummy_function():
    pass

class HyComentTelemetrie:

    def __init__(self):
        self.logger = logger.Logger()
        self.receiver = receiver.Receiver(self.logger)

    def start_processes(self):
        t = Thread(target=self.receiver.start)
        t.start()
        #pool = Pool()
        #receiver_process = pool.apply_async(self.receiver.start_receiver)
        #dummy_process = pool.apply_async(dummy_function)
        #receiver_answer = receiver_process.get()
        #dummy_answer = dummy_process.get()

    def shutdown_handler(self,signal, frame):
        self.logger.close_file()
        self.receiver.close_receiver()
        print('shutdown')
        sys.exit(0)




if __name__ == '__main__':
    hy_comment_tel = HyComentTelemetrie()
    hy_comment_tel.start_processes()
    signal.signal(signal.SIGINT, hy_comment_tel.shutdown_handler)

