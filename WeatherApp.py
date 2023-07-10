from tkinter import *

root = Tk()

root.geometry('250x250')

request = Button(root, text = "Request", bd = 5, command = root.destroy)

request.pack(side = 'top')

root.mainloop()

