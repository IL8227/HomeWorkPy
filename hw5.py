from cmath import sqrt


print('Введите координаты точки A:')
x_A = float(input('xA= '))
y_A = float(input('yA= '))
print('Введите координаты точки B:')
x_B = float(input('xB= '))
y_B = float(input('yB= '))
import math
d = ((x_B-x_A)**2+(y_B-y_A)**2)
sqrt = math.sqrt(d)
print('A: ','x=',x_A,';','y=',y_A,'B: ','x=',x_B,';','y=',y_B,'расстояние между точками -> ',sqrt)
