#Начало
import math

a = int(input(f'\nВведите переменную а: '))
b = int(input('Введите переменную b: '))
c = int(input('Введите переменную c: '))
x = ''
D = b**2 - 4*a*c

D = b**2 - 4*a*c
if D > 0:
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
    print('Дискриминант:',D)
    print(f'Уравнение имеет 2 корня: x1={x1}, x2={x2}')
>>>>>>> c63cfa8077ff9407c23ed655f2104fe5e6d34fc9
