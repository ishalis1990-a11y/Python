from tkinter import *

window=Tk()
window.title("My Profile Card")
window.geometry("400x300")

title=Label(window,text="My Profile Card",fg="white",bg="purple",width=40)
title.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

name=Label(window,text="Name",fg="black",bg="white")
name.grid(row=1,column=0,padx=10,pady=5)

hobby=Label(window,text="Hobby",fg="black",bg="white")
hobby.grid(row=2,column=0,padx=10,pady=5)

name_entry=Entry(window,fg="black",bg="white",width=25)
name_entry.grid(row=1,column=1,padx=10,pady=5)

hobby_entry=Entry(window,fg="black",bg="white",width=25)
hobby_entry.grid(row=2,column=1,padx=10,pady=5)

about_frame=Frame(window,relief="flat",borderwidth=3)
about_frame.grid(row=3,column=0,columnspan=2,padx=10,pady=5)

about_label=Label(about_frame,text="About Me",fg="black",bg="white")
about_label.pack()

about_text=Text(about_frame,fg="black",bg="white",width=30,height=5)
about_text.pack()

submit_button=Button(window,text="Submit",fg="white",bg="purple",width=40)
submit_button.grid(row=4,column=0,columnspan=2,padx=10,pady=10)



window.mainloop()