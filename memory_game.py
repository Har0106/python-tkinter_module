from tkinter import *
from tkinter import messagebox
import random

class MemoryGame():
    def game(self):
        self.root = Tk()
        self.root.title('Memory Game')

        self.reset()

        self.root.mainloop()

    def show(self, b):
        self.ls[b].configure(text=self.tiles[b], state='disabled', disabledforeground='black')
        self.clicked.append(self.ls[b])
        self.count += 1
        if self.count % 2 == 0:
            if self.clicked[-2]['text'] == self.ls[b]['text']:
                self.clicked[-2].configure(bg='#32CD32')
                self.ls[b].configure(bg='#32CD32')
            else:
                messagebox.showinfo('Memory Game', 'Not a Match!')
                self.clicked[-2].configure(text='', state='normal')
                self.ls[b].configure(text='', state='normal')

        state = set([i['state'] for i in self.ls])
        if len(state) == 1 and list(state)[0] == 'disabled':
            if messagebox.askyesno('Gmae Over', 'Congratulations!\nDo you want to play again?'):
                self.reset()
            else:
                self.root.destroy()
                quit()

    def reset(self):
        self.tiles = ['🍏','🍏','🍊','🍊','🍎','🍎','🍐','🍐','🍋','🍋','🍇','🍇','🍓','🍓','🍈','🍈','🍒','🍒','🥭','🥭', '🍌', '🍌', '🍉', '🍉', '🍍', '🍍', '🥝', '🥝', '🥑', '🥑', '🍑', '🍑', '🌽', '🌽', '🍅', '🍅']
        random.shuffle(self.tiles)
        self.ls = [i for i in range(36)]
        coordinates = [[i, j] for i in range(6) for j in range(6)]
        self.clicked = list()
        self.count = 0

        for i in range(36):
            def func(x=i):
                return self.show(x)
            self.ls[i] = Button(self.root, text='', font='Arial 35', width=3, command=func, bg='#ECFFDC')
            self.ls[i].grid(row=coordinates[i][0], column=coordinates[i][1])

MemoryGame().game()