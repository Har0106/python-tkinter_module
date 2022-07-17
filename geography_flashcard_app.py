from tkinter import *
from PIL import Image, ImageTk
import random

class GeographyFlashcard():
    def app(self):
        self.root = Tk()
        self.root.title('Geography Flash Card App')

        self.usa_image = ImageTk.PhotoImage(Image.open('geography_flashcard_app/USA.jpg'))
        self.usa = Label(self.root, image=self.usa_image)
        self.home_label = Label(self.root, text='Study The States of USA\nWith Geography Flash Card App', font='Arial 15', justify='center')
        self.usa.pack()
        self.home_label.pack(pady=20)

        menu = Menu(self.root)
        self.root.config(menu=menu)

        app = Menu(menu)
        menu.add_cascade(label='App', menu=app)
        app.add_command(label='Home', command=self.home)
        app.add_command(label='Exit', command=self.root.destroy)

        geography = Menu(menu)
        menu.add_cascade(label='Geography', menu=geography)
        geography.add_command(label='States', command=self.states)
        geography.add_command(label='State Capitals', command=self.state_capitals)

        self.state_frame = Frame(self.root)
        self.state_capitals_frame = Frame(self.root)

        self.root.mainloop()

    def state_answer(self):
        answer = self.state.replace('_', ' ').title()
        if answer == self.entry.get().title():
            text = 'Correct!'
        else:
            text = f'Incorrect! The Correct Answer is {answer}'
        self.state_label.configure(text=text)

    def state_capitals_answer(self):
        if self.capital == self.choosed.get():
            text = 'Correct!'
        else:
            text = f'Incorrect! The Correct Answer is {self.capital}'
        self.state_capitals_label.configure(text=text)

    def hide_frames(self):
        for widget in self.state_frame.winfo_children():
            widget.destroy()
        for widget in self.state_capitals_frame.winfo_children():
            widget.destroy()
        self.usa.pack_forget()
        self.home_label.pack_forget()
        self.state_frame.pack_forget()
        self.state_capitals_frame.pack_forget()

    def random_state(self, frame):
        states_list = ['alaska', 'arizona', 'california', 'colorado', 'florida', 'hawaii', 'massachusetts', 'michigan', 'montana', 'new_jersey', 'ohio', 'pennsylvania', 'texas', 'virginia', 'washington']
        self.state = random.choice(states_list)
        self.ind = states_list.index(self.state)
        self.image = ImageTk.PhotoImage(Image.open(f'geography_flashcard_app/{self.state}.jpg').resize((250, 250)))
        Label(frame, image=self.image).grid(row=0, column=0, pady=20, padx=100, columnspan=2)

    def home(self):
        self.hide_frames()
        self.usa.pack()
        self.home_label.pack(pady=20)

    def states(self):
        self.hide_frames()
        self.state_frame.pack(fill='both', expand=1)
        self.random_state(self.state_frame)

        self.entry = Entry(self.state_frame, font='Arial 15')
        self.entry.grid(pady=10, row=1, column=0, columnspan=2)

        Button(self.state_frame, text='Submit', font='Arial 13', command=self.state_answer).grid(pady=10, row=2, column=0, sticky='e', padx=5)
        Button(self.state_frame, text='Next', font='Arial 13', command=self.states).grid(pady=10, row=2, column=1, sticky='w', padx=5)

        self.state_label = Label(self.state_frame, text='', font='Arial 15', width=50)
        self.state_label.grid(pady=10, row=3, column=0, columnspan=2)

    def state_capitals(self):
        self.hide_frames()
        self.state_capitals_frame.pack(fill='both', expand=1)
        self.random_state(self.state_capitals_frame)

        self.state_capitals_list = ['Juneau', 'Phoenix', 'Sacramento', 'Denver', 'Tallahassee', 'Honolulu', 'Boston', 'Lansing', 'Helena', 'Trenton', 'Columbus', 'Harrisburg', 'Austin', 'Richmond', 'Olympia']
        self.capital = self.state_capitals_list[self.ind]

        first_two = [i for i in random.sample(self.state_capitals_list, k=3) if i != self.capital]
        if len(first_two) == 3:
            first_two = first_two[:-1]
        choices = random.sample(first_two + [self.capital], k=3) + [self.capital]

        self.choosed = StringVar()
        self.choosed.set(choices[0])
        Radiobutton(self.state_capitals_frame, text=choices[0], font='Arial 13', variable=self.choosed, value=choices[0]).grid(row=1, column=0, columnspan=2)
        Radiobutton(self.state_capitals_frame, text=choices[1], font='Arial 13', variable=self.choosed, value=choices[1]).grid(row=2, column=0, columnspan=2)
        Radiobutton(self.state_capitals_frame, text=choices[2], font='Arial 13', variable=self.choosed, value=choices[2]).grid(row=3, column=0, columnspan=2, pady=(0, 10))

        Button(self.state_capitals_frame, text='Submit', font='Arial 13', command=self.state_capitals_answer).grid(pady=10, row=4, column=0, sticky='e', padx=5)
        Button(self.state_capitals_frame, text='Next', font='Arial 13', command=self.state_capitals).grid(pady=10, row=4, column=1, sticky='w', padx=5)

        self.state_capitals_label = Label(self.state_capitals_frame, text='', font='Arial 15', width=50)
        self.state_capitals_label.grid(pady=10, row=5, column=0, columnspan=2)

GeographyFlashcard().app()