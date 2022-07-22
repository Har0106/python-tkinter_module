from tkinter import *

class ToDoList():
    def app(self):
        self.root = Tk()
        self.root.title('ToDo List App')
        self.root.configure(bg='black')

        self.frame = Frame(self.root, width=425,height=372, bg='white')
        self.frame.grid(row=0, column=0, columnspan=5)
        self.frame.grid_propagate(0)

        self.row = 0

        button_add = Button(self.root, font='Arial 20', text='+', bd=0, command=self.add, height=0)
        button_add.grid(row=1, column=0, pady=2, sticky='nesw', padx=(0, 1))
        button_remove = Button(self.root, font='Arial 20', text='-', bd=0)
        button_remove.grid(row=1, column=1, pady=2, sticky='nesw', padx=(1, 0))
        button_save = Button(self.root, font='Arial 20', text='💾', bd=0)
        button_save.grid(row=1, column=2, pady=2, sticky='nesw', padx=(1, 0))
        button_saveas = Button(self.root, font='Arial 20', text='💾', bd=0)
        button_saveas.grid(row=1, column=3, pady=2, sticky='nesw', padx=(1, 0))
        button_open = Button(self.root, font='Arial 20', text='📂', bd=0)
        button_open.grid(row=1, column=4, pady=2, sticky='nesw', padx=(1, 0))

        self.root.mainloop()

    def add(self):
        button = Button(self.frame, font='Arial 18 bold', text='□', bg='white', bd=0)
        button.grid(row=self.row, column=0)
        entry = Entry(self.frame, font=('Comic Sans MS', 18), width=400, bg='white', bd=0)
        entry.grid(row=self.row, column=1)
        self.row += 1

ToDoList().app()
