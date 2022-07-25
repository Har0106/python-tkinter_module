from tkinter import *
import random

class SpanishFlashcard():
    def app(self):
        # main gui window of the project
        self.root = Tk()
        self.root.title('Spanish Flashcard')

        # entry box for the user to enter the answer
        self.entry = Entry(self.root, font='Arial 20', justify='center')
        self.entry.grid(row=1, column=0, columnspan=3, pady=10)

        # hint, submit and next buttons 
        Button(self.root, text='Hint', font='Arial 10', width=7, command=self.hint).grid(row=2, column=0, pady=20, sticky='e')
        Button(self.root, text='Submit', font='Arial 10', width=7, command=self.submit).grid(row=2, column=1, pady=20)
        Button(self.root, text='Next', font='Arial 10', width=7, command=self.next).grid(row=2, column=2, pady=20, sticky='w')

        # label to show hind
        self.label = Label(self.root, font='Arial 15', text='', width=40)
        self.label.grid(row=3, column=0, columnspan=3, pady=(10, 20))

        # label to show the result and the correct answer
        self.submit_label = Label(self.root, font='Arial 15', text='', width=40)
        self.submit_label.grid(row=4, column=0, columnspan=3, pady=(0, 20))

        # showing the first word on window
        self.next()

        self.root.mainloop()

    def next(self):
        self.index = 0
        self.text = ''

        # delete what is already in entry box and labels
        self.entry.delete(0, END)
        self.label.configure(text='')
        self.submit_label.configure(text='')

        # spanish words and it's english meanings
        spanish_words = ['¿Qué hora tienes?', '¿De dónde viene?', '¿Dónde vives?', '¿Puede ayudarme?', '¿Podría ayudarle?', '¿Cuánto cuesta eso?', '¿Cómo te llamas?', '¿Entiende?', 'Buenas noches', 'Buenos días', 'Buenas tardes', '¿Cómo estás?', '¿Qué tal?', '¿Cómo te va?', '¿Qué haces?', '¿Qué pasa?']
        english_words = ['What time is it?', 'Where are you from?', 'Where do you live?', 'Can you help me?', 'Can I help you?', 'How much does it cost?', 'What is your name?', 'Do you understand?', 'Good night', 'Good morning', 'Good afternoon', 'How are you?', 'How are you?', "How's it going?", 'What are you doing?', "What's happening?"]

        # choosing a word and showing it on screen
        word = random.choice(spanish_words)
        Label(self.root, text=word, font='Arial 30', width=20).grid(row=0, column=0, columnspan=3, pady=20)

        # getting the answer
        self.ans = english_words[spanish_words.index(word)]

    def submit(self):
        # checking if the answer of the user is correct
        if self.entry.get().capitalize().replace('?', '') == self.ans.replace('?', ''):
            result = 'You Won!'
        else:
            result = f'You Lost!\nThe Answer is {self.ans}.'
        self.submit_label.configure(text=result)

    def hint(self):
        # showing the letters of the word one by one when hint is asked
        if self.index < len(self.ans)-2:
            self.text += f'{self.ans[self.index].capitalize()} '
            self.label.configure(text=self.text)
            self.index += 1
        else:
            # showing the answer if the word before last word is asked in hint
            self.submit_label.configure(text=f'You Lost!\nThe Answer is {self.ans.capitalize()}.')

SpanishFlashcard().app()