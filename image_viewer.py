from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')

image1 = ImageTk.PhotoImage(Image.open('images/python_icon.jpg').resize((450,250)))
image2 = ImageTk.PhotoImage(Image.open('images/programming_languages.jpeg').resize((450,250)))
image3 = ImageTk.PhotoImage(Image.open('images/computer.jpg').resize((450,250)))
image4 = ImageTk.PhotoImage(Image.open('images/coding_icon.png').resize((450,250)))
image5 = ImageTk.PhotoImage(Image.open('images/artificial_intelligence.jpg').resize((450,250)))
images = [image1, image2, image3, image4, image5]

image = Label(image=image1)
image.grid(columnspan=3, pady=8, padx=8, row=0, column=0)

def forward(number):
    global image
    
    image.grid_forget()
    image = Label(image=images[number+1])
    image.grid(columnspan=3, pady=8, padx=8, row=0, column=0)

    if number + 1 == 4:
        button_forward = Button(root, text='>', width=4, state='disabled', command=lambda:forward(number+1)).grid(row=1, column=2, pady=5)
        return
    button_forward = Button(root, text='>', width=4, command=lambda:forward(number+1)).grid(row=1, column=2, pady=5)


button_backward = Button(root, text='<', width=4).grid(row=1, column=0, pady=5)
button_close = Button(root, text='Close', width=5, command=root.quit).grid(row=1, column=1, pady=5)
button_forward = Button(root, text='>', width=4, command=lambda:forward(0)).grid(row=1, column=2, pady=5)

root.mainloop()