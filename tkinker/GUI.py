from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(Tk(), text="Wercie!")
    myLabel.grid(row=2, column=2)

myLabel = Label(root, text="Miłosny test")

myButton = Button(root, text="Kogo kocham?", padx= 5, pady= 20, command= myClick, fg="#000000", bg='#FFFFFF')

myLabel.grid(row=0, column=0)
myButton.grid(row=1, column=1)
root.mainloop()

