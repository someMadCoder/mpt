a, operation, b = input("Введите через пробел число1, операцию (+, -, *, /), число2: ").split()
if operation == "+":
    print("= {0}".format(float(a) + float(b)))
elif operation == "-" :
    print("= {0}".format(float(a) - float(b)))
elif operation == "*" :
    print("= {0}".format(float(a) * float(b)))
elif operation == "/" :
    print("= {0}".format(float(a) / float(b)))
else:
    print("Ошибка")