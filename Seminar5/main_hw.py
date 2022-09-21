# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'Мы неабв очень любим Питон иабв Джавабв'
# 'Мы очень любим Питон'
#Solution
# text = 'Мы неабв очень любим Питон иабв Джавабв'
# text_find = 'абв'

# lst = text.split(' ')
# print(lst)

# lst2 = [item for item in lst if text_find not in item]
# print(lst2)
#---------
# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
#Solution
# import random

# def make_move():
#     first_move = random.randrange(1, 3)
#     print(f'First player to make a move is player number {first_move}')
#     candy = 2021
#     take_candy = 28
#     stop = ((candy % take_candy) + 1)
#     if first_move == 1:
#         while (candy >= stop):
#             candy -= take_candy
#             print(f'Player 1 takes 28 pieces of candy. Candy left: {candy}')
#             candy -= take_candy
#             print(f'Player 2 takes 28 pieces of candy. Candy left: {candy}')
#             if candy < 33:
#                 print(f'Player 1 takes the last {candy} pieces and wins!. To win, the first player needs to take {take_candy} pieces.')

#     if first_move == 2:
#         while (candy >= stop):
#             candy -= take_candy
#             print(f'Player 2 takes 28 pieces of candy. Candy left: {candy}')
#             candy -= take_candy
#             print(f'Player 1 takes 28 pieces of candy. Candy left: {candy}')
#             if candy < 33:
#                 print(f'Player 2 takes the last {candy} pieces and wins! To win, the first player needs to take {take_candy} pieces.')
# make_move()
#---------

# 3. Создайте программу для игры в ""Крестики-нолики"".
#Solution

# from tkinter import *
# import random

# def next_move(row, column):
#     global player

#     if btns[row][column]['text'] == "" and check_who_won() is False:

#         if player == players[0]:

#             btns[row][column]['text'] = player

#             if check_who_won() is False:
#                 player = players[1]
#                 label.config(text = (players[1] + " turn"))

#             elif check_who_won() is True:
#                 label.config(text = (players[0] + " wins"))

#             elif check_who_won() == "Tie":
#                 label.config(text = ("Tie!"))
#         else:

#             btns[row][column]['text'] = player

#             if check_who_won() is False:
#                 player = players[0]
#                 label.config(text = (players[0] + " turn"))
#             elif check_who_won() is True:
#                 label.config(text = (players[1] + " wins"))
#             elif check_who_won() == "Tie":
#                 label.config(text = ("Tie!"))

# def check_who_won():
    
#     for row in range(3):
#         if btns[row][0]['text'] == btns[row][1]['text'] == btns[row][2]['text'] != "":
#             btns[row][0].config(bg = "green")
#             btns[row][1].config(bg = "green")
#             btns[row][2].config(bg = "green")
#             return True

#     for column in range(3):
#         if btns[0][column]['text'] == btns[1][column]['text'] == btns[2][column]['text'] != "":
#             btns[0][column].config(bg = "green")
#             btns[1][column].config(bg = "green")
#             btns[2][column].config(bg = "green")
#             return True

#     if btns[0][0]['text'] == btns[1][1]['text'] == btns[2][2]['text'] != "":
#             btns[0][0].config(bg = "green")
#             btns[1][1].config(bg = "green")
#             btns[2][2].config(bg = "green")
#             return True

#     elif btns[0][2]['text'] == btns[1][1]['text'] == btns[2][0]['text'] != "":
#         btns[0][2].config(bg = "green")
#         btns[1][1].config(bg = "green")
#         btns[2][0].config(bg = "green")
#         return True

#     elif empty_space() is False:

#         for row in range(3):
#             for column in range(3):
#                 btns[row][column].config(bg = "#FF6C4D")
#         return "Tie"

#     else: 
#         return False

# def empty_space():
    
#     spaces = 9

#     for row in range(3):
#         for column in range(3):
#             if btns[row][column]['text'] != "":
#                 spaces -= 1

#     if spaces == 0:
#         return False
#     else:
#         return True

# def new_game():
    
#     global player

#     player = random.choice(players)

#     label.config(text = player + " turn")

#     for row in range(3):
#         for column in range(3):
#             btns[row][column].config(text = "", bg = "#F0F0F0")

# window = Tk()
# window.title("TIC-TAC-TOE")
# players = ["x", "o"]
# player = random.choice(players)
# btns = [[0,0,0], 
#         [0,0,0], 
#         [0,0,0]]
# label = Label(text = player + " turn", font = ("Roboto", 40))
# label.pack(side = "top")

# reset_btn = Button(text = "restart", font=('Roboto', 20), command = new_game)
# reset_btn.pack(side = "top")

# frame = Frame(window)
# frame.pack()

# for row in range(3):
#     for column in range(3):
#         btns[row][column] = Button(frame, text = '', font = ("Roboto", 40), width = 5, height = 2,
#         command = lambda row = row, column = column: next_move(row, column))

#         btns[row][column].grid(row = row, column = column)


# window.mainloop()
#---------
# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#Solution
# def compress(original):
#     results = ""
#     current_run_character = ""
#     run_length = 0

#     for i in range(len(original)):
#         if i == 0:
#             current_run_character = original[i]
#             run_length = 1
#         else:
#             current_char = original[i]
#             if current_char == current_run_character:
#                 run_length += 1
#             else:
#                 results += current_run_character + str(run_length)
#                 current_run_character = current_char
#                 run_length = 1
#     results += current_run_character + str(run_length)     
#     return results

# def decompress(compressed_text):
#     results = ""

#     for i in range(0, len(compressed_text), 2):
#         character = compressed_text[i]
#         run_length = int(compressed_text[i+1])

#         for j in range(run_length):
#             results += character
#     return results


# with open('./in.txt') as file1:
#     original_text = file1.read()
# print("Original text: " + original_text)
# print("")
# #compression
# print("Compressing...")

# file2 = open(r"./out.txt", 'w')

# compressed_text = compress(original_text)
# print("Compressed text: " + compressed_text)
# print("")
# file2.writelines(f'Compressed text: {compressed_text}\n')

# print("Decompressing...")

# decompressed_text = decompress(compressed_text)
# print("Decompressed: " + decompressed_text)
# print("")
# file2.writelines(f'Decompressed text: {decompressed_text}')
#---------
