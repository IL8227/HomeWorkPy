x = int(input('x='))
y = int(input('y='))
z = int(input('z='))
a = not(x or y or z)
b = not x and not y and not z
if a == b:
    print('утверждение верно')
else:
    print('утверждение не верно')

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.