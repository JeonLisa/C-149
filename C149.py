from tkinter import *
import random
root=Tk()
root.title("Lucky Friend Wheel")
root.geometry("400x400")
label_1=Label(root)
list_1=["Sriya","Rishika","Suneeti","Aira","Devi","Krithi"]
def Spin():
    random_num=random.randint(0,5)
    random_luck=list_1[random_num]
    label_1["text"]=" That Lucky Friend Is "+random_luck
    print(random_luck)
button_1=Button(root,text="Spin The Wheel",command=Spin)
label_1.place(relx=0.5,rely=0.7,anchor=CENTER)
button_1.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()
