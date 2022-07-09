from tkinter import *
import pyttsx3

root = Tk()
root.title('Make Your Computer Speak')

engine = pyttsx3.init()

def speak():
    engine.say(entry.get())
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)
    engine.save_to_file(entry.get(), 'speak.mp3')
    engine.runAndWait()

entry = Entry(root)
entry.pack()

button = Button(root, text='Speak', command=speak)
button.pack()

root.mainloop()