
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

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return n



a = getNum("a")
print(factorial(a))