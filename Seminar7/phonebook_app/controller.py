#functions
import csv
from random import randint


def add_data(i):
    with open('./python_class/Seminar7/phonebook_app/data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)

def view():
    data = []
    with open('./python_class/Seminar7/phonebook_app/data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def remove(i):
    def save(j):
         with open('./python_class/Seminar7/phonebook_app/data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j) 

    new_lst = []
    Tele = i
    with open('./python_class/Seminar7/phonebook_app/data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_lst.append(row)
            
        for element in row:
            if element == Tele:
                new_lst.remove(row)
    save(new_lst)

def update(i):
    def update_newlst(j):
        with open('./python_class/Seminar7/phonebook_app/data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(j)
    new_lst = []
    tele = i[0]

    with open('./python_class/Seminar7/phonebook_app/data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_lst.append(row)
            for element in row:
                if element == tele:
                    id = i[1]
                    name = i[2]
                    tele = i[3]
                    mail = i[4] 
                    id = randint(1,1000)
                    data = [id, name, tele, mail]
                    index = new_lst.index(row)
                    new_lst[index] = data
            for elements in id:
                if elements == id:
                    print('This ID is already taken!')
    update_newlst(data)    