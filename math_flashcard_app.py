from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random

class MathFlashcard():
    def app(self):
        # creating the main gui of the app
        self.root = Tk()
        self.root.title('Math Flash Card App')

        # creating images
        self.home_image = ImageTk.PhotoImage(Image.open('math_flashcard_app/numbers.jpg').resize((400, 400)))
        self.home_numbers = Label(self.root, image=self.home_image)
        self.home_label = Label(self.root, text='Learn Math With\nMath Flash Card App', font='Arial 15', justify='center')
        self.home_numbers.pack()
        self.home_label.pack(pady=20)

        # main menu of the app
        menu = Menu(self.root)
        self.root.config(menu=menu)

        # app menu to navigate to the home page or exit the app
        app = Menu(menu)
        menu.add_cascade(label='App', menu=app)
        app.add_command(label='Home', command=self.home)
        app.add_command(label='Exit', command=self.root.destroy)

        # math menu to select a quiz type
        math = Menu(menu)
        menu.add_cascade(label='Math', menu=math)
        math.add_command(label='Addition', command=self.additon)
        math.add_command(label='Subtraction', command=self.subtraction)
        math.add_command(label='Multiplication', command=self.multiplication)

        # separate frme for all quiz types
        self.additon_frame = Frame(self.root)
        self.subtraction_frame = Frame(self.root)
        self.multiplication_frame = Frame(self.root)

        self.root.mainloop()

    # hiding frames when navigating from quiz type to another
    def hide_frames(self):
        for widget in self.additon_frame.winfo_children():
            widget.destroy()
        for widget in self.subtraction_frame.winfo_children():
            widget.destroy()
        for widget in self.multiplication_frame.winfo_children():
            widget.destroy()

        self.home_numbers.pack_forget()
        self.home_label.pack_forget()
        self.additon_frame.pack_forget()
        self.subtraction_frame.pack_forget()
        self.multiplication_frame.pack_forget()

    # to navigate to the home page
    def home(self):
        self.hide_frames()
        self.home_numbers.pack()
        self.home_label.pack(pady=20)

    # to perform operations and evaluate the answer
    def answers(self, symbol):
        if symbol == 'x':
            symbol = '*'
        try:
            ans = eval(str(self.num1) + symbol + str(self.num2))
            if ans == int(self.entry.get()):
                text = 'Correct!'
            else:
                text = f'Incorrect! The Answer is {ans}'
            self.op_label.configure(text=text)
        except:
            messagebox.showerror('Error', 'Invalid Number Entered')

    # main gui of different quiz types
    def operations(self, operation, frame, func):
        self.num1 = random.randint(0, 9)
        self.num2 = random.randint(0, 9)
        Label(frame, text=self.num1, font='Arial 150').grid(row=0, column=0, padx=(50, 10))
        Label(frame, text=operation, font='Arial 100').grid(row=0, column=1, padx=10, columnspan=2)
        Label(frame, text=self.num2, font='Arial 150').grid(row=0, column=3, padx=(10, 50))

        self.entry = Entry(frame, font='Arial 25', justify='center', width=10)
        self.entry.grid(row=1, column=0, columnspan=4, pady=(0, 30))

        Button(frame, font='Arial 13', text='Submit', command=lambda: self.answers(operation)).grid(padx=10, pady=(0, 20), row=2, column=0, columnspan=2, sticky='e')
        Button(frame, font='Arial 13', text='Next', command=func).grid(padx=10, pady=(0, 20), row=2, column=2, columnspan=2, sticky='w')

        self.op_label = Label(frame, font='Arial 15', text='', width=30)
        self.op_label.grid(pady=(10, 20), columnspan=4)

    # addition quiz
    def additon(self):
        self.hide_frames()
        self.additon_frame.pack(fill='both', expand=1)
        self.operations('+', self.additon_frame, self.additon)

    # subtraction quiz
    def subtraction(self):
        self.hide_frames()
        self.subtraction_frame.pack(fill='both', expand=1)
        self.operations('-', self.subtraction_frame, self.subtraction)

    # multiplication quiz
    def multiplication(self):
        self.hide_frames()
        self.multiplication_frame.pack(fill='both', expand=1)
        self.operations('x', self.multiplication_frame, self.multiplication)

MathFlashcard().app()