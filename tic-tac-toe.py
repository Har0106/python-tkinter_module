from tkinter import *
import random
from tkinter import messagebox

class TicTacToe():
    def game(self):
        # creating the main gui window
        self.root = Tk()
        self.root.title('Tic-Tac-Toe')
        self.reset()
        self.root.mainloop()

    def reset(self):
        self.clicked = 0
        self.ls = [i for i in range(9)]
        coordinates = [[i,j] for i in range(3) for j in range(3)]
        for i in range(9):
            def func(x=i):
                return self.user(x)
            self.ls[i] = Button(self.root, text='', font='Arial 50 bold', width=3, command=func, bg='#FFF4C2')
            self.ls[i].grid(row=coordinates[i][0], column=coordinates[i][1])
        self.moves = [i for i in self.ls]

    def user(self, i):
        self.ls[i].configure(disabledforeground='blue', text='X', state='disabled')
        self.moves.remove(self.ls[i])
        self.clicked = 1
        self.winner()
        if self.clicked == 1:
            self.computer()
            self.winner()

    def computer(self):
        if self.moves != []:
            choose = random.choice(self.moves)
            choose.configure(disabledforeground='red', text='O', state='disabled')
            self.moves.remove(choose)

    def winner(self):
        for i in range(3):
            row = self.ls[i*3:i*3+3]
            column = [self.ls[i], self.ls[i+3], self.ls[i+6]]
            diagonal1 = [self.ls[0], self.ls[4], self.ls[8]]
            diagonal2 = [self.ls[2], self.ls[4], self.ls[6]]
            for i in [set(i['text'] for i in row), set(i['text'] for i in column), set(i['text'] for i in diagonal1), set(i['text'] for i in diagonal2)]:
                if len(i) == 1 and i in [{'X'},{'O'}]:
                    if messagebox.askyesno('Game Over', f'{list(i)[0]} won!\nDo you want to play again?'):
                        self.reset()
                elif all([i['state']=='disabled' for i in self.ls]):
                    if messagebox.askyesno('Game Over', 'Tie! Do you want to play again?'):
                        self.reset()
            
TicTacToe().game()