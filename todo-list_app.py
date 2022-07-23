from tkinter import *
from tkinter import messagebox

class ToDoList():
    def app(self):
        self.root = Tk()
        self.root.title('ToDo List App')
        self.root.configure(background='#ACDDDE')

        self.listbox = Listbox(self.root, width=30, height=10, font=('Comic Sans MS', 16), bg='#CAF1DE', highlightbackground='#170a45', highlightthickness=1)
        self.listbox.grid(row=0, column=0, columnspan=5, sticky='nesw')

        self.entry = Entry(self.root, font=('Comic Sans MS', 16), width=24)
        self.entry.grid(row=1, column=0, columnspan=4, pady=(10, 0), padx=(10, 0))
        button_add = Button(self.root, font=('Comic Sans MS', 13), text='Add', bd=0, command=lambda:self.add(0))
        button_add.grid(row=1, column=4, sticky='nesw', pady=(10,0), padx=10)

        button_remove = Button(self.root, text='Remove', font=('Comic Sans MS', 13), bd=0)
        button_remove.grid(row=2, column=0, sticky='nesw', pady=10, padx=(10, 5))
        button_remove = Button(self.root, text='Clear', font=('Comic Sans MS', 13), bd=0)
        button_remove.grid(row=2, column=1, sticky='nesw', pady=10, padx=(0, 5))
        button_remove = Button(self.root, text='Save', font=('Comic Sans MS', 13), bd=0)
        button_remove.grid(row=2, column=2, sticky='nesw', pady=10, padx=(0, 5))
        button_remove = Button(self.root, text='Save As', font=('Comic Sans MS', 13), bd=0)
        button_remove.grid(row=2, column=3, sticky='nesw', pady=10, padx=(0, 5))
        button_remove = Button(self.root, text='Open', font=('Comic Sans MS', 13), bd=0)
        button_remove.grid(row=2, column=4, sticky='nesw', pady=10, padx=(0, 10))

        self.root.bind('<Return>', self.add)

        self.root.mainloop()

    def add(self, e):
        if self.entry.get():
            self.listbox.insert(END, f'  {self.entry.get()}')
            self.entry.delete(0, END)
        else:
            messagebox.showinfo('Info', 'No Task Entered In!')

ToDoList().app()
