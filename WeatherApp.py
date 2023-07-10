import tkinter as tk
root = tk.Tk()
root.geometry("600x400")

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()
entry1 = tk.Entry(root) 
canvas1.create_window(300, 140, window=entry1)
entry2 = tk.Entry(root) 
canvas1.create_window(100, 140, window=entry2)

request = tk.Button(root, text = "Request", bd = 5, command = root.destroy)

request.place(x=200, y=50)




root.mainloop()

