from tkinter import *
from datetime import date
from tkinter import messagebox

root = Tk()
root.title('Age Calculator')

def calculate_age():
    today = date.today()
    day = entry_d.get()
    month = entry_m.get()
    year = entry_y.get()
    try:
        text = today.year - int(year)-((today.month, today.day) < (int(month), int(day)))
        Label(root, text=f'Age: {text}', font='Arial 15', width=10).grid(row=6, column=0, columnspan=2)
    except:
        messagebox.showerror('showerror', 'Invalid Birth Date')

Label(root, text='Age Calculator', font='Arial 25').grid(row=0, column=0, columnspan=2, padx=50)
Label(root, text='Enter Your Date of birth', font='Arial 15').grid(row=1, column=0, columnspan=2, pady=10)
Label(root, text='Date:', font='Arial 15').grid(row=2, column=0, pady=8)
Label(root, text='Month:', font='Arial 15').grid(row=3, column=0, pady=8)
Label(root, text='Year:', font='Arial 15').grid(row=4, column=0, pady=8)

entry_d = Entry(root, justify='right', font='Arial 15', width=11)
entry_d.grid(row=2, column=1)
entry_m = Entry(root, justify='right', font='Arial 15', width=11)
entry_m.grid(row=3, column=1)
entry_y = Entry(root, justify='right', font='Arial 15', width=11)
entry_y.grid(row=4, column=1)

Button(root, text='Calculate Age', font='Arial 13', command=calculate_age).grid(row=5, column=0, columnspan=2, pady=8)
Button(root, text='Close', font='Arial 13', command=root.destroy).grid(row=7, column=0, columnspan=2, pady=8)

root.mainloop()