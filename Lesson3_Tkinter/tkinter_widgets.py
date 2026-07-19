from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

window=Tk()
window.title("My Image")
window.geometry("300x180")

title=Label(window,text="My profile Card",fg="white",bg="purple",width=40)
title.pack(pady=10)

image=Image.open("rabbit.jpg")
image_file=image.resize((150,100))
photo=ImageTk.PhotoImage(image_file)
pic=Label(window,image=photo)
pic.pack(pady=10)

def show():
    messagebox.showinfo("Great!","You have clicked the pic!")

click_button=Button(window,text="Click the pic!",fg="white",bg="purple",width=40,command=show)
click_button.pack(pady=10)

def show_details():
    top=Toplevel()
    top.title("This is a show button")
    top.geometry("100x50")
    info=Label(top,text="This picture is taken in Switzerland!")
    info.pack(pady=10)

    message=Label(top,text="This picture was taken today!")
    message.pack(pady=10)




show_button=Button(window,text="Show Details",fg="white",bg="purple",width=20,command=show_details)
show_button.pack(pady=5)

window.mainloop()

