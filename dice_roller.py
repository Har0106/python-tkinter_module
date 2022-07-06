from tkinter import *
import random

root = Tk()
root.title('Dice Roller')

def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    die = random.choice(dice)
    label.configure(text=die)
    Label(root, text=f'You Rolled {dice.index(die) + 1}', font='Arial 15').grid(row=3, column=0, pady=30)

Label(root, text='Dice Roller',font='Arial 30').grid(row=0, column=0, padx=75, pady=(20, 0))
label = Label(root, text='\u2680', font='Arial 125')
label.grid(row=1, column=0)
Button(root, text='Roll Dice', font='Arial 13', command=roll).grid(row=2, column=0, pady=(0, 20))

root.mainloop()