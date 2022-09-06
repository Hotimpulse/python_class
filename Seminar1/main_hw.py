# H/W
# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#     *Пример:*

#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет
# Solution---------------------
# some_number = int(input("Enter any number between 1 and 7 to see if it's the weekend: "))
# list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# if (1 <= some_number <= 5):
#     print(f'{list[some_number - 1]} is a weekday.')
# elif (some_number <= 7):
#     print(f'{list[some_number - 1]} is the weekend.')
# else:
#     print('That is not the right number!')
# ---------------------

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Solution---------------------
# def enterNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Enter the value of {xyz[i]}: "))
#     return a


# def isPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result


# statement = enterNumbers(3)

# if isPredicate(statement) == True:
#     print(f"The statement is true")
# else:
#     print(f"The statement is false")
# ---------------------
# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).


#     *Пример:*

#     - x=34; y=-30 -> 4
#     - x=2; y=4-> 1
#     - x=-34; y=-30 -> 3
# Solution---------------------
# print('Enter xy coordinates of a point to see which quadrant it occupies.')
# x = int(input('Enter x: '))
# y = int(input('Enter y: '))
# if ((x and y) > 0):
#     print('Your point is in the 1st quadrant.')
# elif (x < 0 and y > 0):
#     print('Your point is in the 2nd quadrant.')
# elif (x < 0 and y < 0):
#     print('Your point is in the 3rd quadrant.')
# elif (x > 0 and y < 0):
#     print('Your point is in the 4th quadrant.')
# else:
#     print('Your point is at the intersection')
# ---------------------
# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# Solution---------------------
# print('Enter a quadrant number (1-4) to get a range of possible x and y coordinates.')
# number = int(input('Enter a quadrant number (1 - 4): '))

# def task_four(quadrant):
#     match quadrant:
#         case (1):
#             x = [i for i in range(10)]
#             y = [i for i in range(10)]
#             print(f'X is in {x}.\nY is in {y}.')
#         case (2):
#             x = [-i for i in range(10)]
#             y = [i for i in range(10)]
#             print(f'X is in {x}.\nY is in {y}.')
#         case (3):
#             x = [-i for i in range(10)]
#             y = [-i for i in range(10)]
#             print(f'X is in {x}.\nY is in {y}.')
#         case (4):
#             x = [i for i in range(10)]
#             y = [-i for i in range(10)]
#             print(f'X is in {x}.\nY is in {y}.')

# task_four(number)
# ---------------------
# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#     *Пример:*

#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21
# Solution---------------------
# print("Enter two coordinates to see the distance between the 2 points.")

# x1 = int(input("enter x1: "))
# y1 = int(input("enter y1: "))
# x2 = int(input("enter x2: "))
# y2 = int(input("enter y2: "))

# result = ((((x2 - x1)**2) + ((y2 - y1)**2))**0.5)
# mystr = str(result)

# print(f"Distance between {(x1, x2)} and {(y1, y2)} is: {mystr[0:4]}")
# ---------------------
