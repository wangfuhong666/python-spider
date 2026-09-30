import threading
import time
#lock = threading.Lock()
a = 100
def test1():
    print('test1')
    global a
    #lock.acquire()
    for i in range(10000000):
        a-=1
    #time.sleep(3)
    print('test1 is over')
    #lock.release()

def test2():
    print('test2')
    global a
    #lock.acquire()
    for i in range(10000000):
        a+=1
    #time.sleep(3)
    print('test2 is over')
    #lock.release()
f1 = threading.Thread(target=test1)
f2 = threading.Thread(target=test2)
f1.start()
f2.start()
f1.join()
f2.join()
print(a)