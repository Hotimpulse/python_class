#1. Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141
#Solution---------
# from math import acos

# def print_pi():
#     pi = round(2 * acos(0.0), d)
#     print(pi)
# d = int(input('Enter a number to get this many decimal places in pi: '))
# print_pi()
#---------
#2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]
#Solution---------
# import math

# def get_multiples(N):
#     while N % 2 == 0 and N != 0:
#         N = N / 2
#         lst.append(2)
#     for i in range(3, int(math.sqrt(N)) + 1, 2):
#         while N % i == 0:
#             N = N / i
#             lst.append(i)
#     if N > 2:
#         lst.append(round(N))
#     if N == 0:
#         print(f'Try a different number')
        
# lst = []
# N = int(input('Enter a number N to see a list of prime factors of N: '))
# get_multiples(N)
# print(lst)
#---------
#3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]
#Solution---------
# lst = [1, 1, 2, 3, 4, 5, 5]
# new_lst = [i for i in lst if lst.count(i)==1]
# print(new_lst)
#---------
#4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#Solution---------

# import random

# def poly_func(coeff: list, arg: str, power: int):
#     result = ''
#     for i in range(k):
#         result += '{}*{}^{} + '.format(coeff[i], arg, power)
#         power -= 1
#     return (result[:-2] + '= 0')

# k = int(input('Enter a "k" number to get a polynomial with k coefficients to the power of k--.\nYour answer will be in a file called hw_task4.txt: '))
# lst = []
# for i in range(k):
#     lst.append(random.randint(0,100))
# x = 'x'

# print(f'Your polynomial for k = {k} is: {poly_func(lst, x, k)}', file = open('./Seminar4/hw_task4.txt', 'w'))

#---------
# Output
#|
#|
#\/
# Enter a "k" number to get a polynomial with k coefficients to the degree of k.
# Your answer will be in a file called hw_task4.txt: 3
# Your polynomial for k = 3 is: 52*x^3 + 23*x^2 + 66*x^1 = 0
#---------

#5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#Solution---------
# import sympy as sym
# from IPython.display import display, Math

# from hw_task5_v1 import p1
# from hw_task5_v2 import p2

# my_str = f'{display((Math(sym.latex(p1 + p2))))}' #--> рабочий вариант, но складывает только в онлайн Jupiter notebook, записать в файл не получается 
# #(пишет в консоль <IPython.core.display.Math object>, а в файл пишет None)

# with open("Seminar4/hw_task5_v1.py", "r") as f1, open("Seminar4/hw_task5_v2.py", "r") as f2, open("Seminar4/hw_task5_res.ipynb", "w") as add_txt:
#     num_sum = map(sum, zip(map(int, f1.readlines()), map(int, f2.readlines())))
#     add_txt.write(my_str) #--> не рабочий вариант, хотел чтобы делал хотя бы jupiter файл, в файл пишет None

#---------
#
#
#
#
#
#
#---------
#другая провальная попытка, делаю два дня одну задачу без особого результата, поэтому забиваю
#import re
#p1 = str(p1) #['95*x**3', '+', '74*x**2', '+', '90*x']
#p2 = str(p2) #['70*x**3', '+', '77*x**2', '+', '84*x']
#lst1 = list(filter(str.isdigit, p1)) #['9', '5', '3', '7', '4', '2', '9', '0']
#lst2 = list(filter(str.isdigit, p2)) #['7', '0', '3', '7', '7', '2', '8', '4']



# x = re.sub('[x*123 ]', '', p1)
# y = re.sub('[x*123]', '', p2)

#x = list(map(int, x))

# z = [int(i) for i in x if i.isdigit()]

# print(z)
#---------




