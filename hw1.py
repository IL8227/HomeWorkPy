a = int(input('введите цифру обозначающую день недели '))
if 1 <= a <= 5:
    print('будний день')
elif a == 6 or a == 7:
    print('выходной')
else:
    print('ошибка ввода')


