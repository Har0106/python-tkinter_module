from tkinter import *
from tkinter import messagebox
import random

class TicTacToe():
    def game(self):
        # creating the main gui window
        self.root = Tk()
        self.root.title('Tic-Tac-Toe')
        self.ls = [i for i in range(9)]
        coordinates = [[i,j] for i in range(3) for j in range(3)]  

        for i in range(9):
            def func(x=i):
                return self.user(x)
            self.ls[i] = Button(self.root, text='', font='Arial 60', width=2, command=func)
            self.ls[i].grid(row=coordinates[i][0], column=coordinates[i][1])
        self.moves = [i for i in self.ls]

        self.root.mainloop()

    def user(self, i):
        self.ls[i].configure(text='X', state='disable')
        self.moves.remove(self.ls[i])
        if self.moves != []:
            choose = random.choice(self.moves)
            choose.configure(text='O', state='disabled')
            self.moves.remove(choose)

TicTacToe().game()