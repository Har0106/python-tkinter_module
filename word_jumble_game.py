from tkinter import *
import random

class WordJumble():
    def app(self):
        # creating the main gui window of the app
        self.root = Tk()
        self.root.title('Word Jumble Game')

        # to show the first word of the game
        self.word()

        # design of the app
        self.entry = Entry(self.root, font='Arial 20', justify='center')
        self.entry.grid(row=1, column=0, columnspan=3, pady=10)

        Button(self.root, text='Hint', font='Arial 10', width=7, command=self.hint).grid(row=2, column=0, pady=20, sticky='e')
        Button(self.root, text='Submit', font='Arial 10', width=7, command=self.submit).grid(row=2, column=1, pady=20)
        Button(self.root, text='Next', font='Arial 10', command=self.word, width=7).grid(row=2, column=2, pady=20, sticky='w')

        # label to show hints
        self.label = Label(self.root, font='Arial 15', text='', width=40)
        self.label.grid(row=3, column=0, columnspan=3, pady=(10, 20))

        # label to say if the answer is correct or incorrect
        self.submit_label = Label(self.root, font='Arial 15', text='', width=40)
        self.submit_label.grid(row=4, column=0, columnspan=3, pady=(0, 20))

        self.root.mainloop()

    def word(self):
        self.index = 0
        self.text = ''

        # deleting what is already there on the screen letting the exception pass for the first word of game
        try:
            self.entry.delete(0, END)
            self.label.configure(text='')
            self.submit_label.configure(text='')
        except:
            pass

        # choosing a word from the list and shuffling it
        words = ['algorithm', 'argument', 'program', 'conditional', 'declaration', 'framework', 'iteration', 'autonomous', 'statements', 'compiling', 'latency', 'asynchronous', 'backpropagation', 'centroid', 'clustering', 'denoising', 'generalization', 'lambda', 'authentication', 'decryption', 'encryption', 'scareware', 'bootstrap', 'debugging', 'deployment', 'microsoft', 'oracle', 'adobe', 'console']
        self.w = random.choice(words).upper()
        self.shuffled_word = random.sample(self.w, len(self.w))
        Label(self.root, text=''.join(self.shuffled_word), font='Arial 30', width=20).grid(row=0, column=0, columnspan=3, pady=(20, 10))

    # showing if the answer is correct or incorrect
    def submit(self):
        if self.entry.get().upper() == self.w:
            result = 'You Won!'
        else:
            result = f'You Lost!\nThe Word is {self.w.capitalize()}.'
        self.submit_label.configure(text=result)

    # showing the letters of word as the hint
    def hint(self):
        if self.index < len(self.w)-1:
            self.text += f'{self.w[self.index].capitalize()} '
            self.label.configure(text=self.text)
            self.index += 1
        else:
            self.submit_label.configure(text=f'You Lost!\nThe Word is {self.w.capitalize()}.')

WordJumble().app()