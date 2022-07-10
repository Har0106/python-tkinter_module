from tkinter import *

root = Tk()
root.title('MP3 Player')

def play_pause():
    if mid.cget('text') == u"\u25B6":
        mid.configure(text=u'\u23F8')
    else:
        mid.configure(text=u"\u25B6")

listboxes = Listbox(root, width=40, font='Arial 15')
listboxes.grid(row=0, column=0, columnspan=3, padx=25, pady=(20, 15))

Button(root, text=u'\u23EE', font='Arial 20', bd=0).grid(row=1, column=0, pady=(0, 10), sticky='e')
mid = Button(root, text=u"\u25B6", font='Arial 20', bd=0, command=play_pause)
mid.grid(row=1, column=1, pady=(0, 10))
Button(root, text=u'\u23ED', font='Arial 20', bd=0).grid(row=1, column=2, pady=(0, 10), sticky='w')

menu = Menu(root)
root.config(menu=menu)

add = Menu(menu)
menu.add_cascade(label='Add', menu=add)
add.add_command(label='One Song')
add.add_command(label='Many Songs')

remove = Menu(menu)
menu.add_cascade(label='Remove', menu=remove)
remove.add_command(label='One Song')
remove.add_command(label='Many Songs')

root.mainloop()