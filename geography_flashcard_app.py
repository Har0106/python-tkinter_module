from operator import index
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
        text = f'Incorrect!'
    label.configure(text=text)

def hide_frames():
    for widget in state_frame.winfo_children():
        widget.destroy()
    for widget in state_capitals_frame.winfo_children():
        widget.destroy()
    state_frame.pack_forget()
    state_capitals_frame.pack_forget()

def random_state(frame):
    global state
    global image
    global ind

    states_list = ['alaska', 'arizona', 'california', 'colorado', 'florida', 'hawaii', 'massachusetts', 'michigan', 'montana', 'new_jersey', 'ohio', 'pennsylvania', 'texas', 'virginia', 'washington']
    state = random.choice(states_list)
    ind = states_list.index(state)
    image = ImageTk.PhotoImage(Image.open(f'states/{state}.jpg').resize((250, 250)))
    Label(frame, image=image).grid(row=0, column=0, pady=20, padx=100, columnspan=2)

def states():
    hide_frames()
    state_frame.pack(fill='both', expand=1)
    random_state(state_frame)

    global entry
    entry = Entry(state_frame, font='Arial 15')
    entry.grid(pady=10, row=1, column=0, columnspan=2)

    Button(state_frame, text='Submit', font='Arial 13', command=answer).grid(pady=10, row=2, column=0, sticky='e', padx=5)
    Button(state_frame, text='Next', font='Arial 13', command=states).grid(pady=10, row=2, column=1, sticky='w', padx=5)

    global label
    label = Label(state_frame, text='', font='Arial 15', width=16)
    label.grid(pady=10, row=3, column=0, columnspan=2)

def state_capitals():
    hide_frames()
    state_capitals_frame.pack(fill='both', expand=1)
    random_state(state_capitals_frame)
    state_capitals_list = ['Juneau', 'Phoenix', 'Sacramento', 'Denver', 'Tallahassee', 'Honolulu', 'Boston', 'Lansing', 'Helena', 'Trenton', 'Columbus', 'Harrisburg', 'Austin', 'Richmond', 'Olympia']
    capital = state_capitals_list[ind]

    first_two = [i for i in random.sample(state_capitals_list, k=3) if i != capital]
    if len(first_two) == 3:
        first_two = first_two[:-1]
    choices = random.sample(first_two + [capital], k=3), capital

menu = Menu(root)
root.config(menu=menu)

state = Menu(menu)
menu.add_cascade(label='State', menu=state)
state.add_command(label='States', command=states)
state.add_command(label='State Capitals', command=state_capitals)

state_frame = Frame(root)
state_capitals_frame = Frame(root)

root.mainloop()