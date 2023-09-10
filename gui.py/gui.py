from tkinter import *
from PIL import Image , ImageTk
#to create base
anjaliprajapati_root = Tk()
# for frame
anjaliprajapati_root.geometry("644x434")
#minsize
anjaliprajapati_root.minsize(200,98)
 #maxsize
anjaliprajapati_root.maxsize(1900,1000)

me=Label(text="WELCOME TO MY GUI")
me.pack()
#photo=PhotoImage(file="1.")
image=Image.open("mine.jpg")
photo=ImageTk.photoImage(image)
x_label=Label(image=photo)
x_label.pack()

# gui logic hare
# make intract to user
anjaliprajapati_root.mainloop()
