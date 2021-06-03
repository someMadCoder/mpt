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


x0 = getNum("x0") 
v0 = getNum("v0") 
t = getNum("t")
a = g = 9.81

result = x0 + v0*t - 1/2*a*t*t  
print(result)