from tkinter import *

window=Tk()
window.title("Frame")
window.geometry("500x300+500+200")

fgray=Frame(bg="gray",width=200,height=100)
fgray.place(x=20,y=40)
#Frame içine buton ekleme
b1=Button(fgray, text="Gri Frame Butonu")
b1.place(x=0,y=0)

fblack=Frame(bg="black",width=200,height=100)
fblack.place(x=250,y=40)

label=LabelFrame(text="Etiketli Frame",width=200,height=100)
label.place(x=20,y=150)
#LabelFrame içine buton ekleme
b2=Button(label, text="LabelFrame Butonu")
b2.place(x=10,y=10)

window.mainloop()