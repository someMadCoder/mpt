def powerOfTwo(n):
    count = 0
    d = 1
    while d <= n:
        count += 1
        d = d * 2
    return count

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

a = getNum("")
print(powerOfTwo(a))