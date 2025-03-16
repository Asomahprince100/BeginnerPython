from tkinter import *

root = Tk()


#creating a function
def ClickMe():
    myLabel = Label(root, text="You Just clicked").pack()


#creating a button widget
myButton = Button(root,fg="orange", bg="black", text="Click Me!", state=NORMAL, padx=50, pady= 5, command=ClickMe).pack()






root.mainloop()