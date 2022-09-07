# while loop
# i = 1
# while i <= 10:
#     print(i, end=' ')
#     i += 1
#     continue
# else:
#     print('END!')


# 1. Напишите программу, которая принимает на вход число N и
# выдаёт последовательность из N членов.

#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81
# Solution---------------------
# n = int(input('Enter a number: '))
# arr = [1, ]
# for i in range(1, n):
#     arr.append(arr[i-1] * (-3))
# print(arr)
# 2. Для натурального n создать последовательности 3n + 1.

#     *Пример:*
#     - Для n = 6:
#         1: 4,
#         2: 7,
#         3: 10,
#         4: 13,
#         5: 16,
#         6: 19
# Solution---------------------
# n = int(input('Enter a number: '))
# for i in range(1, n+1):
#     result = 3*i + 1
#     print(f'{i}: {result}')
# ---------------------
# 3. Напишите программу, в которой пользователь будет задавать две
# строки, а программа - определять количество вхождений одной строки в другой.

# *Пример:*
# 'Я люблю Питон!'
# 'лю'
# Solution---------------------
# str = "Я люблю Питон"
# result = str.count('лю')
# print(result)


# a = input("Введите строку: ")
# b = input("Введите искомую подстроку: ")
# count = 0
# for i in range (0, len(a)-1):
#     if a[i]+a[i+1] == b:
#         count += 1
#         print(i)
# print(f"{count} раз")

# a = input("Введите строку: ")
# b = input("Введите искомую подстроку: ")
# count = 0

# for i in range (0, len(a) - len(b)):
#     if b == a[i:i + len(b)]:
#         count += 1
# print(f"{count} раз")

