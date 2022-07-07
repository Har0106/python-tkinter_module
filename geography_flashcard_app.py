from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Geography Flash Card')
root.geometry('550x550')

def hide_frames():
    for widget in state_frame.winfo_children():
        widget.destroy()
    for widget in state_capitals_frame.winfo_children():
        widget.destroy()
    state_frame.pack_forget()
    state_capitals_frame.pack_forget()

def states():
    hide_frames()
    state_frame.pack(fill='both', expand=1)

def state_capitals():
    hide_frames()
    state_capitals_frame.pack(fill='both', expand=1)

menu = Menu(root)
root.config(menu=menu)

state = Menu(menu)
menu.add_cascade(label='State', menu=state)
state.add_command(label='States', command=states)
state.add_command(label='State Capitals', command=state_capitals)

state_frame = Frame(root, width=550, height=550)
state_capitals_frame = Frame(root, width=550, height=550)

root.mainloop()