from tkinter import *
window = Tk()
window.geometry("500x400+10+10")
window.title("My First GUI")

btn1 = Button(window, text="Click Me", fg="Yellow", bg="Black")
btn1.place(x=210, y=195)

txtfld = Entry(window, border=10)
txtfld.place(x=1, y=1)

lbl = Label(window, text="My first Demo", font="Verdana")
lbl.place(x=1, y=45)

window.mainloop()