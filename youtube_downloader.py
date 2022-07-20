from tkinter import *
from pytube import YouTube
from tkinter import messagebox

# main gui window of the app
root = Tk()
root.title('YouTube Downloader')

# getting the link and downloading it
def download():
    try:
        y = YouTube(entry.get())
        video = y.streams.get_highest_resolution()
        try:
            video.download(path.get())
            label.configure(text='Downloaded!')
        except:
            messagebox.showerror('Error', "Couldn't download the video")
    except:
        messagebox.showinfo('Error', "Couldn't download the video")

# deleting the link in the entry widget
def download_next():
    entry.delete(0, END)
    label.configure(text='')

# design of the app
Label(root, text='YouTube Downloader', font='Arial 25').grid(row=0, column=0, pady=10, columnspan=2)

Label(root, text='Enter the URL', font='Arial 15').grid(row=1, column=0, columnspan=2)
entry = Entry(root, width=35, font='Arial 15')
entry.grid(row=2, column=0, padx=50, pady=10, columnspan=2)

Label(root, text='Enter the destination', font='Arial 15').grid(row=3, column=0, columnspan=2)
path = Entry(root, width=35, font='Arial 15')
path.grid(row=4, column=0, padx=50, pady=10, columnspan=2)

Button(root, text='Download', font='Arial 12', command=download).grid(row=5, column=0, pady=5, padx=5, sticky='e')
Button(root, text='Download Next', font='Arial 12', command=download_next).grid(row=5, column=1, pady=5, padx=5, sticky='w')

label = Label(root, text='', font='Arial 14')
label.grid(row=6, column=0, pady=(5,10), columnspan=2)

root.mainloop()