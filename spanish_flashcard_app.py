from tkinter import *
import random

class SpanishFlashcard():
    def app(self):
        self.root = Tk()
        self.root.title('Spanish Flashcard')

        self.entry = Entry(self.root, font='Arial 20', justify='center')
        self.entry.grid(row=1, column=0, columnspan=3, pady=10)

        Button(self.root, text='Hint', font='Arial 10', width=7).grid(row=2, column=0, pady=20, sticky='e')
        Button(self.root, text='Submit', font='Arial 10', width=7, command=self.submit).grid(row=2, column=1, pady=20)
        Button(self.root, text='Next', font='Arial 10', width=7, command=self.next).grid(row=2, column=2, pady=20, sticky='w')

        self.label = Label(self.root, font='Arial 15', text='', width=40)
        self.label.grid(row=3, column=0, columnspan=3, pady=(10, 20))

        self.submit_label = Label(self.root, font='Arial 15', text='', width=40)
        self.submit_label.grid(row=4, column=0, columnspan=3, pady=(0, 20))

        self.next()

        self.root.mainloop()

    def next(self):
        self.index = 0
        self.text = ''

        self.entry.delete(0, END)
        self.label.configure(text='')
        self.submit_label.configure(text='')

        spanish_words = ['¿Qué hora tienes?', '¿De dónde viene?', '¿Dónde vives?', '¿Puede ayudarme?', '¿Podría ayudarle?', '¿Cuánto cuesta eso?', '¿Cómo te llamas?', '¿Entiende?', 'Buenas noches', 'Buenos días', 'Buenas tardes', '¿Cómo estás?', '¿Qué tal?', '¿Cómo te va?', '¿Qué haces?', '¿Qué pasa?']
        self.w = random.choice(spanish_words)
        self.list_index = spanish_words.index(self.w)
        Label(self.root, text=''.join(self.w), font='Arial 30', width=20).grid(row=0, column=0, columnspan=3, pady=20)

    def submit(self):
        english_words = ['What time is it?', 'Where are you from?', 'Where do you live?', 'Can you help me?', 'Can I help you?', 'How much does it cost?', 'What is your name?', 'Do you understand?', 'Good night', 'Good morning', 'Good afternoon', 'How are you?', 'How are you?', "How's it going?", 'What are you doing?', "What's happening?"]
        if self.entry.get().capitalize().replace('?', '') == english_words[self.list_index].replace('?', ''):
            result = 'You Won!'
        else:
            result = f'You Lost!\nThe Answer is {english_words[self.list_index]}.'
        self.submit_label.configure(text=result)

SpanishFlashcard().app()