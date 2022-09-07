# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    
#     *Пример:*
#     - 0,56 -> 11
#----------Solution
# any_number = float(input('Enter a float number to see the sum of consisting digits: '))
# digit_converter = (int(i) for i in str(any_number) if i.isdigit())
# print(f'The sum of consisting digits is: {sum(list(digit_converter))}')    
#----------    
# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#----------Solution
# end_number = int(input('Enter any number: '))

# def factorial(n):
#     if (n == 1 or n == 0):
#         return 1
#     else:
#         return n * factorial(n-1)

# array = [i for i in range(1, end_number+1)]
# mapped = list(map(lambda i: i * factorial(i-1), array))

# print(mapped)
#----------
# 3. Задайте список из k чисел последовательности (1 + 1/k)^k и выведите на экран их сумму.
#     k = 5
#----------Solution
# num = int(input('Enter any number: '))
# array = [i for i in range(1, num+1)]
# mapped = list(map(lambda x: (1 + 1/x)**x, array))
# result = sum(mapped)
# print(f'The sum of float numbers in {mapped} is: {result}.')    
#----------
# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях. 
#----------Solution
# def product(x):
#     result = 1
#     for element in x:
#         result *= element
#     return result

# num = int(input('Enter any number N to get a list of [-N, N]:'))
# lst = [i for i in range(-num,num+1)]
# print(f'Your list is {lst}')
# pick_index = str(input('Enter indexes (separated by space) to get the product of corresponding values from the list: ')) 

# str_list = list((pick_index.split(' ')))
# index_list = [int(i) for i in str_list]

# product_of_indexes = product([lst[i] for i in index_list])
# print(f'The product of the selected values at indexes {index_list} is: {product_of_indexes}.')
#----------
# 5. Реализуйте алгоритм перемешивания списка.
#----------Solution
# from random import random

# some_list = [3, 4, 2, 34, 54, 3, 0, 4, -3, 32]
# print(f'Original list is: {some_list}')
# x = int(input('Enter any number from the list: '))
# while x not in some_list:
#     print(f'This number is not part of the list')
#     break
# else:
#     index_pick = some_list.index(x)
#     def shake_it_up(some_list):
#         for i in range(len(some_list)):
#                 if some_list[i]:
#                     j = int((i+1) * random())
#                     some_list[i], some_list[j] = some_list[j], some_list[i]      
#         return some_list

#     print(f'Shuffled list is: {shake_it_up(some_list)}')
#----------
