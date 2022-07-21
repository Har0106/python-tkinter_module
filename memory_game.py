from tkinter import *
from tkinter import messagebox
import random

class MemoryGame():
    def game(self):
        # creating the main gui window
        self.root = Tk()
        self.root.title('Memory Game')

        # fruits and few vegetables to be shown on the screen when a button is clicked
        self.tiles = ['🍏','🍏','🍊','🍊','🍎','🍎','🍐','🍐','🍋','🍋','🍇','🍇','🍓','🍓','🍈','🍈','🍒','🍒','🥭','🥭', '🍌', '🍌', '🍉', '🍉', '🍍', '🍍', '🥝', '🥝', '🥑', '🥑', '🍑', '🍑', '🌽', '🌽', '🍅', '🍅']
        
        # initial number of tiles
        self.tile_count = 16
        # slicing tiles upto tile count
        self.show_tiles = self.tiles[0:self.tile_count]

        # to create the initial memory game board
        self.reset()

        self.root.mainloop()

    # to reset everything if player clicked on yes
    def reset(self):
        # shuffling tiles to grid them on random places
        random.shuffle(self.show_tiles)

        # to show buttons on the gui window
        self.ls = [i for i in range(self.tile_count)]
        coordinates = [[i, j] for i in range(int(self.tile_count**(1/2))) for j in range(int(self.tile_count**(1/2)))]

        # to store what the player has clicked and how many times he/she/they clicked
        self.clicked = list()
        self.count = 0

        # main menu of the project
        menu = Menu(self.root)
        self.root.configure(menu=menu)

        # game menu to reset or exit the game
        game = Menu(menu, tearoff=False)
        menu.add_cascade(label='Game', menu=game)
        game.add_command(label='Reset', command=self.reset)
        game.add_command(label='Exit', command=self.root.destroy)

        # options menu to decide the number of tiles
        options = Menu(menu, tearoff=False)
        menu.add_cascade(label='Options', menu=options)
        options.add_command(label='16 tiles', command=lambda:self.options_command(16))
        options.add_command(label='36 tiles', command=lambda:self.options_command(36))

        # griding the buttons on the gui window
        for i in range(self.tile_count):
            def func(x=i):
                return self.show(x)
            self.ls[i] = Button(self.root, text='', font='Arial 35', width=3, command=func, bg='#ECFFDC')
            self.ls[i].grid(row=coordinates[i][0], column=coordinates[i][1])

    def options_command(self, num):
        # setting the number of tiles to player's option
        if self.tile_count != num:
            for i in self.root.winfo_children():
                i.destroy()
            self.tile_count = num
            self.show_tiles = self.tiles[0:self.tile_count]
            self.reset()

    def show(self, b):
        # things to be done write after a tile is clicked
        self.ls[b].configure(text=self.show_tiles[b], state='disabled', disabledforeground='black')
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

        # to reset the game after all the tiles are matched if player clicked on yes
        state = set([i['state'] for i in self.ls])
        if len(state) == 1 and list(state)[0] == 'disabled':
            if messagebox.askyesno('Gmae Over', 'Congratulations!\nDo you want to play again?'):
                self.reset()

MemoryGame().game()