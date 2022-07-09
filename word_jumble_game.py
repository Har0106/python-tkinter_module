from tkinter import *
import random

root = Tk()
root.title('Word Jumble Game')

def word():
    global w
    global index
    global text

    index = 0
    text = ''
    try:
        entry.delete(0, END)
        label.configure(text='')
        submit_label.configure(text='')
    except:
        pass
    words = ['algorithm', 'argument', 'program', 'conditional', 'declaration', 'framework', 'iteration', 'autonomous', 'statements', 'compiling', 'latency', 'asynchronous', 'backpropagation', 'centroid', 'clustering', 'denoising', 'generalization', 'lambda', 'authentication', 'decryption', 'encryption', 'scareware', 'bootstrap', 'debugging', 'deployment', 'microsoft', 'oracle', 'adobe', 'console']
    w = random.choice(words).upper()
    shuffled_word = random.sample(w, len(w))
    Label(root, text=''.join(shuffled_word), font='Arial 30', width=20).grid(row=0, column=0, columnspan=3, pady=(20, 10))

def submit():
    global submit_label
    if entry.get().upper() == w:
        result = 'You Won!'
    else:
        result = f'You Lost!\nThe Word is {w.capitalize()}.'
    submit_label.configure(text=result)

def hint():
    global index
    global text
    if index < len(w)-1:
        text += f'{w[index].capitalize()} '
        label.configure(text=text)
        index += 1
    else:
        submit_label.configure(text=f'You Lost!\nThe Word is {w.capitalize()}.')

word()

entry = Entry(root, font='Arial 20', justify='center')
entry.grid(row=1, column=0, columnspan=3, pady=10)

Button(root, text='Hint', font='Arial 10', width=7, command=hint).grid(row=2, column=0, pady=20, sticky='e')
Button(root, text='Submit', font='Arial 10', width=7, command=submit).grid(row=2, column=1, pady=20)
Button(root, text='Next', font='Arial 10', command=word, width=7).grid(row=2, column=2, pady=20, sticky='w')

global label
label = Label(root, font='Arial 15', text='', width=40)
label.grid(row=3, column=0, columnspan=3, pady=(10, 20))

global submit_label
submit_label = Label(root, font='Arial 15', text='', width=40)
submit_label.grid(row=4, column=0, columnspan=3, pady=(0, 20))

root.mainloop()