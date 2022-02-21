from tkinter import *

window=Tk()
window.geometry("500x300+500+200")

label1=Label(text="etiket 1")
label1['font']="Verdana 22"
label1['bg']="red"
label1['fg']="black"
label1.pack(side="left") #top,left,right,bottom

label2=Label(text="etiket 2",font="Verdana 22",bg="gray",fg="black")
label2.pack(fill="y") #x,y

label3=Label(text="etiket 3",font="Verdana 22",bg="blue",fg="black")
label3.pack(expand="yes") #yes,no

window.mainloop()