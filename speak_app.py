from tkinter import *
import pyttsx3

root = Tk()
root.title('Make Your Computer Speak')

engine = pyttsx3.init()

def gen_set():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[gen.get()].id)

def save():
    gen_set()
    engine.save_to_file(entry.get(), entry_filename.get()+'.mp3')
    Label(root, text='Saved!', font='Arial 15').grid(row=6, column=0, columnspan=2, pady=(10, 20))
    engine.runAndWait()

def speak():
    gen_set()
    engine.say(entry.get())
    engine.runAndWait()

Label(root, text='Speak!', font='Arial 25').grid(row=0, column=0, columnspan=2, pady=10)

entry = Entry(root, font='Arial 15')
entry.grid(row=1, column=0, columnspan=2, pady=10, padx=50)

gen = IntVar()
Radiobutton(root, text='Male', variable=gen, value=0, font='Arial 13').grid(row=2, column=0, pady=10, padx=5, sticky='e')
Radiobutton(root, text='Female', variable=gen, value=1, font='Arial 13').grid(row=2, column=1, pady=10, padx=5, sticky='w')

Button(root, text='Speak', command=speak, font='Arial 13').grid(row=3, column=0, columnspan=2, pady=10)

entry_filename = Entry(root, font='Arial 15')
entry_filename.grid(row=4, column=0, columnspan=2, pady=10)

Button(root, text='Save', command=save, font='Arial 13').grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()