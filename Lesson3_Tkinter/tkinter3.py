from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

window=Tk()
window.title("Denomination Calculator")
window.geometry("600x400")

image=Image.open("money.png")
image_file=image.resize((300,300))
photo=ImageTk.PhotoImage(image_file)
pic=Label(window,image=photo)
pic.place(x=100,y=50)

title_label=Label(window,text="This is a denomination app",fg="white",bg="red",width=50)
title_label.place(x=100,y=340)

def click():
    msg_box=messagebox.showinfo("Alert","Do you want to use the denomination calculator?")
    if msg_box=="ok":
        topwin()

def topwin():
    top=Toplevel()
    top.title("Denomination Calculator")
    top.geometry("600x450") 

    amount_label=Label(top,text="Enter the  total amount")
    amount_label.place(x=140,y=50)

    amount_entry=Entry(top)
    amount_entry.place(x=140,y=80)

    declaration_label=Label(top,text="Here are the denomination notes for the amount you have entered")
    declaration_label.place(x=140,y=120) 

    l1=Label(top,text="2000")
    l1.place(x=50,y=170) 

    l2=Label(top,text="500") 
    l2.place(x=50,y=220) 

    l3=Label(top,text="100")
    l3.place(x=50,y=260) 

    e1=Entry(top)
    e1.place(x=100,y=170)
    e2=Entry(top)
    e2.place(x=100,y=220)
    e3=Entry(top)
    e3.place(x=100,y=260) 

    

    def calculator():
        try:
            amount=int(amount_entry.get())
            note_2000=amount//2000
            amount=amount%2000
            note_500=amount//500
            amount=amount%500
            note_100=amount//100

            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)

            e1.insert(END,str(note_2000))
            e2.insert(END,str(note_500))
            e3.insert(END,str(note_100))

        except:
            messagebox.showerror("Alert","The entered value is not numeric! Please enter a number!")

     
            


        
    calculate_button=Button(top,text="Calculate",fg="white",bg="red",width=30,command=calculator)  
    calculate_button.place(x=320,y=220) 

         
       
    
click_button=Button(window,text="Click the button",fg="white",bg="red",command=click)
click_button.place(x=230,y=370)


window.mainloop()

