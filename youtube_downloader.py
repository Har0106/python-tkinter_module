from tkinter import *

root = Tk()
root.title('Youtube Downloader')

def download():
    pass

Label(root, text='YouTube Downloader', font='Arial 25').grid(row=0, column=0, pady=10)
entry = Entry(root, width=30, font='Arial 15')
entry.grid(row=1, column=0, padx=75, pady=10)
Button(root, text='Download', font='Arial 12').grid(row=2, column=0, pady=10)

root.mainloop()