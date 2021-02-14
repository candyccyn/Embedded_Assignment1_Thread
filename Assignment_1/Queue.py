import _thread as thread
import time
class Thread_Queue:
    def __init__(self):
        self.qData= []
        self.numThreads =5
        self.count= 4 
        self.lock = thread.allocate_lock()
        
    def process(self,tid,count):
        try:
            time.sleep(1)
            self.qData.pop(0)
            self.lock.acquire()
            for i in range(count):
                print("Thread: ",tid," count: " ,i)
            
        except:
            pass
        else:
            self.lock.release()
        
    def start(self):
        for i in range(self.numThreads):
            self.qData.append(thread.start_new_thread(self.process, (i,self.count)))
        time.sleep(10)  
        print('exit the main thread')
        
t1= Thread_Queue()
t1.start()


