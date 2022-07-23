from tkinter import *
from tkinter import messagebox

class ToDoList():
    def app(self):
        # creating the main gui of the app
        self.root = Tk()
        self.root.title('ToDo List App')
        self.root.configure(bg='#E5E4E2')

        # listbox to save the tasks
        self.listbox = Listbox(self.root, width=30, height=10, font=('Comic Sans MS', 16), activestyle='none', selectbackground='black', selectforeground='white')
        self.listbox.grid(row=0, column=0, columnspan=5, sticky='nesw')

        # to add an item to the listbox
        self.entry = Entry(self.root, font=('Comic Sans MS', 16), width=24)
        self.entry.grid(row=1, column=0, columnspan=4, pady=(10, 0), padx=(10, 0))
        button_add = Button(self.root, font=('Comic Sans MS', 13), text='Add', bd=0, command=lambda:self.add(0))
        button_add.grid(row=1, column=4, sticky='nesw', pady=(10,0), padx=10)

        # to delete an item or all the items from the listbox
        button_remove = Button(self.root, text='Remove', font=('Comic Sans MS', 13),bd=0, command=self.remove)
        button_remove.grid(row=2, column=0, sticky='nesw', pady=10, padx=(10, 5))
        button_remove = Button(self.root, text='Clear', font=('Comic Sans MS', 13), bd=0, command=self.clear)
        button_remove.grid(row=2, column=1, sticky='nesw', pady=10, padx=(0, 5))

        # to save the list or open an existing list
        button_remove = Button(self.root, text='Save', font=('Comic Sans MS', 13), bd=0)
        button_remove.grid(row=2, column=2, sticky='nesw', pady=10, padx=(0, 5))
        button_remove = Button(self.root, text='Save As', font=('Comic Sans MS', 13), bd=0)
        button_remove.grid(row=2, column=3, sticky='nesw', pady=10, padx=(0, 5))
        button_remove = Button(self.root, text='Open', font=('Comic Sans MS', 13), bd=0)
        button_remove.grid(row=2, column=4, sticky='nesw', pady=10, padx=(0, 10))

        # bindings
        self.root.bind('<Return>', self.add)
        self.listbox.bind('<x>', self.done)

        self.root.mainloop()

    # adding items to the list box
    def add(self, e):
        if self.entry.get():
            if self.listbox.curselection():
                # add the item after the selected item
                self.listbox.insert(self.listbox.curselection()[0]+1, f' {self.entry.get()}')
            else:
                # add the item at the end
                self.listbox.insert(END, f' {self.entry.get()}')
            # clear the entry box
            self.entry.delete(0, END)
        else:
            # show messagebox when the entry box is empty
            messagebox.showinfo('Info', 'No Task Entered In!')
        
    def remove(self):
        # remove the selected item
        if self.listbox.curselection():
            self.listbox.delete(self.listbox.curselection())

    def done(self, e):
        # cross out an item
        if self.listbox.curselection():
            self.listbox.itemconfigure(self.listbox.curselection(), fg='#B2BEB5')
            self.listbox.selection_clear(self.listbox.curselection())

    def clear(self):
        # clear all the things in the listbox
        self.listbox.delete(0, END)

ToDoList().app()
