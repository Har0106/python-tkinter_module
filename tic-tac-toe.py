from tkinter import *
import random
from tkinter import messagebox

class TicTacToe():
    def game(self):
        # creating the main gui window
        self.root = Tk()
        self.root.title('Tic-Tac-Toe')

        # To create the first tic tac toe board
        self.reset()

        self.root.mainloop()

    def reset(self):
        # to check if the user has clicked before the computer clicks
        self.clicked = 0

        # lists to store buttons and row and column of buttons
        self.ls = [i for i in range(9)]
        coordinates = [[i,j] for i in range(3) for j in range(3)]

        # creating buttons and showing them on grid
        for i in range(9):
            def func(x=i):
                return self.user(x)
            self.ls[i] = Button(self.root, text='', font='Arial 50 bold', width=3, command=func, bg='#FFF4C2')
            self.ls[i].grid(row=coordinates[i][0], column=coordinates[i][1])

        # copy of self.ls to remove things when one is choosen
        self.moves = [i for i in self.ls]

    def user(self, i):
        # user making moves
        self.ls[i].configure(disabledforeground='blue', text='X', state='disabled')
        self.moves.remove(self.ls[i])
        self.clicked = 1
        self.winner()

        # computer making move
        if self.clicked == 1:
            self.computer()
            self.winner()

    def computer(self):
        # choosing the computers move
        if self.moves != []:
            choose = random.choice(self.moves)
            choose.configure(disabledforeground='red', text='O', state='disabled')
            self.moves.remove(choose)

    def winner(self):
        # row, column and diagonal buttons of the board
        row = [self.ls[i*3:i*3+3] for i in range(3)]
        column = [[self.ls[i], self.ls[i+3], self.ls[i+6]] for i in range(3)]
        diagonal = [[self.ls[0], self.ls[4], self.ls[8]]]+[[self.ls[2], self.ls[4], self.ls[6]]]

        # checking for the winner
        for grid in row+column+diagonal:
            i = set(i['text'] for i in grid)
            if len(i) == 1 and i in [{'X'},{'O'}]:
                [item.configure(bg='#CD7F32') for item in grid]
                if messagebox.askyesno('Game Over', f'{list(i)[0]} won!\nDo you want to play again?'):
                    self.reset()
        if all([i['state']=='disabled' for i in self.ls]):
            if messagebox.askyesno('Game Over', 'Tie! Do you want to play again?'):
                self.reset()
            
TicTacToe().game()