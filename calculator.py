from tkinter import *

root = Tk()
root.title('Calculator')

entry = Entry(root, justify='right', font="Calibri 25", width=16)
entry.grid(row=0, column=0, columnspan=4, pady=10)

def disable(get):
    global answer

    # to do the calculation
    s = get.replace('÷', '/')
    s = s.replace('x', '*')
    s = s.replace('^', '**')
    s = s.replace('%', '/100')
    if s != s.replace('√(', '('):
        s = s.replace('√(', '(')
        s = s.replace(')', '**(1/2))')
    try:
        answer = eval(s)
    # to disable and enable equal button
    except:
        button_c['state'] = DISABLED
    else:
        button_c['state'] = NORMAL

# to clear the scree of calculator
def clear():
    entry.delete(0, END)

# to delete the last entered character
def back():
    get = ''.join(list(entry.get())[:-1])
    disable(get)
    entry.delete(0, END)
    entry.insert(0, get)

# to put the entered characters to the screen
def chars(char):
    if (char in ['0', '÷', 'x', '+', '%', '^2', ')']) and len(entry.get()) == 0:
        char = ''
    get = entry.get() + char
    disable(get)
    entry.delete(0, END)
    entry.insert(0, get)

# to put the answer of calculation to the screen
def equal():
    global answer
    entry.delete(0, END)
    entry.insert(0, answer)

# Design
Button(root, text='C', font="Calibri 13", width=7, command=clear).grid(row=1,column=0)
Button(root, text='B', font="Calibri 13", width=7, command=back).grid(row=1,column=1)
Button(root, text='(', font="Calibri 13", width=7, command=lambda: chars('(')).grid(row=1,column=2)
Button(root, text=')', font="Calibri 13", width=7, command=lambda: chars(')')).grid(row=1,column=3)

Button(root, text='7', font="Calibri 13", width=7, command=lambda: chars('7')).grid(row=2,column=0)
Button(root, text='8', font="Calibri 13", width=7, command=lambda: chars('8')).grid(row=2,column=1)
Button(root, text='9', font="Calibri 13", width=7, command=lambda: chars('9')).grid(row=2,column=2)
Button(root, text='÷', font="Calibri 13", width=7, command=lambda: chars('÷')).grid(row=2,column=3)

Button(root, text='4', font="Calibri 13", width=7, command=lambda: chars('4')).grid(row=3,column=0)
Button(root, text='5', font="Calibri 13", width=7, command=lambda: chars('5')).grid(row=3,column=1)
Button(root, text='6', font="Calibri 13", width=7, command=lambda: chars('6')).grid(row=3,column=2)
Button(root, text='x', font="Calibri 13", width=7, command=lambda: chars('x')).grid(row=3,column=3)

Button(root, text='1', font="Calibri 13", width=7, command=lambda: chars('1')).grid(row=4,column=0)
Button(root, text='2', font="Calibri 13", width=7, command=lambda: chars('2')).grid(row=4,column=1)
Button(root, text='3', font="Calibri 13", width=7, command=lambda: chars('3')).grid(row=4,column=2)
Button(root, text='-', font="Calibri 13", width=7, command=lambda: chars('-')).grid(row=4,column=3)

Button(root, text='x²', font="Calibri 13", width=7, command=lambda: chars('^2')).grid(row=5,column=0)
Button(root, text='0', font="Calibri 13", width=7, command=lambda: chars('0')).grid(row=5,column=1)
Button(root, text='.', font="Calibri 13", width=7, command=lambda: chars('.')).grid(row=5,column=2)
Button(root, text='+', font="Calibri 13", width=7, command=lambda: chars('+')).grid(row=5,column=3)

Button(root, text='√', font="Calibri 13", width=7, command=lambda: chars('√(')).grid(row=6,column=0)
Button(root, text='1/x', font="Calibri 13", width=7, command=lambda: chars('(1/')).grid(row=6,column=1)
Button(root, text='%', font="Calibri 13", width=7, command=lambda: chars('%')).grid(row=6,column=2)
button_c = Button(root, text='=', font="Calibri 13", width=7, command=equal, state='disabled', bg='#808080')
button_c.grid(row=6,column=3)

root.mainloop()