from tkinter import*

def toplama():
    e1 = int(entry1.get())
    e2 = int(entry2.get())
    label5['text']=str(e1+e2)

def cikarma():
    e1 = int(entry1.get())
    e2 = int(entry2.get())
    label5['text']=str(e1-e2)

def carpma():
    e1 = int(entry1.get())
    e2 = int(entry2.get())
    label5['text']=str(e1*e2)

def bolme():
    e1 = float(entry1.get())
    e2 = float(entry2.get())
    label5['text']=str(e1/e2)

window = Tk()
window.title("Hesap Makinesi")
window.geometry("350x200+600+200")

label1 = Label(window)
label1.config(text="Birinci sayı:",font="bold 9",fg="purple")
label1.place(x=10,y=10)

entry1 = Entry(window)
entry1.config(width=5)
entry1.place(x=10,y=40)


label2 = Label(window)
label2.config(text="İkinci sayı:",font="bold 9",fg="purple")
label2.place(x=100,y=10)

entry2 = Entry(window)
entry2.config(width=5)
entry2.place(x=100,y=40)

label3 = Label(window)
label3.config(text="Yapılacak İşlem:")
label3.place(x=10,y=80)

buton1 = Button(window)
buton1.config(text="+",command=toplama)
buton1.place(x=10,y=110)

buton2 = Button(window)
buton2.config(text="-",command=cikarma)
buton2.place(x=40,y=110)

buton3 = Button(window)
buton3.config(text="x",command=carpma)
buton3.place(x=70,y=110)

buton4 = Button(window)
buton4.config(text="/",command=bolme)
buton4.place(x=100,y=110)


label4 = Label(window)
label4.config(text="Sonuç:",bg="purple")
label4.place(x=200,y=10)

label5 = Label(window)
label5.config(text="")
label5.place(x=200,y=40)


window.mainloop()