import threading
import time
lock1 = threading.Lock()
lock2 = threading.Lock()


def print_ji():
    for i in range(1, 100, 2):
        lock2.acquire()
        print(i, end=' ')
        time.sleep(0.2)
        lock1.release()


def print_ou():
    for i in range(2, 101, 2):
        lock1.acquire()
        print(i, end=' ')
        time.sleep(0.2)
        lock2.release()

t1 = threading.Thread(target=print_ji)
t2 = threading.Thread(target=print_ou)
lock1.acquire()
t1.start()
t2.start()