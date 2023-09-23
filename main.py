#Начало
import math

a = int(input(f'\nВведите переменную а: '))
b = int(input('Введите переменную b: '))
c = int(input('Введите переменную c: '))

D = b**2 - 4*a*c

print('\nДискриминант равен:', D)

if D == 0:
    x = b+b**2/2*a
    print(f'Ответ уравнения: {x}')

if D<0:
    print('Уравнение не имеет корней')

if D > 0:
    x1=(b+math.sqrt(D))/(2*a)
    x2=(b-math.sqrt(D))/(2*a)
    print(f'Уравнение имеет 2 корня: x1={x1}, x2={x2}')