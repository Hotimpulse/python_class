from distutils.ccompiler import new_compiler
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import tkinter as tk
from controller import *
import pandas as pd
import json, os

#colors
FIRST_COL = '#000000'
MAIN_BG = '#ffffff'
THIRD_COL = '#fD293E'

window = Tk()
window.title('Hot Line Bling')
window.geometry('510x530')
window.configure(background = MAIN_BG)
window.resizable(height = False, width = False)

#frames

frame_top = Frame(window, width = 510, height = 50, bg = THIRD_COL)
frame_top.grid(row=0, column=0, padx=0, pady=1)

frame_middle = Frame(window, width = 510, height = 250, bg = THIRD_COL)
frame_middle.grid(row=1, column=0, padx=0, pady=1)

frame_bottom = Frame(window, width = 510, height = 300, bg = THIRD_COL, relief="flat")
frame_bottom.grid(row=2, column=0, padx=0, pady=1, sticky=NW)

#data

def show_data():
    global tree

    list_data = ['ID', 'Name', 'Telephone #', 'Email']

    tree = ttk.Treeview(frame_bottom, selectmode="extended", columns=list_data, show="headings")
    
    vert_scroll = ttk.Scrollbar(frame_bottom, orient="vertical", command=tree.yview)
    hor_scroll = ttk.Scrollbar(frame_bottom, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vert_scroll.set, xscrollcommand=hor_scroll.set)

    tree.grid(column=0, row=0, sticky="nsew")
    vert_scroll.grid(column=1, row=0, sticky="ns")
    hor_scroll.grid(column=0, row=1, sticky="ew")

    #header

    tree.heading(0, text="ID", anchor=NW)
    tree.heading(1, text="Name", anchor=NW)
    tree.heading(2, text="Tele #", anchor=NW)
    tree.heading(3, text="Email", anchor=NW)

    #columns

    tree.column(0, width=30, anchor=NW)
    tree.column(1, width=120, anchor=NW)
    tree.column(2, width=190, anchor=NW)
    tree.column(3, width=160, anchor=NW)

    demo_lst = view()

    for item in demo_lst:
        tree.insert("", "end", values=item)
        
show_data()

#import csvs
def openfile():
    output_file = open('./python_class/Seminar7/phonebook_app/data.csv', "a", newline='')

    file = filedialog.askopenfilename()
    with open(f"{file}", "r", newline='') as some_file:
        if os.path.splitext(file)[1] == ".csv":
            output_file.write(some_file.read())
        if os.path.splitext(file)[1] == ".json":
            json_obj = pd.read_json(some_file, orient='index')
            csvData = json_obj.to_csv(output_file, index=None)
            for row in csvData:
                if row == 'ID,Name,Tele,Email':
                    row.pop()
                    # row.append(csvData, mode='a')
    show_data()
    output_file.close
    some_file.close

#import jsons

# def load_json():
#     output_file = open('./python_class/Seminar7/phonebook_app/data.csv')
#     file = filedialog.askopenfilename()
#     with open(f'{file}', "w") as json_file:
#         if os.path.splitext(file)[1] == ".json":
            
#         # json_data = json.loads(json_file)
#         # for item in json_data:
#         pdObj = pd.read_json(json_file, orient='index')
#         csvData = pdObj.to_csv(index=False)     

#     show_data()
#     output_file.close
#     json_file.close

#insertion of data

def insert():
    ID_num = entry_id.get()
    Name = entry_name.get()
    Tele = entry_tele.get()
    Email = entry_mail.get()

    data = [ID_num, Name, Tele, Email]

    if ID_num == '' or Name == '' or Tele == '' or Email == '':
        messagebox.showwarning('data', 'Please fill all fields')
    else:
        add_data(data)
        messagebox.showwarning('data', 'Data added!')

        entry_id.delete(0, 'end')
        entry_name.delete(0, 'end')
        entry_tele.delete(0, 'end')
        entry_mail.delete(0, 'end')
        
        show_data()

