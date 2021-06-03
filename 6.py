import math

def getNum(num):
    while type:
        num = input('Введите число ' + num + ': ')
        try:
            float(num)
        except ValueError:
            print('"' + num + '"' + ' - не является числом')
        else:
            break
    return float(num)

a = getNum("a") 
b = getNum("b") 
c = getNum("c") 

dis = (b ** 2) - (4*a*c)
print("Дискриминант = ", dis)
if a == 0:
    x = c / b
    print("x =  %.2f" % x)
elif dis > 0:
    x1 = (-b + math.sqrt(dis)) / (2 * a)
    x2 = (-b - math.sqrt(dis)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif dis == 0:
    x = -b / (2*a)
    print("x =  %.2f" % x)
else:
    print("Нет решения")
