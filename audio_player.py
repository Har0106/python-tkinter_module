from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from pygame import mixer
import audioread
import time

root = Tk()
root.title('Audio Player')
mixer.init()
songs = []
volume = 100

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
    song_slider.configure(state='normal')
    volume_slider.configure(state='normal')
    mixer.music.stop()
    for i,a in songs:
        if listboxes.get(0, END)[sel] == a:
            mixer.music.load(i)
            label.configure(text='\n'.join(i.split('/')[-1].split('.')[0].split(' - ')))
            mixer.music.play()
            with audioread.audio_open(i) as f:
                duration = f.duration
                label3.configure(text=time.strftime('%M:%S', time.gmtime(duration)))
                song_slider.configure(to=duration)

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

def mute():
    if mixer.music.get_volume() != 0:
        sound_button.configure(text='🔈x', anchor='e')
        volume_slider.configure(state='disabled')
        mixer.music.set_volume(0)
    else:
        sound_button.configure(text='🔈')
        mixer.music.set_volume(int(volume))
        volume_slider.configure(state='normal')

position = 0

def song_slider_command(x):
    global position
    position = float(song_slider.get())
    mixer.music.set_pos(position)

def volume_slider_command(x):
    global volume
    volume = x.split('.')[0]
    label4.configure(text=f"{volume}%")
    mixer.music.set_volume(int(volume))

def time_duration():
    global position
    if mixer.music.get_busy():
        position += 1
        label2.configure(text=time.strftime('%M:%S', time.gmtime(position)))
        song_slider.configure(value=position)
    root.after(1000, time_duration)

frame = Frame(root, highlightthickness=1, highlightbackground='black')
frame.pack(pady=20, padx=20)

scroll_y = Scrollbar(frame)
scroll_y.grid(sticky='ns', column=6, rowspan=4)

listboxes = Listbox(frame, width=25, font='Arial 15', activestyle='none', height=18, bd=0, highlightthickness=1, highlightbackground='black', justify='center', yscrollcommand=scroll_y.set)
listboxes.grid(row=0, column=5, rowspan=4)
listboxes.bind('<<ListboxSelect>>', get_sound)
scroll_y.configure(command=listboxes.yview)

sound_button = Button(frame, font='Arial 18', bd=0, state='disabled', text=u'🔈', command=mute)
sound_button.grid(row=0, column=0, sticky='e')

label = Label(frame, bg='white', text='', font='Arial 15', width=25, height=8, highlightthickness=1, highlightbackground='black', justify='center')
label.grid(row=1, column=0, columnspan=5, padx=10)
label3 = Label(frame, bg='white', text='00:00', font='Arial 8', highlightthickness=1, highlightbackground='black', justify='center')
label3.grid(row=2, column=4, sticky='e', padx=10)
label2 = Label(frame, bg='white', text='00:00', font='Arial 8', highlightthickness=1, highlightbackground='black', justify='center')
label2.grid(row=2, column=0, sticky='w', padx=10)
label4 = Label(frame, bg='white', text='100%', font='Arail 10', highlightthickness=1, highlightbackground='black', justify='center')
label4.grid(row=0, column=4, sticky='w')

song_slider = ttk.Scale(frame, from_=0, to=0, orient='horizontal', length=200, command=song_slider_command, state='disabled')
song_slider.grid(row=2, column=1, columnspan=3)
volume_slider = ttk.Scale(frame, from_=0, to=100, orient='horizontal', length=175, command=volume_slider_command, value=100, state='disabled')
volume_slider.grid(row=0, column=1, columnspan=3)

backward_button = Button(frame, text=u'\u23EE', font='Arial 20', bd=0, command=lambda: forward_backward(0), state='disabled')
backward_button.grid(row=3, column=0, sticky='e', columnspan=2)
mid = Button(frame, text=u"\u25B6", font='Arial 20', bd=0, command=play_pause, state='disabled')
mid.grid(row=3, column=2)
forward_button = Button(frame, text=u'\u23ED', font='Arial 20', bd=0, command=lambda: forward_backward(1), state='disabled')
forward_button.grid(row=3, column=3, sticky='w', columnspan=2)

menu = Menu(frame)
root.config(menu=menu)
edit_playlist = Menu(menu, tearoff=0)
menu.add_cascade(label='Edit Playlist', menu=edit_playlist)
edit_playlist.add_command(label='Add', command=add_song)
edit_playlist.add_command(label='Remove', command=delete_songs)
edit_playlist.add_command(label='Clear', command=clear_songs)

time_duration()
root.mainloop()