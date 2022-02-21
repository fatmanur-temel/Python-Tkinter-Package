from tkinter import *

window=Tk()
window.geometry("500x300+500+200")

label1=Label(text="etiket 1",font="Verdana 22",bg="red",fg="black")
label1.grid(row=0,column=0)

label2=Label(text="etiket 2",font="Verdana 22",bg="gray",fg="black")
label2.grid(row=1,column=0)

label3=Label(text="etiket 3",font="Verdana 22",bg="blue",fg="black")
label3.grid(row=1,column=1)

window.mainloop()