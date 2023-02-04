def createList() :
    d = [
    ('Hendrix' , '1942'),
    ('Allman' , '1946'),
    ('King' , '1925'),
    ('Clapton' , '1945'),
    ('Johnson' , '1911'),
    ('Berry' , '1926'),
    ('Vaughan' , '1954'),
    ('Cooder' , '1947'),
    ('Page' , '1944'),
    ('Richards' , '1943'),
    ('Hammett' , '1962'),
    ('Cobain' , '1967'),
    ('Garcia' , '1942'),
    ('Beck' , '1944'),
    ('Santana' , '1947'),
    ('Ramone' , '1948'),
    ('White' , '1975'),
    ('Frusciante', '1970'),
    ('Thompson' , '1949'),
    ('Burton' , '1939')
        ]
    return d

def createDictionary(dic) :
    flipped = {}
    for key, var in dic.items() :
        if(var not in flipped) :
           flipped[var] = [key]
        else:
            flipped[var].append(key)
    return flipped

def printDictionary(flipped) :
    for i, j in flipped.items() :
        print(str(i) + " : " + str(j).replace("[", "").replace("]", "").replace("\'", "").replace(",", ""))    

def dictionary() :
    dic = dict(createList())
    printDictionary(createDictionary(dic))

        

if __name__ == '__main__' : 
    dictionary()