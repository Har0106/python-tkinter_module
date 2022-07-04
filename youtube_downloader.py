from tkinter import *
from pytube import YouTube
from tkinter import messagebox

root = Tk()
root.title('YouTube Downloader')

def download():
    try:
        y = YouTube(entry.get())
        video = y.streams.get_highest_resolution()
        try:
            video.download()
        except:
            messagebox.showerror('showerror', 'Some error occured')
    except:
        messagebox.showinfo('showinfo', 'Check your network connection or check the URL')

def download_next():
    entry.delete(0, END)

Label(root, text='YouTube Downloader', font='Arial 25').grid(row=0, column=0, pady=10, columnspan=2)
Label(root, text='Enter the URL', font='Arial 15').grid(row=1, column=0, columnspan=2)
entry = Entry(root, width=35, font='Arial 15')
entry.grid(row=2, column=0, padx=50, pady=10, columnspan=2)
Button(root, text='Download', font='Arial 12', command=download).grid(row=3, column=0, pady=10, padx=5, sticky='e')
Button(root, text='Download Next', font='Arial 12', command=download_next).grid(row=3, column=1, pady=10, padx=5, sticky='w')

root.mainloop()