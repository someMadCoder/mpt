import math

def getNum(num):
    while type:
        num = input('Введите число ' + num + ': ')
        try:
            int(num)
        except ValueError:
            print('"' + num + '"' + ' - не является числом')
        else:
            break
    return int(num)

s_type = getNum("Способ нахождения (1 - по сторонам, 2 - по координатам)")
if s_type == 1:
    a = getNum("Сторона а")
    b = getNum("Сторона b")
    c = getNum("Сторона c")

    p = (a + b + c) / 2
    ans = math.sqrt(p * (p-a) * (p-b) * (p-c))
    print('Площадь: {0}'.format(ans))
elif s_type == 2:
    x1, y1 = input("Введите координаты x1 и y1 через пробел: ").split()
    x2, y2 = input("Введите координаты x2 и y2 через пробел: ").split()
    x3, y3 = input("Введите координаты x3 и y3 через пробел: ").split()

    ans = abs((int(x2)-int(x1))*(int(y3)-int(y1))-(int(x3)-int(x1))*(int(y2)-int(y1)))/2
    print('Площадь: {0}'.format(ans))
else:
    print("Ошибка")
