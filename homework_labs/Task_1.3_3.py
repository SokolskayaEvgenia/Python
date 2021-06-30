import math

"""3. Напишите программу вычисления площади выпуклого пятиугольника.
Исходными данными являются координаты вершин.
Для решения задачи следует использовать метод декомпозиции:
сначала получить площадь треугольников, а их затем сложить.
Для расчета длины стороны и площади треугольника рекомендуется
использовать отдельные функции.​"""

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

A = Point(3.2,8)
B = Point(2,5)
C = Point(5,2)
D = Point(9,4)
E = Point(8,7)

def side_length(point1, point2):
    length = math.sqrt(pow((point2.y - point1.y),2) + pow((point2.x - point1.x),2))
    return length


def triangle_square(a,b,c):
    p = (a + b + c) /2
    square = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return square

AB = side_length(A,B)
BC = side_length(B,C)
AC = side_length(A,C)
CD = side_length(C,D)
DE = side_length(D,E)
EC = side_length(E,C)
AE = side_length(A,E)

ABC_square = triangle_square(AB,BC,AC)
CDE_square = triangle_square(CD, DE, EC)
ACE_square = triangle_square (EC, AE, AC)

ABCDE_square = round((ABC_square + CDE_square + ACE_square), 2)

print ("Площадь выпуклого пятиугольника равна: {0}". format(ABCDE_square))

    
