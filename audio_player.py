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

# Disabling or enabling forward button and backward button
def disabel_fb():
    if listboxes.get(0, END)[-1] == listboxes.get(0, END)[sel]:
       forward_button.configure(state='disabled')
    else:
       forward_button.configure(state='normal')
    if listboxes.get(0, END)[0] == listboxes.get(0, END)[sel]:
       backward_button.configure(state='disabled')
    else:
       backward_button.configure(state='normal')

# Modifying widgets if delete or clear function is used
def disabel_dc():
    mid.configure(state='disable')
    forward_button.configure(state='disable')
    backward_button.configure(state='disable')
    sound_button.configure(state='disable', text='🔈')
    volume_slider.configure(state='disabled', value=100)
    song_slider.configure(state='disabled', value=0)
    label4.configure(text='100%')
    label2.configure(text='00:00')
    label3.configure(text='00:00')
    label.configure(text='')
    mixer.music.stop()

# Adding songs to the playlist
def add_song():
    global songs
    path = filedialog.askopenfilenames(filetypes=[('mp3 files', '*.mp3'), ('ogg files', '*.ogg')])
    songs += [[i, i.split('/')[-1].split('.')[0].split(' - ')[1]] for i in path]
    for i,a in songs:
        if a not in listboxes.get(0, END):
            listboxes.insert(END, a)
    # Disabling or enabling forward and backward button when adding new songs
    if listboxes.curselection():
        if len(listboxes.get(0, END)) > 1:
            forward_button.configure(state='normal')
        else:
            forward_button.configure(state='disabled')

# Deleting a selected song from the playlist
def delete_songs():
    for i in songs:
        if listboxes.get(ANCHOR) in i:
            songs.remove(i)
    listboxes.delete(ANCHOR)
    mid.configure(text=u"\u25B6")
    if listboxes.curselection():
        listboxes.selection_clear(listboxes.curselection()[0])
    disabel_dc()

# Deleting all the songs from the playlist
def clear_songs():
    global songs
    songs = []
    listboxes.delete(0, END)
    mid.configure(text=u"\u25B6")
    disabel_dc()

# playing the song
def get_sound():
    global position
    mid.configure(state='normal')
    sound_button.configure(state='normal')
    song_slider.configure(state='normal')
    volume_slider.configure(state='normal')
    mixer.music.stop()
    position = -1
    for i,a in songs:
        if listboxes.get(0, END)[sel] == a:
            mixer.music.load(i)
            # Because I save songs like 'Artist - Song'
            label.configure(text='\n'.join(i.split('/')[-1].split('.')[0].split(' - ')))
            mixer.music.play()
            with audioread.audio_open(i) as f:
                duration = f.duration
                label3.configure(text=time.strftime('%M:%S', time.gmtime(duration)))
                song_slider.configure(to=duration)

# Getting the song to be played
def play_sound(event):
    global sel
    if listboxes.curselection():
        mid.configure(text=u'\u23F8')
        sel = listboxes.curselection()[0]
        disabel_fb()
        get_sound()

# Pausing and unpausing the music
def play_pause():
    if mid.cget('text') == u"\u25B6":
        mid.configure(text=u'\u23F8')
        mixer.music.unpause()
    else:
        mid.configure(text=u"\u25B6")
        mixer.music.pause()

# Play the next song or the previous song
def forward_backward(v):
    global sel
    if v:
        sel = listboxes.curselection()[0] + 1
    else:
        sel = listboxes.curselection()[0] - 1
    listboxes.selection_clear(listboxes.curselection()[0])
    listboxes.selection_set(sel)
    disabel_fb()
    get_sound()

# Muting and unmuting the song
def mute():
    if mixer.music.get_volume() != 0:
        sound_button.configure(text='🔈x', anchor='e')
        volume_slider.configure(state='disabled')
        mixer.music.set_volume(0)
    else:
        sound_button.configure(text='🔈')
        mixer.music.set_volume(int(volume))
        volume_slider.configure(state='normal')

# Setting the position of the music
def song_slider_command(x):
    global position
    position = float(song_slider.get())
    mixer.music.set_pos(position)

# Setting volume of the song
def volume_slider_command(x):
    global volume
    volume = x.split('.')[0]
    label4.configure(text=f"{volume}%")
    mixer.music.set_volume(int(volume))

# Changing label and slider the position as the song plays
# The song position would not be accurate
def time_duration():
    global position
    if mixer.music.get_busy():
        position += 1
        label2.configure(text=time.strftime('%M:%S', time.gmtime(position)))
        song_slider.configure(value=position)
    root.after(1000, time_duration)

# Design of the audio player
frame = Frame(root, highlightthickness=1, highlightbackground='black')
frame.pack(pady=20, padx=20)

scroll_y = Scrollbar(frame)
scroll_y.grid(sticky='ns', column=6, rowspan=4)

listboxes = Listbox(frame, width=25, font='Arial 15', activestyle='none', height=18, bd=0, highlightthickness=1, highlightbackground='black', justify='center', yscrollcommand=scroll_y.set)
listboxes.grid(row=0, column=5, rowspan=4)
listboxes.bind('<<ListboxSelect>>', play_sound)
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