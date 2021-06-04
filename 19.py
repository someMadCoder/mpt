import itertools

def getNum():
    while type:
        num = input('Длина строки = ')
        try:
            int(num)
        except ValueError:
            print('"' + num + '"' + ' - не является числом')
        else:
            break
    return int(num)


myList = []
myLen = getNum()
myStr = input("Количество символов = ")

def intersection(str):
    for i in range(len(str)):
        for j in range(len(myStr)):
            if myStr[j] not in str:
                return False
    return True

for i in itertools.product(myStr, repeat=myLen):
    myList.append("".join(i))

for i in myList:
    if intersection(i):
        print(i, end=" ")
