from tkinter import *

root = Tk()
root.title('Untiled - Notepad')

frame = Frame(root)
frame.pack()

def new():
    text.delete(1.0, END)
    root.title('Untiled - Notepad')

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
file_menu.add_command(label='Open')
file_menu.add_command(label='Close')
file_menu.add_separator()
file_menu.add_command(label='Save')
file_menu.add_command(label='Save As')
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