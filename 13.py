def primeCheck(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n and "Простое" or "Составное"

def getNum(num):
    while type:
        num = input('Введите число ' + num + ': ')
        try:
            int(num)
        except ValueError:
            print('"' + num + '"' + ' - не является числом')
        else:
            break
    return float(num)


a = getNum("a")
print(primeCheck(a))
