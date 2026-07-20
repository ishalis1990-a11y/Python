from tkinter imoprt *
from tkinter import messagebox
from PIL import Image,ImageTk

window=Tk()
window.title("My Photo Album")
window.geometry("300x180")
window.config(bg="lavender")

title_label=Label(window,text="My Photo Album",fg="black",bg="aqua",width=60)
title_label.pack(pady=10)

image=Image.open(place.jpg)
image_file=image.resize((150,100))
photo=ImageTk.PhotoImage(image_file)
pic=Label(window,image=photo)
pic.pack(pady=10)

def show():
    messagebox.showinfo("Hurray!","You have clicked the image!")

show_button=Button(window,text="Click the pic!",fg="black",bg="aqua",command=show) 
show_button.pack(pady=10)

def show_details():
    top=Toplevel()
    top.title("Details")
    top.geometry=("150x90")

    title=Label(top,text="Details",fg="black",bg="aqua",width=15)
    title.pack(pady=10)

    info=Label(top,text="This picture is taken in a famous place")
    info.pack(pady=10)

    message=Label(top,text="This picture was taken today!")
    message.pack(pady=10)

def close():
    top.destroy()    

    close_button=Button(top,text"Close",command=close)
    close_button.pack(pady=10)

details_button=Button(window,text="Click the pic!",fg="black",bg="aqua",command=show_details) 
details_button.pack(pady=10)   

window.mainloop()
    