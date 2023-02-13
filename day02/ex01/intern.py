class Intern :
    def __init__(self, Name = "My name? I’m nobody, an intern, I have no name.") :
        self.Name = Name

    def __str__(self) :
        return self.Name

    def work(self) :
        raise Exception ("I’m just an intern, I can’t do that...")

    class Coffee :
        def __str__(self) :
            return "This is the worst coffee you ever tasted."
    
    def make_coffe(self) :
        return self.Coffee()


if __name__ == '__main__' :
  
    try :
        a = Intern()
        print ("Standard Constructor called: ")
        print (a)
        c = Intern("Mark")
        print ("Param Constructor called: ")
        print (c)
        print ("Raoni is making coffee: ")
        b = a.make_coffe()
        print (b)
        print ("Raoni is yelling with Mark")
        a.work()
    except Exception as e : 
        print (e)
 