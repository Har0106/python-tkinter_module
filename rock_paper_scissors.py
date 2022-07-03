from tkinter import *
import random

#Tkinter Window
root = Tk()
root.title('Rock Paper Scissors')

def game(user):
    #Computer Choice
    computer = random.choice(['Rock', 'Paper', 'Scissors'])
    #Computer Choice on Screen
    Label(root, font='Arial 15', text=f'Computer Choice: {computer}', width=25).grid(row=4, column=0)
    #Won, Lost or Tie
    label = Label(root, font='Arial 15', width=20, pady=2)
    label.grid(row=5, column=0)
    if (computer == 'Rock' and user == 'Paper') or (computer == 'Scissor' and user == 'Rock') or (computer == 'Paper' and user == 'Scissors'):
        label.config(text='You won!')
    elif computer == user:
        label.config(text="It's Tie!")
    else:
        label.config(text="You Lost!")

#Design
Button(root, text='Rock', font='Arial 15', width=10, command=lambda: game('Rock')).grid(row=0, column=0, padx=100, pady=2)
Button(root, text='Paper', font='Arial 15', width=10, command=lambda: game('Paper')).grid(row=1, column=0, padx=100, pady=2)
Button(root, text='Scissor', font='Arial 15', width=10, command=lambda: game('Scissors')).grid(row=2, column=0, padx=100, pady=2)
Label(root, text='').grid(row=3, column=0)

root.mainloop()