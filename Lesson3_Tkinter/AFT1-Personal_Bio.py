from tkinter import *

window=Tk()
window.title("My Personal Bio")
window.geometry("450x450")
window.config(bg="lavender")

title_label=Label(window,text="My Profile Card",fg="white",bg="purple",width=60)
title_label.grid(row=0,column=0,columnspan=2,padx=10,pady=5)

name_label=Label(window,text="Name",fg="white",bg="purple",width=20)
name_label.grid(row=1,column=0,padx=10,pady=5)

age_label=Label(window,text="Age",fg="white",bg="purple",width=20)
age_label.grid(row=2,column=0,padx=10,pady=5)

hobby_label=Label(window,text="Hobby",fg="white",bg="purple",width=20)
hobby_label.grid(row=3,column=0,padx=10,pady=5)

about_label=Label(window,text="About Me",fg="white",bg="purple",width=20)
about_label.grid(row=4,column=0,padx=10,pady=5)

name_entry=Entry(window,fg="black",bg="white",width=25)
name_entry.grid(row=1,column=1,padx=10,pady=5)

age_entry=Entry(window,fg="black",bg="white",width=25)
age_entry.grid(row=2,column=1,padx=10,pady=5)

hobby_entry=Entry(window,fg="black",bg="white",width=25)
hobby_entry.grid(row=3,column=1,padx=10,pady=5)

about_text=Text(window,fg="black",bg="white",width=23,height=5)
about_text.grid(row=4,column=1,pady=5)



submit_button=Button(window,text="Submit",fg="white",bg="purple",width=25)
submit_button.grid(row=5,column=0,columnspan=2,padx=10,pady=10)

def show_bio():
    name=name_entry.get()
    age=age_entry.get()
    hobby=hobby_entry.get()
    about=about_text.get()

    result_label.config(
        text=f("Hello! My name is {name}. I am {age} years old. I love to do {hobby}. About me:{about}")
    )

submit_button=Button(window,text="Submit",fg="white",bg="purple",width=25,command=show_bio)
submit_button.grid(row=5,column=0,columnspan=2,padx=10,pady=10) 

result_label=Label(window,text="Your bio will appear here!",fg="black",bg="white",width=60,height=15)
result_label.grid(row=7,column=0,columnspan=2,padx=10,pady=10)    
    
    



window.mainloop()




