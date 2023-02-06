import sys

def dicsCitiesStates(city) :
    
    city = str(city).title()
    city =  " ".join(city.split())
 
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    for key, value in states.items() :
        if key == city :
            for key2, value2 in capital_cities.items() :
                if value == key2 :
                    print (value2 + " is the capital of " + city)
                    return True
    for key, value in capital_cities.items() :
        if value == city :
            for key2, value2 in states.items() :
                if key == value2 :
                    print (value + " is the capital of " + key2)
                    return True
    return False

def parseLine(line) :
    lst = str(line).split(',')
    for i in range (len(lst)) :
        lst[i] = lst[i].strip()
    return lst

def checkInDic(lst) :
    for i in lst :
        if not dicsCitiesStates(i) :
            if  i :
                print(i + " is neither a capital city nor a state")            

if __name__ == '__main__' :
    if (len(sys.argv) == 2) :
        lst = parseLine(sys.argv[1])
        checkInDic(lst)
