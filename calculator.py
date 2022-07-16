from tkinter import *

class Calculator():
    def app(self):
        # Creating the gui of the app
        self.root = Tk()
        self.root.title('Calculator')

        # Design
        self.entry = Entry(self.root, justify='right', font="Calibri 25", width=16)
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        Button(self.root, text='C', font="Calibri 13", width=7, command=self.clear).grid(row=1,column=0)
        Button(self.root, text='BS', font="Calibri 13", width=7, command=self.back).grid(row=1,column=1)
        Button(self.root, text='(', font="Calibri 13", width=7, command=lambda: self.chars('(')).grid(row=1,column=2)
        Button(self.root, text=')', font="Calibri 13", width=7, command=lambda: self.chars(')')).grid(row=1,column=3)

        Button(self.root, text='7', font="Calibri 13", width=7, command=lambda: self.chars('7')).grid(row=2,column=0)
        Button(self.root, text='8', font="Calibri 13", width=7, command=lambda: self.chars('8')).grid(row=2,column=1)
        Button(self.root, text='9', font="Calibri 13", width=7, command=lambda: self.chars('9')).grid(row=2,column=2)
        Button(self.root, text='÷', font="Calibri 13", width=7, command=lambda: self.chars('÷')).grid(row=2,column=3)

        Button(self.root, text='4', font="Calibri 13", width=7, command=lambda: self.chars('4')).grid(row=3,column=0)
        Button(self.root, text='5', font="Calibri 13", width=7, command=lambda: self.chars('5')).grid(row=3,column=1)
        Button(self.root, text='6', font="Calibri 13", width=7, command=lambda: self.chars('6')).grid(row=3,column=2)
        Button(self.root, text='x', font="Calibri 13", width=7, command=lambda: self.chars('x')).grid(row=3,column=3)

        Button(self.root, text='1', font="Calibri 13", width=7, command=lambda: self.chars('1')).grid(row=4,column=0)
        Button(self.root, text='2', font="Calibri 13", width=7, command=lambda: self.chars('2')).grid(row=4,column=1)
        Button(self.root, text='3', font="Calibri 13", width=7, command=lambda: self.chars('3')).grid(row=4,column=2)
        Button(self.root, text='-', font="Calibri 13", width=7, command=lambda: self.chars('-')).grid(row=4,column=3)

        Button(self.root, text='x²', font="Calibri 13", width=7, command=lambda: self.chars('^2')).grid(row=5,column=0)
        Button(self.root, text='0', font="Calibri 13", width=7, command=lambda: self.chars('0')).grid(row=5,column=1)
        Button(self.root, text='.', font="Calibri 13", width=7, command=lambda: self.chars('.')).grid(row=5,column=2)
        Button(self.root, text='+', font="Calibri 13", width=7, command=lambda: self.chars('+')).grid(row=5,column=3)

        Button(self.root, text='√', font="Calibri 13", width=7, command=lambda: self.chars('√(')).grid(row=6,column=0)
        Button(self.root, text='1/x', font="Calibri 13", width=7, command=lambda: self.chars('(1/')).grid(row=6,column=1)
        Button(self.root, text='%', font="Calibri 13", width=7, command=lambda: self.chars('%')).grid(row=6,column=2)
        self.button_c = Button(self.root, text='=', font="Calibri 13", width=7, command=self.equal, state='disabled', bg='#808080')
        self.button_c.grid(row=6,column=3)

        self.root.mainloop()

    def disable(self, get):
        # to do the calculation
        s = get.replace('÷', '/')
        s = s.replace('x', '*')
        s = s.replace('^', '**')
        s = s.replace('%', '/100')
        if s != s.replace('√(', '('):
            s = s.replace('√(', '(')
            s = s.replace(')', '**(1/2))')
        try:
            self.answer = eval(s)
        # to disable and enable equal button
        except:
            self.button_c['state'] = DISABLED
        else:
            self.button_c['state'] = NORMAL

    # to clear the scree of calculator
    def clear(self):
        self.entry.delete(0, END)

    # to delete the last entered character
    def back(self):
        get = ''.join(list(self.entry.get())[:-1])
        self.disable(get)
        self.entry.delete(0, END)
        self.entry.insert(0, get)

    # to put the entered characters to the screen
    def chars(self, char):
        if (char in ['0', '÷', 'x', '+', '%', '^2', ')']) and len(self.entry.get()) == 0:
            char = ''
        get = self.entry.get() + char
        self.disable(get)
        self.entry.delete(0, END)
        self.entry.insert(0, get)

    # to put the answer of calculation to the screen
    def equal(self):
        self.entry.delete(0, END)
        self.entry.insert(0, self.answer)

Calculator().app()