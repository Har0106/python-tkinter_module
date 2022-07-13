from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title('Audio Player')
mixer.init()

songs = []

def disabel_normal():
    if listboxes.get(0, END)[-1] == listboxes.get(0, END)[sel]:
       forward_button.configure(state='disabled')
    else:
       forward_button.configure(state='normal')
    if listboxes.get(0, END)[0] == listboxes.get(0, END)[sel]:
       backward_button.configure(state='disabled')
    else:
       backward_button.configure(state='normal')

def add_song():
    global songs
    path = filedialog.askopenfilenames(filetypes=[('mp3 files', '*.mp3'), ('wav files', '*.wav')])
    songs += [[i, i.split('/')[-1]] for i in path]
    for i,a in songs:
        if a not in listboxes.get(0, END):
            listboxes.insert(END, a)
    if listboxes.curselection():
        if len(listboxes.get(0, END)) > 1:
            forward_button.configure(state='normal')
        else:
            forward_button.configure(state='disabled')

def delete_songs():
    mid.configure(state='disable')
    for i in songs:
        if listboxes.get(ANCHOR) in i:
            songs.remove(i)
    listboxes.delete(ANCHOR)
    mid.configure(text=u"\u25B6")
    if listboxes.curselection():
        listboxes.selection_clear(listboxes.curselection()[0])
    forward_button.configure(state='disable')
    backward_button.configure(state='disable')
    mixer.music.stop()

def clear_songs():
    mid.configure(state='disable')
    global songs
    listboxes.delete(0, END)
    mid.configure(text=u"\u25B6")
    songs = []
    forward_button.configure(state='disable')
    backward_button.configure(state='disable')
    mixer.music.stop()

def play_sound():
    mid.configure(state='normal')
    mixer.music.stop()
    for i,a in songs:
        if listboxes.get(0, END)[sel] == a:
            mixer.music.load(i)
            mixer.music.play()

def get_sound(event):
    global sel
    mid.configure(text=u'\u23F8')
    if listboxes.curselection():
        sel = listboxes.curselection()[0]
        disabel_normal()
        play_sound()

def play_pause():
    if mid.cget('text') == u"\u25B6":
        mid.configure(text=u'\u23F8')
        mixer.music.unpause()
    else:
        mid.configure(text=u"\u25B6")
        mixer.music.pause()

def forward_backward(v):
    global sel
    if v:
        sel = listboxes.curselection()[0] + 1
    else:
        sel = listboxes.curselection()[0] - 1
    listboxes.selection_clear(listboxes.curselection()[0])
    listboxes.selection_set(sel)
    disabel_normal()
    play_sound()

listboxes = Listbox(root, width=40, font='Arial 15', activestyle='none')
listboxes.grid(row=0, column=0, columnspan=3, padx=25, pady=(20, 15))
listboxes.bind('<<ListboxSelect>>', get_sound)

backward_button = Button(root, text=u'\u23EE', font='Arial 20', bd=0, command=lambda: forward_backward(0), state='disabled')
backward_button.grid(row=1, column=0, pady=(0, 10), sticky='e')
mid = Button(root, text=u"\u25B6", font='Arial 20', bd=0, command=play_pause, state='disabled')
mid.grid(row=1, column=1, pady=(0, 10))
forward_button = Button(root, text=u'\u23ED', font='Arial 20', bd=0, command=lambda: forward_backward(1), state='disabled')
forward_button.grid(row=1, column=2, pady=(0, 10), sticky='w')

menu = Menu(root)
root.config(menu=menu)

player = Menu(menu)
menu.add_cascade(label='Player', menu=player)
player.add_command(label='Exit', command=root.destroy)

edit_playlist = Menu(menu)
menu.add_cascade(label='Edit Playlist', menu=edit_playlist)
edit_playlist.add_command(label='Add', command=add_song)
edit_playlist.add_command(label='Remove', command=delete_songs)
edit_playlist.add_command(label='Clear', command=clear_songs)

root.mainloop()