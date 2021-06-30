import math
import numpy as np


"""2. Создайте программу
для заполнения списка размерности m x n числами x^y, где x = 1..m, y = 1..n.​"""

m = int(input("Введите количество строк списка: "))
n = int(input("Введите количество столбцов списка: "))
a = []
for x in range (1,m+1):
    for y in range (1,n+1,1):
        a.append(pow(x,y))
        
a= np.reshape(a,(m,n))
print(a)

"""for i in range(m):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    A.append(row)"""
