from tkinter import *
from tkinter import filedialog
from pygame import mixer
import audioread
import time

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
    path = filedialog.askopenfilenames(filetypes=[('mp3 files', '*.mp3'), ('wav files', '*.wav'), ('ogg files', '*.ogg')])
    songs += [[i, i.split('/')[-1].split('.')[0].split(' - ')[1]] for i in path]
    for i,a in songs:
        if a not in listboxes.get(0, END):
            listboxes.insert(END, a)

def delete_songs():
    for i in songs:
        if listboxes.get(ANCHOR) in i:
            songs.remove(i)
    listboxes.delete(ANCHOR)
    mid.configure(text=u"\u25B6")
    if listboxes.curselection():
        listboxes.selection_clear(listboxes.curselection()[0])
    mid.configure(state='disable')
    forward_button.configure(state='disable')
    backward_button.configure(state='disable')
    label.configure(text='')
    mixer.music.stop()

def clear_songs():
    global songs
    songs = []
    listboxes.delete(0, END)
    mid.configure(text=u"\u25B6")
    mid.configure(state='disable')
    forward_button.configure(state='disable')
    backward_button.configure(state='disable')
    label.configure(text='')
    mixer.music.stop()

def play_sound():
    mid.configure(state='normal')
    sound_button.configure(state='normal')
    mixer.music.stop()
    for i,a in songs:
        if listboxes.get(0, END)[sel] == a:
            sound = mixer.music.load(i)
            label.configure(text='\n'.join(i.split('/')[-1].split('.')[0].split(' - ')))
            mixer.music.play()
            with audioread.audio_open(i) as f:
                label3.configure(text=time.strftime('%M:%S', time.gmtime(f.duration)))

def get_sound(event):
    global sel
    if listboxes.curselection():
        mid.configure(text=u'\u23F8')
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

def time_duration():
    if mixer.music.get_busy():
        label2.configure(text=time.strftime('%M:%S', time.gmtime(mixer.music.get_pos()/1000)))
    root.after(1000, time_duration)

frame = Frame(root, highlightthickness=1, highlightbackground='black')
frame.pack(pady=20, padx=20)

scroll_y = Scrollbar(frame)
scroll_y.grid(sticky='ns', column=6, rowspan=4)

listboxes = Listbox(frame, width=25, font='Arial 15', activestyle='none', height=18, bd=0, highlightthickness=1, highlightbackground='black', justify='center', yscrollcommand=scroll_y.set)
listboxes.grid(row=0, column=5, rowspan=4)
listboxes.bind('<<ListboxSelect>>', get_sound)
scroll_y.configure(command=listboxes.yview)

sound_button = Button(frame, font='Arial 20', bd=0, state='disabled', text=u'🔈')
sound_button.grid(row=0, column=0)
info_button = Button(frame, font='Arial 28', bd=0, text=u'🛈')
info_button.grid(row=0, column=4)

label = Label(frame, bg='white', text='', font='Arial 15', width=25, height=8, highlightthickness=1, highlightbackground='black', justify='center')
label.grid(row=1, column=0, columnspan=5, padx=10)
label3 = Label(frame, bg='white', text='00:00', font='Arial 8', highlightthickness=1, highlightbackground='black', justify='center')
label3.grid(row=2, column=4, sticky='e', padx=10)
label2 = Label(frame, bg='white', text='00:00', font='Arial 8', highlightthickness=1, highlightbackground='black', justify='center')
label2.grid(row=2, column=0, sticky='w', padx=10)

song_slider = Scale(frame, from_=0, to=100, orient='horizontal', length=175)
song_slider.grid(row=2, column=1, sticky='n', columnspan=3)

backward_button = Button(frame, text=u'\u23EE', font='Arial 20', bd=0, command=lambda: forward_backward(0), state='disabled')
backward_button.grid(row=3, column=0, sticky='e', columnspan=2)
mid = Button(frame, text=u"\u25B6", font='Arial 20', bd=0, command=play_pause, state='disabled')
mid.grid(row=3, column=2)
forward_button = Button(frame, text=u'\u23ED', font='Arial 20', bd=0, command=lambda: forward_backward(1), state='disabled')
forward_button.grid(row=3, column=3, sticky='w', columnspan=2)

menu = Menu(frame)
root.config(menu=menu)

player = Menu(menu)
menu.add_cascade(label='Player', menu=player)
player.add_command(label='Exit', command=root.destroy)

edit_playlist = Menu(menu)
menu.add_cascade(label='Edit Playlist', menu=edit_playlist)
edit_playlist.add_command(label='Add', command=add_song)
edit_playlist.add_command(label='Remove', command=delete_songs)
edit_playlist.add_command(label='Clear', command=clear_songs)

time_duration()
root.mainloop()