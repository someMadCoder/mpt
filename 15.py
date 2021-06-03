import random

answers = ["Загаданное число больше", "Загаданное число меньше", "Поздравляю! Вы угадали"]


def game(inputNum, rndNum):
    if (inputNum < rndNum):
        answer = 0
    elif (inputNum > rndNum):
        answer = 1
    else:
        answer = 2
    print(answers[answer])
    return answer

def getNum(count):
    while type:
        num = input('{0}-ая попытка. Попробуйте угадать число: '.format(count+1))
        try:
            int(num)
        except ValueError:
            print('"' + num + '"' + ' - не является числом')
        else:
            break
    return float(num)



gameOver = False

while gameOver==False:

    i = 0
    cnt = 5
    rndNum = random.randint(0, 50)

    while cnt > i:
        a = getNum(i)
        result = game(a, rndNum)
        i += 1
        if result == 2:
            break
        elif i == cnt and result != 2:
            print("Вы проиграли! Было задано число: {0}".format(rndNum))

    check = input("Хотите начать сначала? (1 - ДА ): ")
    if check != "1":
        gameOver = True
