# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 4 5

# with open('Exercise_01.txt', 'r') as f:
#     string = f.readline()

# string = string.split(' ')
# string = list(map(int, string))

# for i in range(1, len(string)):
#     if string[i] - 1 != string[i - 1]:
#         print(f'Missed: {}')
#         break
#     else:
#         print('Good')
# OR
# lst = [(string[i] - 1) for i in range(1, len(string)) if string[i] - 1 != string[i - 1]]
# print(lst)


# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.
# my_list = [1, 5, 2, 3, 4, 6, 1, 7]
# count = 0
# new_list = ([my_list[i] for i in range(1, len(my_list)) if my_list[i] >= max(my_list[0:i])])
# new_list.insert(0, my_list[0])
# print(new_list)

# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавабв'
# 'Мы очень любим Питон'

# text = 'Мы неабв очень любим Питон иабв Джавабв'

# text_find = 'абв'
# index = 0

# lst = text.split(' ')
# print(lst)

# i = 0
# while i in range(len(lst)):
#     if text_find in lst[i]:
#         lst.remove(lst[i])
#     else:
#         i += 1

# lst2 = [item for item in lst if text_find not in item]
# print(lst2)