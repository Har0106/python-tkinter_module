from tkinter import *

root = Tk()
root.title('Untiled - Notepad')

frame = Frame(root)
frame.pack()

text = Text(frame, font='Consolas 15')
text.pack()

root.mainloop()