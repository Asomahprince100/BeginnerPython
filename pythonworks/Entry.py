from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5, text="What is your name?", fg="teal")
e.pack()
e.insert(0,"Enter your name: ")


def nameDef(event=None):
    display = e.get()
    nameLabel = Label(root, text="Welcome " + display.strip() + "!")
    nameLabel.pack()


e.bind("<Return>", nameDef)

#creating input widgets
NameButton = Button(root, text="what is your name?", command=nameDef)
NameButton.pack()








root.mainloop()