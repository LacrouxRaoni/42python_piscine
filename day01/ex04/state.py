import sys

def dicsCitiesStates(city) :

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
    for key, value in capital_cities.items() :
        if (value == city) :
            for key2, value2 in states.items() :
                if (key == value2) :
                    return key2
    return 0

def getCity(city) :
    state = dicsCitiesStates(city)
    if (state == 0) :
        print("Unknown capital city")
    else:
        print(state)

if __name__ == '__main__' :
    if (len(sys.argv) == 2) :
        getCity(sys.argv[1])
