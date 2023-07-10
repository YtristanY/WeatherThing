import tkinter as tk
root = tk.Tk()

#text input
canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()
entry1 = tk.Entry(root) 
canvas1.create_window(100, 40, window=entry1)
entry1 = tk.Entry(root) 
canvas1.create_window(100, 140, window=entry1)

#button
request = tk.Button(root, text = "Request", bd = 5, command = root.destroy)

request.pack(side = 'top')

root.mainloop()

hello
