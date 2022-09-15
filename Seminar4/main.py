# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.


# lst = input('Enter a few numbers. The program will return the max and min numbers from your list: ').split(" ")
# print(f'Your list is: {lst}')
# max_num = max(lst)
# min_num = min(lst)
# print(f"Your list's max and min numbers are:")
# print(max_num, min_num)

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# *2) с помощью дополнительных библиотек Python
# import math 

# def equationroots( x, y, z): 
#     discri = y * y - 4 * x * z 
#     sqrtval = math.sqrt(abs(discri)) 
#     # checking condition for discriminant
#     if discri > 0: 
#         print("Real and different roots ") 
#         print((-y + sqrtval)/(2 * x)) 
#         print((-y - sqrtval)/(2 * x)) 
#     elif discri == 0: 
#         print(" real and same roots") 
#         print(-y / (2 * x)) 
# # when discriminant is less than 0
#     else:
#         print("Complex Roots") 
#         print(- y / (2 * x), " + i", sqrt_val) 
#         print(- y / (2 * x), " - i", sqrt_val) 

# x = 1
# y = 17
# z = -18

# if x == 0: 
#     print("Input correct quadratic equation") 
# else:
#     equationroots(x, y, z)
# OR

# a = 1
# b = 10 
# c = 3

# def solution(a, b , c):
#     discri = (b ** 2) - (4 * a * c)
#     if discri > 0:
#         discri = discri ** 0.5
#         answer1 = (-b - discri) / (2 * a)
#         answer2 = (-b + discri) / (2 * a)
#         return answer1, answer2
#     elif discri == 0:
#         discri = discri ** 0.5
#         answer = -b / (2 * a)
#         return answer
#     else:
#         print('Wrong input')
# print(f'Your solution is: {(solution(a, b, c))}')
# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное/Least common multiple) этих двух чисел.
# Ответ записать в файл.

# import math

# def lcm(a, b):
#     if a == 0 or b == 0:
#         return 0
#     else:
#         gcd = math.gcd(a, b)
#         return abs(a * b) / gcd

# print(int(lcm(12, 18)), file = open('./Seminar4/output.txt', 'w'))
# OR

# a = 5
# b = 10

# count = a * b
# while (a !=b):
#     if a > b: 
#         a = a - b
#     else: 
#         b = b - a
# print(count/b)