def to_update():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']

        ID_num = str(tree_list[0])
        Name = str(tree_list[1])
        Tele = str(tree_list[2])
        Email = str(tree_list[3])

        entry_id.insert(0, ID_num)
        entry_name.insert(0, Name)
        entry_tele.insert(0, Tele)
        entry_mail.insert(0, Email)
    
        def confirm():
            new_id = entry_id.get()
            new_name = entry_name.get()
            new_tele = entry_tele.get()
            new_mail = entry_mail.get()

            data = [new_tele, new_id, new_name, new_tele, new_mail]

            update(data)

            messagebox.showinfo('Success', 'Data updated')

            entry_id.delete(0, 'end')
            entry_name.delete(0, 'end')
            entry_tele.delete(0, 'end')
            entry_mail.delete(0, 'end')

            # for widget in frame_bottom.winfo_children():
            #     widget.destroy()
            
            btn_confirm.destroy()
            show_data()
        global btn_confirm
        btn_confirm = Button(frame_middle, border=0, width=4, text="Confirm", height=1, font = ('Roboto 14'), bg = THIRD_COL, fg=FIRST_COL, command=confirm)
        btn_confirm.place(x=435, y=60)

    except IndexError:
        messagebox.showerror('Error', 'Select something from the table')

def to_remove():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values'] 
        tree_tele = str(tree_list[2])
        remove(tree_tele)

        messagebox.showinfo('Success', 'Data deleted')

        # for widget in frame_middle.winfo_children():
        #     widget.destroy()
        show_data()
    except IndexError:
        messagebox.showerror('Error', 'Select something from the table') 

def clear():
    ID_num = entry_id.get()
    Name = entry_name.get()
    Tele = entry_tele.get()
    Email = entry_mail.get()

    if ID_num == '' or Name == '' or Tele == '' or Email == '':
        messagebox.showwarning('data', 'Please fill all fields')
    else:
        entry_id.delete(0, 'end')
        entry_name.delete(0, 'end')
        entry_tele.delete(0, 'end')
        entry_mail.delete(0, 'end')
        btn_confirm.destroy()
        
#title_and_widgets

app_name = Label(frame_top, text = "Phonebook", height = 1, font=('Roboto 25 bold'), bg = MAIN_BG, fg = FIRST_COL)
app_name.place(x=5, y=5)

#mid section

person_id = Label(frame_middle, text = "ID", height = 1, font = ('Roboto 14'), bg = MAIN_BG, fg = FIRST_COL, anchor = NW)
person_id.place(x=10, y=0)
entry_id = Entry(frame_middle, width = 25, justify= "left", highlightthickness=1, relief= "solid")
entry_id.place(x=80, y=0)

person_name = Label(frame_middle, text = "Name", height = 1, font = ('Roboto 14'), bg = MAIN_BG, fg = FIRST_COL, anchor = NW)
person_name.place(x=10, y=30)
entry_name = Entry(frame_middle, width = 25, justify= "left", highlightthickness=1, relief= "solid")
entry_name.place(x=80, y=30)

person_tele = Label(frame_middle, text = "Tele #", height = 1, font = ('Roboto 14'), bg = MAIN_BG, fg = FIRST_COL, anchor = NW)
person_tele.place(x=10, y=60)
entry_tele = Entry(frame_middle, width = 25, justify= "left", highlightthickness=1, relief= "solid")
entry_tele.place(x=80, y=60)

person_mail = Label(frame_middle, text = "E-mail", height = 1, font = ('Roboto 14'), bg = MAIN_BG, fg = FIRST_COL, anchor = NW)
person_mail.place(x=10, y=90)
entry_mail = Entry(frame_middle, width = 25, justify= "left", highlightthickness=1, relief= "solid")
entry_mail.place(x=80, y=90)

#btns

btn_import = Button(frame_middle, border=0, text = "Import", height=1, justify="center", font = ('Roboto 14'), bg = MAIN_BG, fg=FIRST_COL, command=openfile)
btn_import.place(x=350, y=0)

btn_add = Button(frame_middle, border=0, text = "Add", height=1, justify="center", font = ('Roboto 14'), bg = MAIN_BG, fg=FIRST_COL, command=insert)
btn_add.place(x=350, y=30)

btn_update = Button(frame_middle, border=0, text = "Update", height=1, justify="center", font = ('Roboto 14'), bg = MAIN_BG, fg=FIRST_COL, command=to_update)
btn_update.place(x=350, y=60)

btn_delete = Button(frame_middle, border=0, text = "Delete", height=1, justify="center", font = ('Roboto 14'), bg = THIRD_COL, fg=FIRST_COL, command=to_remove)
btn_delete.place(x=350, y=90)

btn_clear = Button(frame_middle, border=0, text = "Clear", height=1, justify="center", font = ('Roboto 14'), bg = THIRD_COL, fg=FIRST_COL, command=clear)
btn_clear.place(x=350, y=130)

window.mainloop()