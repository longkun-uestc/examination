import threading
import time
lock1 = threading.Lock()
lock2 = threading.Lock()
def show1():
    for i in range(1, 52, 2):
        lock2.acquire()
        print(i, end='')
        print(i+1, end='')
        time.sleep(0.2)
        lock1.release()

def show2():
    for i in range(26):
        lock1.acquire()
        print(chr(i+ord('A')), end=' ')
        time.sleep(0.2)
        lock2.release()


t1 = threading.Thread(target=show1)
t2 = threading.Thread(target=show2)
lock1.acquire()
t1.start()
t2.start()
