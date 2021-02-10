from _thread import *
import time


lock = allocate_lock()
availableTable = 2

customers = ["A","B","C","D","E","F","G"]

def isEating(delay, name):
    global availableTable
    while(1):
        time.sleep(delay)
        if(availableTable>0):
            availableTable =availableTable-1
            lock.acquire()
            print(" available table: " + str(availableTable))
            print(" Now "+str(name)+ " is eating. ")
            lock.release()
            if(availableTable<2):
                availableTable =availableTable+1
            print(" returning table ")
            exit()
        elif(availableTable==0):
            print(" %s Waiting for table " %name)
        

for i in range(len(customers)):
    start_new_thread(isEating, (1, customers[i]))
