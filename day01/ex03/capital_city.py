import sys

def dicsCitiesStates(state) :

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
        if (key == state) :
            for key2, value2 in capital_cities.items() :
                if (key2 == value) :
                    return value2
    return 0

def getState(state) :
    capital = dicsCitiesStates(state)
    if (capital == 0) :
        print("Unknown state")
    else:
        print(capital)

if __name__ == '__main__' : 
    if (len(sys.argv) == 2) :
        getState(sys.argv[1])
    