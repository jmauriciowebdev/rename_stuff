import os, sys, glob
from tkinter import *


def lastly():
    a = txt.get()
    b = txt2.get()
    print("Replacing ", a , " with " , b)
    files = glob.glob("*")
    for f in files:
        if ".py" not in f:
                n = f.replace(str(a),str(b))
                os.rename(f,n)


root = Tk()
root.title("Rename Stuff")
root.geometry("600x100")





lbl = Label(root, text="Rename")
lbl.grid(column=0, row=3)
txt = Entry(root,width=20)
txt.grid(column=1, row=3)
lbl2 = Label(root, text="to")
lbl2.grid(column=2, row=3)
txt2 = Entry(root,width=20)
txt2.grid(column=3, row=3)

btn = Button(root, text="Now", command=lastly)
btn.grid(column=4, row=3)


root.mainloop()