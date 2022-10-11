from tkinter import *
from controller import *
from tkinter.tix import Tree
from tkinter import ttk

FIRST_COL = '#000000'
MAIN_BG = '#ffffff'
THIRD_COL = '#fD293E'

window = Tk()
window.title('Hot Line Bling')
window.geometry('600x600')
window.configure(background = MAIN_BG)
window.resizable(height = False, width = False)


#frames

frame_top = Frame(window, width = 510, height = 50, bg = THIRD_COL)
frame_top.grid(row=0, column=0, padx=0, pady=1)

frame_middle = Frame(window, width = 510, height = 200, bg = THIRD_COL)
frame_middle.grid(row=1, column=0, padx=0, pady=1)

frame_bottom = Frame(window, width = 510, height = 250, bg = THIRD_COL, relief="flat")
frame_bottom.grid(row=2, column=0, columnspan=2, padx=0, pady=1, sticky=NW)

def show_data():
    global Tree

    list_data = ['ID', 'Name', 'Tele #', 'Email']

    demo_lst = [['1', 'Lev', '678', 'haha@gmail.com']]

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

    tree.column(0, width=20, anchor=NW)
    tree.column(1, width=120, anchor=NW)
    tree.column(2, width=200, anchor=NW)
    tree.column(3, width=160, anchor=NW)

    for item in demo_lst:
        tree.insert("", "end", values=item)
show_data()

#title

app_name = Label(frame_top, text = "Phonebook", height = 1, font=('Roboto 25 bold '), bg = MAIN_BG, fg = FIRST_COL)
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

btn_search = Button(frame_middle, border=0, text = "Search", height=1, justify="center", font = ('Roboto 14'), bg = MAIN_BG, fg=FIRST_COL)
btn_search.place(x=350, y=150)
entry_search = Entry(frame_middle, justify="center", highlightthickness=1, relief="solid", width=20)
entry_search.place(x=150, y=150)

btn_view = Button(frame_middle, border=0, text = "View", height=1, justify="center", font = ('Roboto 14'), bg = MAIN_BG, fg=FIRST_COL)
btn_view.place(x=350, y=15)

btn_add = Button(frame_middle, border=0, text = "Add", height=1, justify="center", font = ('Roboto 14'), bg = MAIN_BG, fg=FIRST_COL)
btn_add.place(x=350, y=45)

btn_update = Button(frame_middle, border=0, text = "Update", height=1, justify="center", font = ('Roboto 14'), bg = MAIN_BG, fg=FIRST_COL)
btn_update.place(x=350, y=75)

btn_delete = Button(frame_middle, border=0, text = "Delete", height=1, justify="center", font = ('Roboto 14'), bg = THIRD_COL, fg=FIRST_COL)
btn_delete.place(x=350, y=115)

window.mainloop()
