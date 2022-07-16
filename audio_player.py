from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from pygame import mixer
import audioread
import time

class AudioPlayer():
    def app(self):
        # Creating the gui window
        self.root = Tk()
        self.root.title('Audio Player')

        mixer.init()
        self.songs = []
        self.volume = 100

        # Design of the audio player

        # Main frame of the app
        frame = Frame(self.root, highlightthickness=1, highlightbackground='black')
        frame.pack(pady=20, padx=20)

        # Scroll bar used for listbox
        scroll_y = Scrollbar(frame)
        scroll_y.grid(sticky='ns', column=6, rowspan=4)

        # Listbox which contains playlist
        self.listboxes = Listbox(frame, width=25, font='Arial 14', activestyle='none', height=18, bd=0, highlightthickness=1, highlightbackground='black', yscrollcommand=scroll_y.set, justify='center')
        self.listboxes.grid(row=0, column=5, rowspan=4)
        self.listboxes.bind('<<ListboxSelect>>', self.get_sound)
        scroll_y.configure(command=self.listboxes.yview)

        # Volume mute or unmute button
        self.sound_button = Button(frame, font='Arial 18', bd=0, state='disabled', text=u'🔈', command=self.mute)
        self.sound_button.grid(row=0, column=0, sticky='e')

        # Label to show the song being played, with the artist name
        self.label = Label(frame, bg='white', text='', font='Arial 15', width=25, height=8, highlightthickness=1, highlightbackground='black', justify='center')
        self.label.grid(row=1, column=0, columnspan=5, padx=10)

        # Label to show the duration of the song
        self.label3 = Label(frame, bg='white', text='00:00', font='Arial 8', highlightthickness=1, highlightbackground='black', justify='center')
        self.label3.grid(row=2, column=4, sticky='e', padx=10)

        # Label to show the current song position
        self.label2 = Label(frame, bg='white', text='00:00', font='Arial 8', highlightthickness=1, highlightbackground='black', justify='center')
        self.label2.grid(row=2, column=0, sticky='w', padx=10)

        # Show the percentage of volume
        self.label4 = Label(frame, bg='white', text='100%', font='Arail 10', highlightthickness=1, highlightbackground='black', justify='center')
        self.label4.grid(row=0, column=4, sticky='w')

        # Song position slider
        self.song_slider = ttk.Scale(frame, from_=0, to=0, orient='horizontal', length=200, command=self.song_slider_command, state='disabled')
        self.song_slider.grid(row=2, column=1, columnspan=3)

        # Volume level slider
        self.volume_slider = ttk.Scale(frame, from_=0, to=100, orient='horizontal', length=175, command=self.volume_slider_command, value=100, state='disabled')
        self.volume_slider.grid(row=0, column=1, columnspan=3)

        # Button to play the song above the song, which is being played, in the playlist
        self.backward_button = Button(frame, text=u'\u23EE', font='Arial 20', bd=0, command=lambda: self.forward_backward(0), state='disabled')
        self.backward_button.grid(row=3, column=0, sticky='e', columnspan=2)

        # Pause and unpause the song
        self.mid = Button(frame, text=u"\u25B6", font='Arial 20', bd=0, command=self.play_pause, state='disabled')
        self.mid.grid(row=3, column=2)

        # Button to play the song below the song, which is being played, in the playlist
        self.forward_button = Button(frame, text=u'\u23ED', font='Arial 20', bd=0, command=lambda: self.forward_backward(1), state='disabled')
        self.forward_button.grid(row=3, column=3, sticky='w', columnspan=2)

        # Main menu of the app
        menu = Menu(frame)
        self.root.config(menu=menu)

        # Player menu to exit the app or get the info of app
        player_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label='Player', menu=player_menu)
        player_menu.add_command(label='Exit', command=self.root.destroy)
        player_menu.add_command(label='About', command=lambda:messagebox.showinfo('About', 'Audio player by Har0106'))

        # Edit playlist menu to add new song to playlist, remove a song from playlist or remove all the songs in playlist
        edit_playlist = Menu(menu, tearoff=0)
        menu.add_cascade(label='Edit Playlist', menu=edit_playlist)
        edit_playlist.add_command(label='Add', command=self.add_song)
        edit_playlist.add_command(label='Remove', command=self.delete_songs)
        edit_playlist.add_command(label='Clear', command=self.clear_songs)

        self.time_duration()
        self.root.mainloop()

    # Disabling or enabling forward button and backward button
    def disabel_fb(self):
        # If the song being played is the last song in the list box disable forward button
        if self.listboxes.get(0, END)[-1] == self.listboxes.get(0, END)[self.sel]:
            self.forward_button.configure(state='disabled')
        else:
            self.forward_button.configure(state='normal')

        # If the song being played is the first song in the list box enable forward button  
        if self.listboxes.get(0, END)[0] == self.listboxes.get(0, END)[self.sel]:
            self.backward_button.configure(state='disabled')
        else:
            self.backward_button.configure(state='normal')

    # Resetting widgets if delete or clear function is used
    def disabel_dc(self):
        self.mid.configure(text=u"\u25B6")
        self.mid.configure(state='disable')
        self.forward_button.configure(state='disable')
        self.backward_button.configure(state='disable')
        self.sound_button.configure(state='disable', text='🔈')
        self.volume_slider.configure(state='disabled', value=100)
        self.song_slider.configure(state='disabled', value=0)
        self.label4.configure(text='100%')
        self.label2.configure(text='00:00')
        self.label3.configure(text='00:00')
        self.label.configure(text='')
        mixer.music.stop()

    # Adding songs to the playlist
    def add_song(self):
        # Asking for the song/songs to be added in the playlist
        path = filedialog.askopenfilenames(filetypes=[('mp3 files', '*.mp3'), ('ogg files', '*.ogg')])
        # Adding the path of song and the song title without artist name to songs list
        self.songs += [[i, i.split('/')[-1].split('.')[0].split(' - ')[1]] for i in path]

        # Adding song title without the artist name to the list box
        for i,a in self.songs:
            if a not in self.listboxes.get(0, END):
                self.listboxes.insert(END, a)

        # Disabling or enabling forward and backward button when adding new songs
        if self.listboxes.curselection():
            if len(self.listboxes.get(0, END)) > 1:
                self.forward_button.configure(state='normal')
            else:
                self.forward_button.configure(state='disabled')

    # Deleting a selected song from the playlist
    def delete_songs(self):
        for i in self.songs:
            if self.listboxes.get(self.sel) in i:
                self.songs.remove(i)
        self.listboxes.delete(self.sel)
        if self.listboxes.curselection():
            self.listboxes.selection_clear(self.listboxes.curselection()[0])
        self.disabel_dc()

    # Deleting all the songs from the playlist
    def clear_songs(self):
        self.songs = []
        self.listboxes.delete(0, END)
        self.disabel_dc()

    # playing the song
    def play_sound(self):
        # Enabling pause, sound buttons and song, volume sliders when a new song is being played
        self.mid.configure(text=u"\u23F8")
        self.mid.configure(state='normal')
        self.sound_button.configure(state='normal')
        self.song_slider.configure(state='normal')
        self.volume_slider.configure(state='normal')
        self.position = 0

        # Stop if a music is already being played
        mixer.music.stop()

        # Getting the full path of the song which is selected and playing it
        for i,a in self.songs:
            if self.listboxes.get(0, END)[self.sel] == a:
                mixer.music.load(i)

                # Text to be put on the label 1. Because I save songs like 'Artist - Song'.
                self.label.configure(text='\n'.join(i.split('/')[-1].split('.')[0].split(' - ')))
                mixer.music.play()

                # Getting the duration of the song and setting slider and label
                with audioread.audio_open(i) as f:
                    self.duration = f.duration
                    self.label3.configure(text=time.strftime('%M:%S', time.gmtime(self.duration)))
                    self.song_slider.configure(to=self.duration)

    # Getting the song to be played
    def get_sound(self, event):
        # passing the selected song to get_song fuction
        if self.listboxes.curselection():
            self.mid.configure(text=u'\u23F8')
            self.sel = self.listboxes.curselection()[0]
            self.disabel_fb()
            self.play_sound()

    # Pausing and unpausing the music
    def play_pause(self):
        if self.mid.cget('text') == u"\u25B6":
            self.mid.configure(text=u'\u23F8')
            mixer.music.unpause()
        else:
            self.mid.configure(text=u"\u25B6")
            mixer.music.pause()

    # Play the next song or the previous song
    def forward_backward(self, v):
        if v:
            self.sel = self.listboxes.curselection()[0] + 1
        else:
            self.sel = self.listboxes.curselection()[0] - 1
        self.listboxes.selection_clear(self.listboxes.curselection()[0])
        self.listboxes.selection_set(self.sel)
        self.disabel_fb()
        self.play_sound()

    # Muting and unmuting the song
    def mute(self):
        if mixer.music.get_volume() != 0:
            self.sound_button.configure(text='🔈x', anchor='e')
            self.volume_slider.configure(state='disabled')
            mixer.music.set_volume(0)
        else:
            self.sound_button.configure(text='🔈')
            mixer.music.set_volume(int(self.volume)/100)
            self.volume_slider.configure(state='normal')

    # Setting the position of the music
    def song_slider_command(self, x):
        self.position = float(self.song_slider.get())
        mixer.music.set_pos(self.position)

    # Setting volume of the song and updating label
    def volume_slider_command(self, x):
        self.volume = x.split('.')[0]
        self.label4.configure(text=f"{self.volume}%")
        mixer.music.set_volume(int(self.volume)/100)

    # Changing label and slider the position as the song plays. The song position would not be accurate.
    def time_duration(self):
        if mixer.music.get_busy():
            if self.position <= self.duration:
                self.position += 1
                self.label2.configure(text=time.strftime('%M:%S', time.gmtime(self.position)))
                self.song_slider.configure(value=self.position)
        else:
            self.mid.configure(text=u"\u25B6")
        self.root.after(1000, self.time_duration)

AudioPlayer().app()