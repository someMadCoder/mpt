import re

def getNum():
    while type:
        num = input('Введите кол-во номеров: ')
        try:
            int(num)
        except ValueError:
            print('"' + num + '"' + ' - не является числом')
        else:
            break
    return float(num)

ticketFound = False
a = getNum()
tickets = input("Введите номера билетов через пробел: ".format("a")).split()

for ticket in tickets:
    match = re.search(r'a.{3}55661', ticket)
    if match:
        print(match.group())
        ticketFound = True

if not ticketFound:
    print(-1)