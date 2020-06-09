from tkinter import *
# tkinter does not support much of the image types and there we will be using PIL(python image library) now known to be as PILLOW
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code')
# Add Icon to program, pass the path of image
#img = PhotoImage(file='index.png')
#root.tk.call('wm', 'iconphoto', root._w, img)

my_img = ImageTk.PhotoImage(Image.open("logos/insta.png"))
my_label = Label(image = my_img)
my_label.grid(row = 0, column = 0)


def onClick():
    # Used for clearing the grid or removing that widget
    my_label.grid_forget()
    
butto = Button(root, text = 'remove img',command = onClick).grid(row=1,column=0)

button_quit = Button(root, text='Exit Program', command = root.quit).grid(row=3,column=0)
root.mainloop()
