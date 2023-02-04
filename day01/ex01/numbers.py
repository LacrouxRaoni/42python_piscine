def my_num() :
    file = open("numbers.txt", 'r')
    print (file.read().replace(',', '\n'))

if __name__ == '__main__' :
    my_num()