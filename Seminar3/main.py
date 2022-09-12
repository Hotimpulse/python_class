# 2 TASK
# myList = ['65h734q', 'sdg634d', '147jnbv']
# n = '7'
# for i in myList:
#     if i.find(n) >= 0:
#         print(i)

# 3 TASK
# myList = ["1", "qwe", "asd", "zxc", "qwe", "ertqwe", "qwe"]
# myString = '5'
# count = 0
# for i in range(0, len(myList)):
#     if myList[i] == myString:
#         count += 1
#         if count == 2:
#             print(i)
#             break
# if count < 2:
#     print("False")



# import time

# start = time.time()
# print("hello")
# end = time.time()
# print(end - start)

import random
import time
sec = str(time.time())
num = sec[-1]
user_input = int(input("Enter range for your random number generator: "))
count = 0
if user_input//10>0:
    count += 1
num = sec[-count:-1]
print(num)