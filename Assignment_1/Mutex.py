import _thread 
import time

class Thread():
    def __init__(self,mutex):
        self.mutex = mutex     
    def counter(self,tid,count):
        for i in range(count):
            time.sleep(1)
            self.mutex.acquire()
            print("Thread: ",tid," count: " ,i)
            self.mutex.release()
    def start(self):
        for i in range(3):
            _thread.start_new_thread(self.counter, (i, 3))
        time.sleep(4)
        print('Main thread exiting...')
        
        
mutex = _thread.allocate_lock()
t1 = Thread(mutex)
t1.start()
