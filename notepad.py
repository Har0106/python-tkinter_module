from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Untitled - Notepad')

frame = Frame(root)
frame.pack()

cut_copy = None

def new(event):
    text.delete(1.0, END)
    root.title('Untitled - Notepad')
    status_bar.configure(text='Unsaved    ')

def open_file(event):
    global file_name
    file_name = filedialog.askopenfilename(filetypes=(('Python Files', '*.py'), ('Text Files', '*.txt'), ('All Files', '*.*')))
    text.delete(1.0, END)
    name = file_name.split('/')[-1]
    if name != '':
        root.title(f'{name} - Notepad')
        with open(file_name, 'r') as file:
            text.insert(END, file.read())
            status_bar.configure(text='Saved    ')

def save_as(event):
    global file_name
    file_name = filedialog.asksaveasfilename(filetypes=(('Python Files', '*.py'), ('Text Files', '*.txt'), ('All Files', '*.*')))
    name = file_name.split('/')[-1]
    root.title(f'{name} - Notepad')
    with open(file_name, 'w') as file:
        file.write(text.get(1.0, END))
    status_bar.configure(text='Saved    ')

def save(event):
    if root.title() == 'Untitled - Notepad':
        save_as()
    else:
        with open(file_name, 'w') as file:
            file.write(text.get(1.0, END))
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
    if text.selection_get():
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

text_scroll = Scrollbar(frame)
text_scroll.pack(fill='y', side='right')
text = Text(frame, font='Consolas 15', undo=True, yscrollcommand=text_scroll.set, height=25, width=82, selectbackground='black', selectforeground='white')
text.pack()
text_scroll.configure(command=text.yview)

status_bar = Label(frame, text='Unsaved    ', relief='groove', anchor='e')
status_bar.pack(fill='x', side='bottom')

menu = Menu(frame)
root.configure(menu=menu)

file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', accelerator='Ctrl+N', command=lambda: new(None))
root.bind('<Control-n>', new)
file_menu.add_command(label='Open', accelerator='Ctrl+C', command=lambda: open_file(None))
root.bind('<Control-o>', open_file)
file_menu.add_separator()
file_menu.add_command(label='Save', accelerator='Ctrl+S', command=lambda: save(None))
root.bind('<Control-s>', save)
file_menu.add_command(label='Save As', accelerator='Ctrl+Shift+S', command=lambda: save_as(None))
root.bind('<Control-Shift-S>', save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)

edit_menu = Menu(menu, tearoff=False)
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Undo')
edit_menu.add_command(label='Redo')
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', command=lambda: cut(None))
root.bind('<Control-x>', cut)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', command=lambda: copy(None))
root.bind('<Control-c>', copy)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', command=lambda: paste(None))
root.bind('<Control-v>', paste)

root.mainloop()
