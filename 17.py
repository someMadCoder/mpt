dict = {}
tableNumbers = []
uniqueNumbers = []

countRed = 0
countBlack = 0

for i in range(0,37):
    tableNumbers.append(str(i))

red = [1, 3, 5, 7, 9, 12, 14, 16, 18,  19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

redStr = [str(i) for i in red]
blackStr = [str(i) for i in black]

def getTable():
    sortKeyArr = sorted(dict, key=dict.get)
    sortKeyArrInt = [int(i) for i in sortKeyArr]
    tableNumbersInt = [int(i) for i in tableNumbers]
    newList = list(set(tableNumbersInt) - set(sortKeyArrInt))
    newListStr = [str(i) for i in newList]
    return " ".join(newListStr)

def getNum():
    while type:
        getNum = input('')
        try:
            int(getNum)
        except ValueError:
            print('"' + getNum + '"' + ' - не является числом')
        else:
            break
    return int(getNum)


def getMaxKey():
    sortKeyArr = sorted(dict, key=dict.get)
    return " ".join(sortKeyArr)

def addToDict(num):
    if dict.get(num) == None:
        dict[num] = 1
    else:
        dict[num] += 1

gameOver = False

while not gameOver:
    
    a = getNum()
    addToDict(str(a)) 

    if str(a) in blackStr:
        countBlack += 1
    elif str(a) in redStr:
        countRed += 1

    print(getMaxKey())
    print(getTable())
    print(str(countRed) + " " + str(countBlack))

    if a == -1:
        gameOver = True
