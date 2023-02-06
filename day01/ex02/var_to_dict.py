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

def createDictionary(d) :
    dic = {}
    for key, var in d :
        if(var not in dic) :
           dic[var] = [key]
        else:
            dic[var].append(key)
    return dic

def printDictionary(dic) :
    for i, j in dic.items() :
        print(str(i) + " : " + str(j).replace("[", "").replace("]", "").replace("\'", "").replace(",", ""))    


def dictionary() :
    d = createList()
    dic = createDictionary(d)
    printDictionary(dic)


if __name__ == '__main__' : 
    dictionary()