from ast import arg
import threading
import time
import random

class Urna1():
    def __init__(self, urna=0):
        self.locked = threading.Lock()
        self.urna_send = urna
        

    def incrementar(self):
        self.locked.acquire() #Esperar a que locked termine 

        try:
            self.urna_send += 1
            print("Turno:",self.urna_send,"de la urna Num 1")
        finally:
            print("La persona con el turno",self.urna_send,"de la urna 1 ha terminado de votar")
            self.locked.release()        

def func_urna(x):
    for y in range(4):
        time_f=random.random()
        time.sleep(time_f)
        x.incrementar()
        
class Urna2():
    def __init__(self, urna2=0):
        self.locked = threading.Lock()
        self.urna2_send = urna2

    def incrementar2(self):
        self.locked.acquire() #Esperar a que locked termine 

        try:
            self.urna2_send += 1
            print("Turno:",self.urna2_send," de la urna Num 2")
        finally:
            print("La persona con el turno",self.urna2_send,"de la urna 2 ha terminado de votar")
            self.locked.release()

def func_urna2(x):
    for y in range(4):
        time_f=random.random()
        time.sleep(time_f)
        x.incrementar2()





if __name__ == "__main__":
    urna1=Urna1()
    urna2=Urna2()
    for y in range(4):
         tsart= threading.Thread(target=func_urna, args=(urna1,))
         tsart.start()

    for z in range(4):
         tsart= threading.Thread(target=func_urna2, args=(urna2,))
         tsart.start()    
    