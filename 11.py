def getNum(num):
    while type:
        num = input('Введите ' + num + ': ')
        try:
            int(num)
        except ValueError:
            print('"' + num + '"' + ' - не является числом')
        else:
            break
    return int(num)

a = getNum("основание")
b = getNum("степень")

num = a

for i in range(b-1):
    a *= num
print(a)