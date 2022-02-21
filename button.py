#hesap makinesi

from tkinter import *

def topla():
    b1= int(buton1.get())
    b2=int(buton2.get())
    sonuc['text']=str(b1+b2)
def cikar():
    b1= int(buton1.get())
    b2=int(buton2.get())
    sonuc['text']=str(b1-b2)
def carp():
    b1= int(buton1.get())
    b2=int(buton2.get())
    sonuc['text']=str(b1*b2)
def bol():
    b1= float(buton1.get())
    b2=float(buton2.get())
    sonuc['text']=str(b1/b2)

#pencere
window=Tk()
window.geometry("400x200+500+200")
window.title("Hesap Makinesi")

buton1=Entry(width=15) #width>entry nin genişliği
buton1.place(x=20,y=20)

buton2=Entry(width=15) #width>entry nin genişliği
buton2.place(x=150,y=20)

sonuc=Label(text="Sonuc",bg="white")
sonuc.place(x=280,y=20)

btopla=Button(text="+",command=topla).place(x=20,y=50)
bcikar=Button(text="-",command=cikar).place(x=50,y=50)
bcarp=Button(text="x",command=carp).place(x=80,y=50)
bbol=Button(text="/",command=bol).place(x=110,y=50)

window.mainloop()