from tkinter import *
from turtle import backward
from PIL import ImageTk, Image

class ImageViewer():
    def app(self):
        # creating main gui window for the app
        self.root = Tk()
        self.root.title('Image Viewer')

        # creating images
        image1 = ImageTk.PhotoImage(Image.open('image_viewer/python_icon.jpg').resize((450,250)))
        image2 = ImageTk.PhotoImage(Image.open('image_viewer/programming_languages.jpeg').resize((450,250)))
        image3 = ImageTk.PhotoImage(Image.open('image_viewer/computer.jpg').resize((450,250)))
        image4 = ImageTk.PhotoImage(Image.open('image_viewer/coding_icon.png').resize((450,250)))
        image5 = ImageTk.PhotoImage(Image.open('image_viewer/artificial_intelligence.jpg').resize((450,250)))
        self.images = [image1, image2, image3, image4, image5]

        # showing the first image on app gui
        self.image = Label(image=image1)
        self.image.grid(columnspan=3, pady=8, padx=8, row=0, column=0)

        # creating for, close and back button
        self.backward_button = Button(self.root, text='<', width=4, state='disabled')
        self.backward_button.grid(row=1, column=0, pady=5)
        Button(self.root, text='Close', width=5, command=self.root.quit).grid(row=1, column=1, pady=5)
        self.forward_button = Button(self.root, text='>', width=4, command=lambda:self.forward(0))
        self.forward_button.grid(row=1, column=2, pady=5)

        self.root.mainloop()

    # to show the next picture
    def forward(self, number):
        self.image.grid_forget()
        self.image = Label(image=self.images[number+1])
        self.image.grid(columnspan=3, pady=8, padx=8, row=0, column=0)
        self.backward_button.configure(command=lambda:self.backward(number-1), state='normal')

        if number + 1 == 4:
            self.forward_button.configure(state='disabled')
            return
        self.forward_button.configure(command=lambda:self.forward(number+1))

    # to show the previous picture
    def backward(self, number):
        self.image.grid_forget()
        self.image = Label(image=self.images[number+1])
        self.image.grid(columnspan=3, pady=8, padx=8, row=0, column=0)
        self.forward_button.configure(command=lambda:self.forward(number+1))

        if number+1 == 0:
            self.backward_button.configure(state='disabled')
            return
        self.backward_button.configure(command=lambda:self.backward(number-1))

ImageViewer().app()