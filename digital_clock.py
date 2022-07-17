from tkinter import *
import time

# creating the main gui wondow of the project
root = Tk()
root.title('Digital Clock')

# getting the current time and day of the week
def clock():
    t = time.strftime('%H:%M:%S')
    label.config(text=t)
    label2.config(text=time.strftime('%A'))
    label.after(1000, clock)

# design of the app
label = Label(root, font='Arial 50', fg='white', bg='black')
label2 = Label(root, font='Arial 30')
label.grid(row=0, column=0)
label2.grid(row=1, column=0)
clock()

root.mainloop()