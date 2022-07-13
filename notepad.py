from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title('Untitled - Notepad')

cut_copy = None
file_name = None

def new(event):
    text.delete(1.0, END)
    root.title('Untitled - Notepad')
    status_bar.configure(text='Unsaved    ')

def open_file(event):
    global file_name
    file_name = filedialog.askopenfilename(filetypes=(('Python Files', '*.py'), ('Text Files', '*.txt'), ('All Files', '*.*')))
    if file_name:
        text.delete(1.0, END)
        name = file_name.split('/')[-1]
        root.title(f'{name} - Notepad')
        with open(file_name, 'r') as file:
            text.insert(END, file.read())
        status_bar.configure(text='Saved    ')

def save_as(event):
    global file_name
    file_name = filedialog.asksaveasfilename(filetypes=(('Python Files', '*.py'), ('Text Files', '*.txt'), ('All Files', '*.*')))
    if file_name:
        name = file_name.split('/')[-1]
        root.title(f'{name} - Notepad')
        with open(file_name, 'w') as file:
            file.write(text.get(1.0, END)[:-1])
        status_bar.configure(text='Saved    ')

def save(event):
    if root.title() == 'Untitled - Notepad':
        save_as(None)
    else:
        with open(file_name, 'w') as file:
            file.write(text.get(1.0, END)[:-1])
    status_bar.configure(text='Saved    ')

def cut(event):
    global cut_copy
    if event:
        cut_copy = root.clipboard_get()
    elif text.selection_get():
        cut_copy = text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(cut_copy)
        text.delete('sel.first', 'sel.last')

def copy(event):
    global cut_copy
    if event:
        cut_copy = root.clipboard_get()
    elif text.selection_get():
        cut_copy = text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(cut_copy)

def paste(event):
    global cut_copy
    if event:
        cut_copy = root.clipboard_get()
    elif cut_copy:
        pos = text.index(INSERT)
        text.insert(pos, cut_copy)

def select_all():
    text.tag_add('sel', '1.0', 'end')

def dark_mode(event):
    text.configure(bg='#1f1d1d', fg='white', insertbackground='white', selectbackground='white', selectforeground='black')
    file_menu.configure(bg='#1f1d1d', fg='white')
    edit_menu.configure(bg='#1f1d1d', fg='white')
    selection_menu.configure(bg='#1f1d1d', fg='white')
    view_menu.configure(bg='#1f1d1d', fg='white')
    help_menu.configure(bg='#1f1d1d', fg='white')

def light_mode(event):
    text.configure(bg='white', fg='black', insertbackground='black', selectbackground='black', selectforeground='white')
    file_menu.configure(bg='SystemButtonFace', fg='black')
    edit_menu.configure(bg='SystemButtonFace', fg='black')
    selection_menu.configure(bg='SystemButtonFace', fg='black')
    view_menu.configure(bg='SystemButtonFace', fg='black')
    help_menu.configure(bg='SystemButtonFace', fg='black')

def about():
    messagebox.showinfo('About', 'Notepad by Har0106')

def refresh_status():
    if file_name:
        with open(file_name, 'r') as file:
            if file.read() == text.get(1.0, 'end-1c'):
                status_bar.configure(text='Saved    ')
            else:
                status_bar.configure(text='Unsaved    ')
    root.after(1000, refresh_status)

frame = Frame(root)
frame.pack()

text_scroll_y = Scrollbar(frame)
text_scroll_x = Scrollbar(frame, orient='horizontal')
text_scroll_y.pack(fill='y', side='right')
text_scroll_x.pack(fill='x', side='bottom')
text = Text(frame, font='Consolas 15', undo=True, yscrollcommand=text_scroll_y.set, xscrollcommand=text_scroll_x.set, height=22, width=82, selectbackground='black', selectforeground='white', wrap='none')
text.pack()
text_scroll_y.configure(command=text.yview) 
text_scroll_x.configure(command=text.xview)

status_bar = Label(root, text='Unsaved    ', relief='groove', anchor='e', bg='#808080')
status_bar.pack(fill='x', side='bottom')

menu = Menu(frame)
root.configure(menu=menu)

file_menu = Menu(menu, tearoff=False, fg='black')
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', accelerator='Ctrl+N', command=lambda: new(None))
root.bind('<Control-n>', new)
file_menu.add_command(label='Open', accelerator='Ctrl+O', command=lambda: open_file(None))
root.bind('<Control-o>', open_file)
file_menu.add_separator()
file_menu.add_command(label='Save', accelerator='Ctrl+S', command=lambda: save(None))
root.bind('<Control-s>', save)
file_menu.add_command(label='Save As        ', accelerator='Ctrl+Shift+S', command=lambda: save_as(None))
root.bind('<Control-Shift-S>', save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)

edit_menu = Menu(menu, tearoff=False, fg='black')
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Undo       ', accelerator='Ctrl+Z')
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y')
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', command=lambda: cut(None))
root.bind('<Control-x>', cut)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', command=lambda: copy(None))
root.bind('<Control-c>', copy)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', command=lambda: paste(None))
root.bind('<Control-v>', paste)

selection_menu = Menu(menu, tearoff=False, fg='black')
menu.add_cascade(label='Selection', menu=selection_menu)
selection_menu.add_command(label='Select All       ', accelerator='Ctrl+A', command=select_all)

view_menu = Menu(menu, tearoff=False, fg='black')
menu.add_cascade(label='View', menu=view_menu)
view_menu.add_command(label='Dark Mode       ', accelerator='Ctrl+Alt+D', command=lambda: dark_mode(None))
root.bind('<Control-Alt-d>', dark_mode)
view_menu.add_command(label='Light Mode       ', accelerator='Ctrl+Alt+L', command=lambda: light_mode(None))
root.bind('<Control-Alt-l>', light_mode)

help_menu = Menu(menu, tearoff=False, fg='black')
menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About       ', command=about)

refresh_status()
root.mainloop()
