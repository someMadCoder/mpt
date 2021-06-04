def getNum(text):
    while type:
        num = input(text)
        try:
            int(num)
        except ValueError:
            print('"' + num + '"' + ' - не является числом')
        else:
            break
    return int(num)

List = []
money = getNum('Введите кол-во денег: ')
drink = getNum('Введите кол-во доступного алкоголя: ')

name = ""
botles = 0
alcoLitres = 0

def sort(alcohol):
    return alcohol.get('price') / alcohol.get('litres')

while drink:
    drink -= 1
    name, price, litres = input("Введите [Название алкоголя, стоимость, кол-во] через пробел: ").split()
    List.append({"name": name, "price": int(price), "litres": int(litres)})


List.sort(key=sort) 

if (money >= List[0]["price"]):
    name = List[0]["name"] 
    alcoholPrice = List[0]["price"]
    while ((money - alcoholPrice) > 0):
        money -= alcoholPrice
        alcoLitres += List[0]["litres"]
        botles += 1
    print(name + " " + str(botles))
    print(alcoLitres)
    print(money)
else:
    print(-1)