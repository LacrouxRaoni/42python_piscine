class HotBeverage :
    name = "hot beverage"
    price = 0.30

    def description(self) :
        return "Just some hot water in a cup."

    def __str__(self) :
        str = "name : " + self.name + "\nprice : " + "{:.2f}".format(self.price) + "\ndescription: " + self.description()
        return str

class Coffee(HotBeverage) :
    def __init__(self) :
        self.name = "coffee"
        self.price = 0.40

    def description(self) :
       return "A coffee to stay awake."

class Tea(HotBeverage) :
    def __init__(self) :
        self.name = "tea"

class Chocolate(HotBeverage) :
    def __init__(self) :
        self.name = "chocolate"
        self.price = 0.50

    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage) :
    def __init__(self) :
        self.name = "cappuccino"
        self.price = 0.45
    
    def description(self):
        return "Un po’ di Italia nella sua tazza!"


if __name__ == '__main__' :

    drink = HotBeverage()
    print (drink)
    print ("\n")

    drink = Coffee()
    print(drink)
    print ("\n")

    drink = Tea()
    print (drink)
    print ("\n")

    drink = Chocolate()
    print (drink)
    print ("\n")

    drink = Cappuccino()
    print (drink)
    print ("\n")

