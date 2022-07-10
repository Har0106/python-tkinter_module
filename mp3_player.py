from tkinter import *
from tkinter import filedialog
import pygame

root = Tk()
root.title('MP3 Player')
pygame.mixer.init()

def add_song():
    global songs
    path = filedialog.askopenfilenames(filetypes=[('mp3 files', '*.mp3')])
    songs = [[i, i.split('/')[-1]] for i in path]
    for i,a in songs:
        listboxes.insert(END, a)

def play_pause():
        if mid.cget('text') == u"\u25B6":
            mid.configure(text=u'\u23F8')
        else:
            mid.configure(text=u"\u25B6")

global sound
sound = ''

def play_sound(event):
    global sound
    try:
        sound.stop()
    except:
        pass
    sel = listboxes.curselection()
    for i,a in songs:
        if listboxes.get(0, END)[sel[0]] == a:
            print(i)
            sound = pygame.mixer.Sound(i)
            sound.play()

listboxes = Listbox(root, width=40, font='Arial 15')
listboxes.grid(row=0, column=0, columnspan=3, padx=25, pady=(20, 15))
root.bind('<Button-1>', play_sound)

Button(root, text=u'\u23EE', font='Arial 20', bd=0).grid(row=1, column=0, pady=(0, 10), sticky='e')
mid = Button(root, text=u"\u25B6", font='Arial 20', bd=0, command=play_pause)
mid.grid(row=1, column=1, pady=(0, 10))
Button(root, text=u'\u23ED', font='Arial 20', bd=0).grid(row=1, column=2, pady=(0, 10), sticky='w')

menu = Menu(root)
root.config(menu=menu)

player = Menu(menu)
menu.add_cascade(label='Player', menu=player)
player.add_command(label='Exit', command=root.destroy)

edit_playlist = Menu(menu)
menu.add_cascade(label='Edit Playlist', menu=edit_playlist)
edit_playlist.add_command(label='Add', command=add_song)
edit_playlist.add_command(label='Remove')

root.mainloop()