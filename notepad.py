from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Untiled - Notepad')

frame = Frame(root)
frame.pack()

def new():
    text.delete(1.0, END)
    root.title('Untiled - Notepad')

def open_file():
    file_name = filedialog.askopenfilename(filetypes=(('Python Files', '*.py'), ('Text Files', '*.txt'), ('All Files', '*.*')))
    text.delete(1.0, END)
    name = file_name.split('/')[-1]
    root.title(f'{name} - Notepad')
    with open(file_name, 'r') as file:
        text.insert(END, file.read())

def save_as():
    file_name = filedialog.asksaveasfilename(filetypes=(('Python Files', '*.py'), ('Text Files', '*.txt'), ('All Files', '*.*')))
    name = file_name.split('/')[-1]
    root.title(f'{name} - Notepad')
    with open(file_name, 'w') as file:
        file.write(text.get(1.0, END))

text_scroll = Scrollbar(frame)
text_scroll.pack(fill='y', side='right')
text = Text(frame, font='Consolas 15', undo=True, yscrollcommand=text_scroll.set, height=25, width=82)
text.pack()
text_scroll.configure(command=text.yview)

menu = Menu(frame)
root.configure(menu=menu)

file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new)
file_menu.add_separator()
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Close')
file_menu.add_separator()
file_menu.add_command(label='Save')
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)

edit_menu = Menu(menu, tearoff=False)
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Undo')
edit_menu.add_command(label='Redo')
edit_menu.add_separator()
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')

root.mainloop()