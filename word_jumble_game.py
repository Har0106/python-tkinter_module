from tkinter import *
import random

root = Tk()
root.title('Word Jumble Game')

def word():
    words = ['algorithm', 'argument', 'program', 'conditional', 'declaration', 'framework', 'iteration', 'autonomous', 'statements', 'compiling', 'latency', 'asynchronous', 'backpropagation', 'centroid', 'clustering', 'denoising', 'generalization', 'lambda', 'authentication', 'decryption', 'encryption', 'scareware', 'bootstrap', 'debugging', 'deployment', 'microsoft', 'oracle', 'adobe', 'console']
    w = random.choice(words)
    shuffled_word = random.sample(w, len(w))
    Label(root, text=''.join(shuffled_word), font='Arial 25', width=25).grid(row=0, column=0, columnspan=2, pady=(20, 10))

word()

entry = Entry(root, font='Arial 15')
entry.grid(row=1, column=0, columnspan=2, pady=10)

Button(root, text='Submit', font='Arial 13').grid(row=2, column=0, sticky='e', padx=5, pady=10)
Button(root, text='Next', font='Arial 13', command=word).grid(row=2, column=1, sticky='w', padx=5, pady=10)

label = Label(root, font='Arial 15', text='')
label.grid(row=3, column=0, columnspan=2, pady=(10, 20))

root.mainloop()