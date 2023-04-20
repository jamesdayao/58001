from tkinter import*
win = Tk()

lbl = Label(win, text="Gender")
lbl.place(relx=5, rely=5)
lbl.pack(anchor="center")

var1 = IntVar()
var2 = IntVar()
r1 = Radiobutton(win, text="Male", variable=var1)
r2 = Radiobutton(win, text="Female", variable=var2)
r1.place(x=20,y=50)
r2.place(x=20,y=70)

chk1 = Checkbutton(win, text=" 100 - 199")
chk2 = Checkbutton(win, text=" 200 - 299")
chk3 = Checkbutton(win, text=" 300 - 399")
chk1.place(x=40, y=90)
chk2.place(x=40, y=120)
chk3.place(x=40, y=150)

lbl2 = Label(win, text="List of Fruits")
lbl2.place(x=50, y=180)

lst = Listbox(win, selectmode=SINGLE)
lst.insert(1, "Mango")
lst.insert(2, "Orange")
lst.insert(3, "Apple")
lst.place(x=50, y=200)

win.geometry("500x400+10+10")
win.mainloop()