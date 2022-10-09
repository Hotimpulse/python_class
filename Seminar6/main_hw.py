# Задача: предложить улучшения кода для уже решённых задач (3-5 задач):
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     *Пример:*
#     - 0,56 -> 11
#----------Solution
# any_number = float(input('Enter a float number to see the sum of consisting digits: '))
# digit_converter = (int(i) for i in str(any_number) if i.isdigit())
# print(f'The sum of consisting digits is: {sum(list(digit_converter))}')
#-------------------
#Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]
#Solution---------
# lst = [1, 1, 2, 3, 4, 5, 5]
# new_lst = [i for i in lst if lst.count(i) == 1]
# print(new_lst)
#-------------------
# 3. Задайте список из k чисел последовательности (1 + 1/k)^k и выведите на экран их сумму.
#     k = 5
#----------Solution
# num = int(input('Enter any number: '))
# array = [i for i in range(1, num+1)]
# mapped = list(map(lambda x: (1 + 1/x)**x, array))
# result = sum(mapped)
# print(f'The sum of float numbers in {mapped} is: {result}.') 