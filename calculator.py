from tkinter import *

root = Tk()
root.title('Calculator')

entry = Entry(root, justify='right', font="Calibri 25")
entry.grid(row=0, column=0, columnspan=4)
entry.focus_force()

def clear():
    entry.delete(0, END)

def chars(char):
    get = entry.get()
    entry.delete(0, END)
    entry.insert(0, get+char)

def equal():
    get = entry.get()
    get = get.replace('÷', '/')
    get = get.replace('x', '*')
    get = get.replace('^', '**')
    try:
        answer = eval(get)
        entry.delete(0, END)
        entry.insert(0, answer)
    except:
        state = DISABLED

button_c = Button(root, text='C', font="Calibri 13", width=8, bg='#65fe08', command=clear).grid(row=1,column=0)
button_bracket1 = Button(root, text='(', font="Calibri 13", width=8, command=lambda: chars('(')).grid(row=1,column=1)
button_bracket2 = Button(root, text=')', font="Calibri 13", width=8, command=lambda: chars(')')).grid(row=1,column=2)
button_divide = Button(root, text='÷', font="Calibri 13", width=8, command=lambda: chars('÷')).grid(row=1,column=3)

button_7 = Button(root, text='7', font="Calibri 13", width=8, command=lambda: chars('7')).grid(row=2,column=0)
button_8 = Button(root, text='8', font="Calibri 13", width=8, command=lambda: chars('8')).grid(row=2,column=1)
button_9 = Button(root, text='9', font="Calibri 13", width=8, command=lambda: chars('9')).grid(row=2,column=2)
button_multiply = Button(root, text='x', font="Calibri 13", width=8, command=lambda: chars('x')).grid(row=2,column=3)

button_4 = Button(root, text='4', font="Calibri 13", width=8, command=lambda: chars('4')).grid(row=3,column=0)
button_5 = Button(root, text='5', font="Calibri 13", width=8, command=lambda: chars('5')).grid(row=3,column=1)
button_6 = Button(root, text='6', font="Calibri 13", width=8, command=lambda: chars('6')).grid(row=3,column=2)
button_subtract = Button(root, text='-', font="Calibri 13", width=8, command=lambda: chars('-')).grid(row=3,column=3)

button_1 = Button(root, text='1', font="Calibri 13", width=8, command=lambda: chars('1')).grid(row=4,column=0)
button_2 = Button(root, text='2', font="Calibri 13", width=8, command=lambda: chars('2')).grid(row=4,column=1)
button_3 = Button(root, text='3', font="Calibri 13", width=8, command=lambda: chars('3')).grid(row=4,column=2)
button_add = Button(root, text='+', font="Calibri 13", width=8, command=lambda: chars('+')).grid(row=4,column=3)

button_power = Button(root, text='x²', font="Calibri 13", width=8, command=lambda: chars('^2')).grid(row=5,column=0)
button_0 = Button(root, text='0', font="Calibri 13", width=8, command=lambda: chars('0')).grid(row=5,column=1)
button_decimal = Button(root, text='.', font="Calibri 13", width=8, command=lambda: chars('.')).grid(row=5,column=2)
button_equal = Button(root, text='=', font="Calibri 13", width=8, command=equal).grid(row=5,column=3)

root.mainloop()