from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title('Geography Flash Card App')

global usa_image
global usa
global home_label
usa_image = ImageTk.PhotoImage(Image.open('states/USA.jpg'))
usa = Label(root, image=usa_image)
home_label = Label(root, text='Study The States of USA\nWith Geography Flash Card App', font='Arial 15', justify='center')
usa.pack()
home_label.pack(pady=20)

def state_answer():
    answer = state.replace('_', ' ').title()
    if answer == entry.get().title():
        text = 'Correct!'
    else:
        text = f'Incorrect!'
    state_label.configure(text=text)

def state_capitals_answer():
    if capital == choosed.get():
        text = 'Correct!'
    else:
        text = f'Incorrect!'
    state_capitals_label.configure(text=text)

def hide_frames():
    for widget in state_frame.winfo_children():
        widget.destroy()
    for widget in state_capitals_frame.winfo_children():
        widget.destroy()
    usa.pack_forget()
    home_label.pack_forget()
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

def home():
    hide_frames()
    usa.pack()
    home_label.pack(pady=20)

def states():
    hide_frames()
    state_frame.pack(fill='both', expand=1)
    random_state(state_frame)

    global entry
    entry = Entry(state_frame, font='Arial 15')
    entry.grid(pady=10, row=1, column=0, columnspan=2)

    Button(state_frame, text='Submit', font='Arial 13', command=state_answer).grid(pady=10, row=2, column=0, sticky='e', padx=5)
    Button(state_frame, text='Next', font='Arial 13', command=states).grid(pady=10, row=2, column=1, sticky='w', padx=5)

    global state_label
    state_label = Label(state_frame, text='', font='Arial 15', width=16)
    state_label.grid(pady=10, row=3, column=0, columnspan=2)

def state_capitals():
    hide_frames()
    state_capitals_frame.pack(fill='both', expand=1)
    random_state(state_capitals_frame)

    global capital
    state_capitals_list = ['Juneau', 'Phoenix', 'Sacramento', 'Denver', 'Tallahassee', 'Honolulu', 'Boston', 'Lansing', 'Helena', 'Trenton', 'Columbus', 'Harrisburg', 'Austin', 'Richmond', 'Olympia']
    capital = state_capitals_list[ind]

    first_two = [i for i in random.sample(state_capitals_list, k=3) if i != capital]
    if len(first_two) == 3:
        first_two = first_two[:-1]
    choices = random.sample(first_two + [capital], k=3) + [capital]

    global choosed
    choosed = StringVar()
    choosed.set(choices[0])
    Radiobutton(state_capitals_frame, text=choices[0], font='Arial 13', variable=choosed, value=choices[0]).grid(row=1, column=0, columnspan=2)
    Radiobutton(state_capitals_frame, text=choices[1], font='Arial 13', variable=choosed, value=choices[1]).grid(row=2, column=0, columnspan=2)
    Radiobutton(state_capitals_frame, text=choices[2], font='Arial 13', variable=choosed, value=choices[2]).grid(row=3, column=0, columnspan=2, pady=(0, 10))

    Button(state_capitals_frame, text='Submit', font='Arial 13', command=state_capitals_answer).grid(pady=10, row=4, column=0, sticky='e', padx=5)
    Button(state_capitals_frame, text='Next', font='Arial 13', command=state_capitals).grid(pady=10, row=4, column=1, sticky='w', padx=5)

    global state_capitals_label
    state_capitals_label = Label(state_capitals_frame, text='', font='Arial 15', width=16)
    state_capitals_label.grid(pady=10, row=5, column=0, columnspan=2)

menu = Menu(root)
root.config(menu=menu)

app = Menu(menu)
menu.add_cascade(label='App', menu=app)
app.add_command(label='Home', command=home)
app.add_command(label='Exit', command=root.destroy)

geography = Menu(menu)
menu.add_cascade(label='Geography', menu=geography)
geography.add_command(label='States', command=states)
geography.add_command(label='State Capitals', command=state_capitals)

state_frame = Frame(root)
state_capitals_frame = Frame(root)

root.mainloop()