from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class Notepad():
    def app(self):
        # Creating the gui window
        self.root = Tk()
        self.root.title('Untitled - Notepad')

        self.cut_copy = None
        self.file_name = None

        # Design of the notepad

        # Main frame of the notepad
        frame = Frame(self.root)
        frame.pack()

        # Horizontal and vertical scrollbar for the text widget
        text_scroll_y = Scrollbar(frame)
        text_scroll_x = Scrollbar(frame, orient='horizontal')
        text_scroll_y.pack(fill='y', side='right')
        text_scroll_x.pack(fill='x', side='bottom')
        self.text = Text(frame, font='Consolas 15', undo=True, yscrollcommand=text_scroll_y.set, xscrollcommand=text_scroll_x.set, height=22, width=82, selectbackground='black', selectforeground='white', wrap='none')
        self.text.pack()
        text_scroll_y.configure(command=self.text.yview) 
        text_scroll_x.configure(command=self.text.xview)

        # Status bar
        self.status = 'Unsaved'
        self.status_bar = Label(self.root, text='', relief='groove', anchor='e', bg='#808080')
        self.status_bar.pack(fill='x', side='bottom')

        # Main menu of the notepad
        menu = Menu(frame)
        self.root.configure(menu=menu)

        # To create new file, open an existing file, save a file in another name and save the changes to a file 
        self.file_menu = Menu(menu, tearoff=False, fg='black')
        menu.add_cascade(label='File', menu=self.file_menu)
        self.file_menu.add_command(label='New', accelerator='Ctrl+N', command=lambda: self.new(None))
        self.root.bind('<Control-n>', self.new)
        self.file_menu.add_command(label='Open', accelerator='Ctrl+O', command=lambda: self.open_file(None))
        self.root.bind('<Control-o>', self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Save', accelerator='Ctrl+S', command=lambda: self.save(None))
        self.root.bind('<Control-s>', self.save)
        self.file_menu.add_command(label='Save As        ', accelerator='Ctrl+Shift+S', command=lambda: self.save_as(None))
        self.root.bind('<Control-Shift-S>', self.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.root.destroy)

        # Cut, copy and paste text and redo or undo the changes made to a file
        self.edit_menu = Menu(menu, tearoff=False, fg='black')
        menu.add_cascade(label='Edit', menu=self.edit_menu)
        self.edit_menu.add_command(label='Undo       ', accelerator='Ctrl+Z')
        self.edit_menu.add_command(label='Redo', accelerator='Ctrl+Y')
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='Cut', accelerator='Ctrl+X', command=lambda: self.cut(None))
        self.root.bind('<Control-x>', self.cut)
        self.edit_menu.add_command(label='Copy', accelerator='Ctrl+C', command=lambda: self.copy(None))
        self.root.bind('<Control-c>', self.copy)
        self.edit_menu.add_command(label='Paste', accelerator='Ctrl+V', command=lambda: self.paste(None))
        self.root.bind('<Control-v>', self.paste)

        # Select all the text from the notepad
        self.selection_menu = Menu(menu, tearoff=False, fg='black')
        menu.add_cascade(label='Selection', menu=self.selection_menu)
        self.selection_menu.add_command(label='Select All       ', accelerator='Ctrl+A', command=self.select_all)

        # Switch from light mode to dark mode and vice versa
        self.view_menu = Menu(menu, tearoff=False, fg='black')
        menu.add_cascade(label='View', menu=self.view_menu)
        self.view_menu.add_command(label='Dark Mode       ', accelerator='Ctrl+Alt+D', command=lambda: self.dark_mode(None))
        self.root.bind('<Control-Alt-d>', self.dark_mode)
        self.view_menu.add_command(label='Light Mode       ', accelerator='Ctrl+Alt+L', command=lambda: self.light_mode(None))
        self.root.bind('<Control-Alt-l>', self.light_mode)

        # About the notepad
        self.help_menu = Menu(menu, tearoff=False, fg='black')
        menu.add_cascade(label='Help', menu=self.help_menu)
        self.help_menu.add_command(label='About       ', command=lambda:messagebox.showinfo('About', 'Notepad by Har0106'))

        self.refresh_status()
        self.root.mainloop()

    # Opening a new file
    def new(self, event):
        self.text.delete(1.0, END)
        self.root.title('Untitled - Notepad')

    # Opening an existing file
    def open_file(self, event):
        self.file_name = filedialog.askopenfilename(filetypes=(('Python Files', '*.py'), ('Text Files', '*.txt'), ('All Files', '*.*')))
        if self.file_name:
            self.text.delete(1.0, END)
            name = self.file_name.split('/')[-1]
            self.root.title(f'{name} - Notepad')
            with open(self.file_name, 'r') as file:
                self.text.insert(END, file.read())

    # Save the file with a new name
    def save_as(self, event):
        self.file_name = filedialog.asksaveasfilename(filetypes=(('Python Files', '*.py'), ('Text Files', '*.txt'), ('All Files', '*.*')))
        if self.file_name:
            name = self.file_name.split('/')[-1]
            self.root.title(f'{name} - Notepad')
            with open(self.file_name, 'w') as file:
                file.write(self.text.get(1.0, END)[:-1])

    # Save the changes made to the opened file
    def save(self, event):
        if self.root.title() == 'Untitled - Notepad':
            self.save_as(None)
        else:
            with open(self.file_name, 'w') as file:
                file.write(self.text.get(1.0, END)[:-1])

    # Cut the selected text
    def cut(self, event):
        if event:
            self.cut_copy = self.root.clipboard_get()
        elif self.text.selection_get():
            self.cut_copy = self.text.selection_get()
            self.root.clipboard_clear()
            self.root.clipboard_append(self.cut_copy)
            self.text.delete('sel.first', 'sel.last')

    # Copy the selected text to the clipboard
    def copy(self, event):
        if event:
            self.cut_copy = self.root.clipboard_get()
        elif self.text.selection_get():
            cut_copy = self.text.selection_get()
            self.root.clipboard_clear()
            self.root.clipboard_append(self.cut_copy)

    # Paste the text in the clipboard whereever the curser is
    def paste(self, event):
        if event:
            self.cut_copy = self.root.clipboard_get()
        elif self.cut_copy:
            pos = self.text.index(INSERT)
            self.text.insert(pos, self.cut_copy)

    # Select all the text in the notepad
    def select_all(self):
        self.text.tag_add('sel', '1.0', 'end')

    # Change white widgets to black
    def dark_mode(self, event):
        self.text.configure(bg='#1f1d1d', fg='white', insertbackground='white', selectbackground='white', selectforeground='black')
        self.file_menu.configure(bg='#1f1d1d', fg='white')
        self.edit_menu.configure(bg='#1f1d1d', fg='white')
        self.selection_menu.configure(bg='#1f1d1d', fg='white')
        self.view_menu.configure(bg='#1f1d1d', fg='white')
        self.help_menu.configure(bg='#1f1d1d', fg='white')

    # Change black widgets to white
    def light_mode(self, event):
        self.text.configure(bg='white', fg='black', insertbackground='black', selectbackground='black', selectforeground='white')
        self.file_menu.configure(bg='SystemButtonFace', fg='black')
        self.edit_menu.configure(bg='SystemButtonFace', fg='black')
        self.selection_menu.configure(bg='SystemButtonFace', fg='black')
        self.view_menu.configure(bg='SystemButtonFace', fg='black')
        self.help_menu.configure(bg='SystemButtonFace', fg='black')

    # Updating the status bar as the user types something in
    def refresh_status(self):
        row, column = self.text.index(INSERT).split('.')
        if self.file_name:
            with open(self.file_name, 'r') as file:
                if file.read() == self.text.get(1.0, 'end-1c'):
                    self.status = 'Saved'
                else:
                    self.status = 'Unsaved'
        self.status_bar.configure(text=f'Ln {row}, Col {column}     {self.status}       ')
        self.root.after(1000, self.refresh_status)

Notepad().app()