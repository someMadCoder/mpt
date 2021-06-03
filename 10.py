s, l1, r1, l2, r2 = [int(x) for x in input("Введите число и два диапазона целых чисел через пробел: ").split()]
sum = l1 + r2

if (sum == s):
    print(str(l1) + " " + str(r2))
elif (s > sum):
    if ((sum - s) + l1 >= l1) and ((sum - s) + l1 <= r1):
        print(str(sum) + " " + str(r2))
    else:
        print(-1)
elif (s < sum):
    if (r2 - (sum - s) >= l2) and (r2 - (sum - s) <= r2):
        print(str(l1) + " " + str(sum))
    else:
        print(-1)
 