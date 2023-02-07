class HotBeverage :
    def __init__(self) :
        self.Name = "hot beverage"
        self.Price = 0.30

    def description(self) :
        return "Just some hot water in a cup."

    def __str__(self) :
        str = "name : " + self.Name + "\nprice : " + "{:.2f}".format(self.Price) + "\ndescription: " + self.description()
        return str

class Coffee(HotBeverage) :
    def __init__(self) :
        HotBeverage.

if __name__ == '__main__' :

    a = HotBeverage()
    print (a)