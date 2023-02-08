import random
from beverages import *

class CoffeeMachine :
    count = 10
    def __init__(self) :
        pass
    class EmptyCup (HotBeverage) :
        def __init__(self) :
            self.name = "empty cup"
            self.price = 0.90
        
        def description(self):
            return "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException (Exception) :
        def __init__(self) :
            super().__init__("This coffee machine has to be repaired.")

    def repair(self) :
        if self.count == 0 :
            self.count = 10

    def serve(self, order) :
        self.count -= 1
        if self.count == 0 :
            raise self.BrokenMachineException()
        if (random.randrange(0, 2) == 0) :
            return self.EmptyCup()
        return order()

if __name__ == '__main__' :
    
    j = 0
    a = CoffeeMachine()
    print(a.count)
    
    for i in range (0, 20) :
        try :
            b = a.serve(random.choice([HotBeverage, Coffee, Tea, Chocolate, Cappuccino]))
            print(b)
            print("Machine counter: ", a.count)
        except Exception as e :     
            print ("\n\n")
            print (e)
            print ("\n\n")
            a.repair()

