from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from pygame import mixer
import audioread
import time

# Creating the gui window
root = Tk()
root.title('Audio Player')

mixer.init()
songs = []
volume = 100

# Disabling or enabling forward button and backward button
def disabel_fb():
    # If the song being played is the last song in the list box disable forward button
    if listboxes.get(0, END)[-1] == listboxes.get(0, END)[sel]:
       forward_button.configure(state='disabled')
    else:
       forward_button.configure(state='normal')

    # If the song being played is the first song in the list box enable forward button  
    if listboxes.get(0, END)[0] == listboxes.get(0, END)[sel]:
       backward_button.configure(state='disabled')
    else:
       backward_button.configure(state='normal')

# Modifying widgets if delete or clear function is used
def disabel_dc():
    mid.configure(text=u"\u25B6")
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
    # Asking for the song/songs to be added in the playlist
    path = filedialog.askopenfilenames(filetypes=[('mp3 files', '*.mp3'), ('ogg files', '*.ogg')])
    # Adding the path of song and the song title without artist name to songs list
    songs += [[i, i.split('/')[-1].split('.')[0].split(' - ')[1]] for i in path]

    # Adding song title without the artist name to the list box
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
    if listboxes.curselection():
        listboxes.selection_clear(listboxes.curselection()[0])
    disabel_dc()

# Deleting all the songs from the playlist
def clear_songs():
    global songs
    songs = []
    listboxes.delete(0, END)
    disabel_dc()

# playing the song
def play_sound():
    global position
    position = -1

    # Enabling pause, sound buttons and song, volume sliders when a new song is being played
    mid.configure(state='normal')
    sound_button.configure(state='normal')
    song_slider.configure(state='normal')
    volume_slider.configure(state='normal')

    # Stop if a music is already being played
    mixer.music.stop()

    # Getting the full path of the song which is selected and playing it
    for i,a in songs:
        if listboxes.get(0, END)[sel] == a:
            mixer.music.load(i)

            # Text to be put on the label 1. Because I save songs like 'Artist - Song'.
            label.configure(text='\n'.join(i.split('/')[-1].split('.')[0].split(' - ')))
            mixer.music.play()

            # Getting the duration of the song and setting slider and label
            with audioread.audio_open(i) as f:
                duration = f.duration
                label3.configure(text=time.strftime('%M:%S', time.gmtime(duration)))
                song_slider.configure(to=duration)

# Getting the song to be played
def get_sound(event):
    global sel
    # passing the selected song to get_song fuction
    if listboxes.curselection():
        mid.configure(text=u'\u23F8')
        sel = listboxes.curselection()[0]
        disabel_fb()
        play_sound()

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
    play_sound()

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

# Setting volume of the song and updating label
def volume_slider_command(x):
    global volume
    volume = x.split('.')[0]
    label4.configure(text=f"{volume}%")
    mixer.music.set_volume(int(volume))

# Changing label and slider the position as the song plays. The song position would not be accurate.
def time_duration():
    global position
    if mixer.music.get_busy():
        position += 1
        label2.configure(text=time.strftime('%M:%S', time.gmtime(position)))
        song_slider.configure(value=position)
    root.after(1000, time_duration)

# Design of the audio player

# Main frame of the app
frame = Frame(root, highlightthickness=1, highlightbackground='black')
frame.pack(pady=20, padx=20)

# Scroll bar used for listbox
scroll_y = Scrollbar(frame)
scroll_y.grid(sticky='ns', column=6, rowspan=4)

# Listbox which contains playlist
listboxes = Listbox(frame, width=25, font='Arial 14', activestyle='none', height=18, bd=0, highlightthickness=1, highlightbackground='black', yscrollcommand=scroll_y.set, justify='center')
listboxes.grid(row=0, column=5, rowspan=4)
listboxes.bind('<<ListboxSelect>>', get_sound)
scroll_y.configure(command=listboxes.yview)

# Volume mute or unmute button
sound_button = Button(frame, font='Arial 18', bd=0, state='disabled', text=u'🔈', command=mute)
sound_button.grid(row=0, column=0, sticky='e')

# Label to show the song being played, with the artist name
label = Label(frame, bg='white', text='', font='Arial 15', width=25, height=8, highlightthickness=1, highlightbackground='black', justify='center')
label.grid(row=1, column=0, columnspan=5, padx=10)

# Label to show the duration of the song
label3 = Label(frame, bg='white', text='00:00', font='Arial 8', highlightthickness=1, highlightbackground='black', justify='center')
label3.grid(row=2, column=4, sticky='e', padx=10)

# Label to show the current song position
label2 = Label(frame, bg='white', text='00:00', font='Arial 8', highlightthickness=1, highlightbackground='black', justify='center')
label2.grid(row=2, column=0, sticky='w', padx=10)

# Show the percentage of volume
label4 = Label(frame, bg='white', text='100%', font='Arail 10', highlightthickness=1, highlightbackground='black', justify='center')
label4.grid(row=0, column=4, sticky='w')

# Song position slider
song_slider = ttk.Scale(frame, from_=0, to=0, orient='horizontal', length=200, command=song_slider_command, state='disabled')
song_slider.grid(row=2, column=1, columnspan=3)

# Volume level slider
volume_slider = ttk.Scale(frame, from_=0, to=100, orient='horizontal', length=175, command=volume_slider_command, value=100, state='disabled')
volume_slider.grid(row=0, column=1, columnspan=3)

# Button to play the song above the song, which is being played, in the playlist
backward_button = Button(frame, text=u'\u23EE', font='Arial 20', bd=0, command=lambda: forward_backward(0), state='disabled')
backward_button.grid(row=3, column=0, sticky='e', columnspan=2)

# Pause and unpause the song
mid = Button(frame, text=u"\u25B6", font='Arial 20', bd=0, command=play_pause, state='disabled')
mid.grid(row=3, column=2)

# Button to play the song below the song, which is being played, in the playlist
forward_button = Button(frame, text=u'\u23ED', font='Arial 20', bd=0, command=lambda: forward_backward(1), state='disabled')
forward_button.grid(row=3, column=3, sticky='w', columnspan=2)

# Main menu of the app
menu = Menu(frame)
root.config(menu=menu)

# Player menu to exit the app or get the info of app
player_menu = Menu(menu, tearoff=0)
menu.add_cascade(label='Player', menu=player_menu)
player_menu.add_command(label='Exit', command=root.destroy)
player_menu.add_command(label='About', command=lambda:messagebox.showinfo('About', 'Audio player by Har0106'))

# Edit playlist menu to add new song to playlist, remove a song from playlist or remove all the songs in playlist
edit_playlist = Menu(menu, tearoff=0)
menu.add_cascade(label='Edit Playlist', menu=edit_playlist)
edit_playlist.add_command(label='Add', command=add_song)
edit_playlist.add_command(label='Remove', command=delete_songs)
edit_playlist.add_command(label='Clear', command=clear_songs)

time_duration()
root.mainloop()