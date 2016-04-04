from receiver import start_receiver
from multiprocessing import Pool

def dummy_function():
    pass

if __name__ == '__main__':
    print('HyComent Telemetry is starting')
    print('Creating new processes')
    pool = Pool()
    receiver_process = pool.apply_async(start_receiver)
    dummy_process=pool.apply_async(dummy_function)
    try:
        receiver_answer = receiver_process.get()
    except:
        print('ERROR')
    try:
        dummy_answer = dummy_process.get()
    except:
        print('ERROR')
