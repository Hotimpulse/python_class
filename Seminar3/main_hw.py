# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

#----------Solution
# some_list = [2, 3, 5, 9, 3]
# new_array = 0
# for i in range(len(some_list)):
#     if i % 2 != 0:
#         new_array += some_list[i]
# print(new_array)
#----------

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

#----------Solution
# lst = [2, 3, 4, 5, 6]
# sorted = []
# for i in lst:
#     if len(lst) % 2 != 0:
#         i = lst[0] * lst[-1]
#         lst = lst[1:-1]
#         sorted.append(i)
# while len(lst) > 0:
#     i = lst[0] * lst[-1]
#     lst = lst[1:-1]
#     sorted.append(i)
# print(sorted)
#----------

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

#----------Solution
# some_list = [1.1, 1.2, 3.1, 10.01]
# x = [(i - int(i)) for i in some_list]
# new_list = ['%.2f' % i for i in x]
# max = max(new_list)
# min = min(new_list)
# print(f'The difference between {max} and {min} decimals is: {float(max) - float(min)}')
#----------

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

#----------Solution
# def tobin(x):
#     if x == 0: return 0
#     lst = []
#     while x:
#       lst.append(x % 2)
#       x >>= 1
#     return lst[::-1]
# print(tobin(45))
#----------

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

#----------Solution
# k = int(input('Enter any N number to see the Fibonacci sequence: '))
# def fibonacci(k):
#     if k >= 0:
#         idx = range(k+1)
#         x = [0, 1]
#         for k in idx[2:]:
#             x.append(x[k-1] + x[k-2])
#         return x[k]
#     else:
#         k = -(k-1)
#         idx = range(k+1)
#         x = [1,0]
#         for k in idx[2:]:
#             x.append(x[k-2] - x[k-1])
#         x.reverse()
#     return x[0]
# lst = [fibonacci(i) for i in range(-k, k+1)]  
# print(lst)
#----------






















