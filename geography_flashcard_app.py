from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title('Geography Flash Card')

def answer():
    answer = state.replace('_', ' ').title()
    if answer == entry.get().title():
        text = 'Correct!'
    else:
        text = f'Incorrect! And The Correct Answer is {answer}'
    label.configure(text=text)

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
    global state
    global image
    states = ['alaska', 'arizona', 'california', 'colorado', 'florida', 'hawaii', 'massachusetts', 'michigan', 'montana', 'new_jersey', 'ohio', 'pennsylvania', 'texas', 'virginia', 'washington']
    state = random.choice(states)
    image = ImageTk.PhotoImage(Image.open(f'states/{state}.jpg').resize((250, 250)))
    Label(state_frame, image=image).pack(pady=20, padx=150)

    global entry
    entry = Entry(state_frame, font='Arial 15')
    entry.pack(pady=10)

    Button(state_frame, text='Submit', font='Arial 13', command=answer).pack(pady=10)

    global label
    label = Label(state_frame, text='', font='Arial 15', width=50)
    label.pack(pady=10)

def state_capitals():
    hide_frames()
    state_capitals_frame.pack(fill='both', expand=1)

menu = Menu(root)
root.config(menu=menu)

state = Menu(menu)
menu.add_cascade(label='State', menu=state)
state.add_command(label='States', command=states)
state.add_command(label='State Capitals', command=state_capitals)

state_frame = Frame(root)
state_capitals_frame = Frame(root)

root.mainloop()