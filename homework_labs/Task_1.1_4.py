import time

"""4. Напишите программу для расчета n!.​"""

try:
    n = int(input("Введите натуральное число, факториал которого хотите вычислить: "))
except ValueError:
    print("Это не число!")
else:
    if n<0:
        print ("Невозможно вычислить!")
    elif n==0:
        print("{0}! = 1".format(n))
    else:
        factorial = 1
        for i in range(2, n+1):
            factorial *= i
        print("{0}! = {1}".format(n,factorial))
finally:
    print("До свидания!")
