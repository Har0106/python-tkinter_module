from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title('Math Flash Card App')

global home_image
global home_numbers
global home_label
home_image = ImageTk.PhotoImage(Image.open('math_flashcard_app/numbers.jpg').resize((400, 400)))
home_numbers = Label(root, image=home_image)
home_label = Label(root, text='Learn Math With\nMath Flash Card App', font='Arial 15', justify='center')
home_numbers.pack()
home_label.pack(pady=20)

def hide_frames():
    for widget in additon_frame.winfo_children():
        widget.destroy()
    for widget in subtraction_frame.winfo_children():
        widget.destroy()
    for widget in multiplication_frame.winfo_children():
        widget.destroy()
    for widget in division_frame.winfo_children():
        widget.destroy()

    home_numbers.pack_forget()
    home_label.pack_forget()
    additon_frame.pack_forget()
    subtraction_frame.pack_forget()
    multiplication_frame.pack_forget()
    division_frame.pack_forget()

def home():
    hide_frames()
    home_numbers.pack()
    home_label.pack(pady=20)

def operations(operation, frame, func):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    Label(frame, text=num1, font='Arial 150').grid(row=0, column=0, padx=(50, 10))
    Label(frame, text=operation, font='Arial 100').grid(row=0, column=1, padx=10)
    Label(frame, text=num2, font='Arial 150').grid(row=0, column=2, padx=(10, 50))

    entry = Entry(frame, font='Arial 25', justify='center', width=10)
    entry.grid(row=1, column=0, columnspan=3, pady=(0, 30))

    Button(frame, font='Arial 13', text='Submit').grid(padx=10, pady=(0, 20), row=2, column=0, sticky='e')
    Button(frame, font='Arial 13', text='Next', command=func).grid(padx=10, pady=(0, 20), row=2, column=2, sticky='w')

    op_label = Label(frame, font='Arial 15', text='')
    op_label.grid(pady=10)

def additon():
    hide_frames()
    additon_frame.pack(fill='both', expand=1)
    operations('+', additon_frame, additon)

def subtraction():
    hide_frames()
    subtraction_frame.pack(fill='both', expand=1)
    operations('-', subtraction_frame, subtraction)

def multiplication():
    hide_frames()
    multiplication_frame.pack(fill='both', expand=1)
    operations('x', multiplication_frame, multiplication)

def division():
    hide_frames()
    division_frame.pack(fill='both', expand=1)
    operations('÷', division_frame, division)
    Label(division_frame, text='Give The Answer\nIn Rounded Form', font='Arial 15', justify='center').grid(row=3, column=0, columnspan=3, pady=10)

menu = Menu(root)
root.config(menu=menu)

app = Menu(menu)
menu.add_cascade(label='App', menu=app)
app.add_command(label='Home', command=home)
app.add_command(label='Exit', command=root.destroy)

math = Menu(menu)
menu.add_cascade(label='Math', menu=math)
math.add_command(label='Addition', command=additon)
math.add_command(label='Subtraction', command=subtraction)
math.add_command(label='Multiplication', command=multiplication)
math.add_command(label='Division', command=division)

additon_frame = Frame(root)
subtraction_frame = Frame(root)
multiplication_frame = Frame(root)
division_frame = Frame(root)

root.mainloop()