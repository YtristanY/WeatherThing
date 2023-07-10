import tkinter as tk
import requests

root = tk.Tk()
#set screeen
root.geometry('600x400')
root.title('Weather app')

#text input
lon_label = tk.Label(root, text = 'Longitude', font=('calibre',10, 'bold'))
canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()
entry1 = tk.Entry(root) 
canvas1.create_window(200, 100, window=entry1)

lat_label = tk.Label(root, text = 'Latitude', font=('calibre',10, 'bold'))
canvas2 = tk.Canvas(root, width=400, height=300)
canvas2.pack()
entry2 = tk.Entry(root) 
canvas2.create_window(200, 200, window=entry1)

#function for api
def submit():
    lat = entry1.get()
    lon = entry2.get()
    data = requests.get('https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=74109a70b2f459c87c25409811f4e6be'.format(lat,lon))
    print(data)

#button
request = tk.Button(root, text = "Request", bd = 5, command = submit())
request.place(x = 200, y = 20)


root.mainloop()