from tkinter import *
from tkinter import messagebox
import random

class MemoryGame():
    def game(self):
        # creating the main gui window
        self.root = Tk()
        self.root.title('Memory Game')

        # to create the initial memory game board
        self.reset()

        self.root.mainloop()

    def show(self, b):
        # things to be done write after a tile is clicked
        self.ls[b].configure(text=self.tiles[b], state='disabled', disabledforeground='black')
        self.clicked.append(self.ls[b])
        self.count += 1

        # determing if it is a match or not a match
        if self.count % 2 == 0:
            if self.clicked[-2]['text'] == self.ls[b]['text']:
                self.clicked[-2].configure(bg='#32CD32')
                self.ls[b].configure(bg='#32CD32')
            else:
                messagebox.showinfo('Memory Game', 'Not a Match!')
                self.clicked[-2].configure(text='', state='normal')
                self.ls[b].configure(text='', state='normal')

        # to reset or quit the game after all the tiles are matched
        state = set([i['state'] for i in self.ls])
        if len(state) == 1 and list(state)[0] == 'disabled':
            if messagebox.askyesno('Gmae Over', 'Congratulations!\nDo you want to play again?'):
                self.reset()
            else:
                self.root.destroy()
                quit()

    # to reset everything if player clicked on yes
    def reset(self):
        # fruits and few vegetables to be shown on the screen when a button is clicked
        self.tiles = ['🍏','🍏','🍊','🍊','🍎','🍎','🍐','🍐','🍋','🍋','🍇','🍇','🍓','🍓','🍈','🍈','🍒','🍒','🥭','🥭', '🍌', '🍌', '🍉', '🍉', '🍍', '🍍', '🥝', '🥝', '🥑', '🥑', '🍑', '🍑', '🌽', '🌽', '🍅', '🍅']
        random.shuffle(self.tiles)

        # to show buttons on the gui window
        self.ls = [i for i in range(36)]
        coordinates = [[i, j] for i in range(6) for j in range(6)]

        # to store what the player has clicked and how many times he/she/they clicked
        self.clicked = list()
        self.count = 0

        # griding the buttons on the gui window
        for i in range(36):
            def func(x=i):
                return self.show(x)
            self.ls[i] = Button(self.root, text='', font='Arial 35', width=3, command=func, bg='#ECFFDC')
            self.ls[i].grid(row=coordinates[i][0], column=coordinates[i][1])

MemoryGame().game()