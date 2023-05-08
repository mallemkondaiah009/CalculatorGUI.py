from tkinter import *
mw = Tk()
mw.title("Calculator")

def clear():
    db.delete(0, END)

def button_click(num):
    cur_number = db.get()
    clear()
    final_number = cur_number + num
    db.insert(0, final_number)

first_num = 0
math = " "

def calc(math_type):
    global first_num, math
    math = math_type
    first_num = db.get()
    clear()


def Equal():
    result = " "
    second_num = db.get()
    clear()
    if math == "Add":
        result = int(first_num) + int(second_num)
    elif math == "Sub":
        result = int(first_num) - int(second_num)
    elif math == "Mul":
        result = int(first_num) * int(second_num)
    elif math == "Div":
        result = int(first_num) / int(second_num)
    db.insert(0, str(result))


# widget creation
db = Entry(mw, width=14, font=("Arial", 28), justify=RIGHT)

button_0 = Button(mw, text="0", padx=36, pady=10, font=("Arial", 14), command=lambda: button_click("0"))
button_1 = Button(mw, text="1", padx=36, pady=10, font=("Arial", 14), command=lambda: button_click("1"))
button_2 = Button(mw, text="2", padx=36, pady=10, font=("Arial", 14), command=lambda: button_click("2"))
button_3 = Button(mw, text="3", padx=36, pady=10, font=("Arial", 14), command=lambda: button_click("3"))
button_4 = Button(mw, text="4", padx=36, pady=10, font=("Arial", 14), command=lambda: button_click("4"))
button_5 = Button(mw, text="5", padx=36, pady=10, font=("Arial", 14), command=lambda: button_click("5"))
button_6 = Button(mw, text="6", padx=36, pady=10, font=("Arial", 14), command=lambda: button_click("6"))
button_7 = Button(mw, text="7", padx=36, pady=10, font=("Arial", 14), command=lambda: button_click("7"))
button_8 = Button(mw, text="8", padx=36, pady=10, font=("Arial", 14), command=lambda: button_click("8"))
button_9 = Button(mw, text="9", padx=36, pady=10, font=("Arial", 14), command=lambda: button_click("9"))

button_clear = Button(mw, text="clear", padx=74, pady=10, font=("Arial", 14), command=clear)
button_Div = Button(mw, text="/", padx=38, pady=10, font=("Arial", 14), command=lambda: calc("Div"))
button_Mul = Button(mw, text="*", padx=38, pady=10, font=("Arial", 14), command=lambda: calc("Mul"))
button_Add = Button(mw, text="+", padx=36, pady=10, font=("Arial", 14), command=lambda: calc("Add"))
button_Sub = Button(mw, text="-", padx=38, pady=10, font=("Arial", 14), command=lambda: calc("Sub"))
button_Equal = Button(mw, text="=", padx=36, pady=40, font=("Arial", 14), command=Equal)
# showing widgets
button_Equal.grid(row=5, column=2, rowspan=2, padx=2, pady=2)
button_Add.grid(row=6, column=1, padx=2, pady=2)
button_Sub.grid(row=6, column=0, padx=2, pady=2)
button_Div.grid(row=5, column=0, padx=2, pady=2)
button_Mul.grid(row=5, column=1, padx=2, pady=2)

button_clear.grid(row=4, column=1, columnspan=2, padx=2, pady=2)
button_0.grid(row=4, column=0, padx=2, pady=2)

button_1.grid(row=3, column=0, padx=2, pady=2)
button_2.grid(row=3, column=1, padx=2, pady=2)
button_3.grid(row=3, column=2, padx=2, pady=2)

button_4.grid(row=2, column=0, padx=2, pady=2)
button_5.grid(row=2, column=1, padx=2, pady=2)
button_6.grid(row=2, column=2, padx=2, pady=2)

button_7.grid(row=1, column=0, padx=2, pady=2)
button_8.grid(row=1, column=1, padx=2, pady=2)
button_9.grid(row=1, column=2, padx=2, pady=2)

db.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

mw.mainloop()
