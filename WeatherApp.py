import tkinter as tk
import requests
import sqlite3
import json

root = tk.Tk()
#set screeen
root.geometry('600x400')
root.title('Weather app')


#create table 
def createtable():
    try:
        connection_obj = sqlite3.connect('weather.db')
        sql_weather = '''CREATE TABLE IF NOT EXISTS WEATHER (
            id integer PRIMARY KEY,
            lat text NOT NULL,
            lon text NOT NULL,
            Wind text NOT NULL,
            Rain text NOT NULL,
            name text
            UNIQUE (id)
        );'''
        
        cursor = connection_obj.cursor()
        print("Successfully connected")
        cursor.execute(sql_weather)
        connection_obj.commit()
        print("SQLite table created")

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table",error)
    finally:
        if connection_obj:
            connection_obj.close()
            print("sqlite connection is closed")
createtable()
#syntax error??

#finding previous entry
def max1():
    sqliteconnection = sqlite3.connect('weather.db')
    cursor = sqliteconnection.cursor()
    maxvalue = ('SELECT MAX (id) FROM WEATHER')
    cursor.execute(maxvalue)
    result = cursor.fetchall()
    maxv = (result[0][0]+1)
    return maxv

#no errors

#function for api
def submit():
    lat = lat_entry.get()
    lon = lon_entry.get()
    #search api
    data1 = requests.get('https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=74109a70b2f459c87c25409811f4e6be'.format(lat,lon))
    json_data = data1.json()
    wSpeed=json_data['wind']['speed']
    location = json_data['name']
    rainDescription = json_data['weather'][0]['main']

    x=max1()
    selectrecord(x)
    #inserting into table
    insertVaribleIntoTable(x,lat, lon, wSpeed, rainDescription, location)

    #printing record
    
#wind error

#setting latitude and longitude variables
lon = tk.StringVar()
lat = tk.StringVar()
#input boxes and labels
lon_label = tk.Label(root, text = 'Longitude', font=('calibre',10, 'bold'))
lon_entry = tk.Entry(root,textvariable = lon, font=('calibre',10,'normal'))
  
lat_label = tk.Label(root, text = 'Latitude', font = ('calibre',10,'bold'))
lat_entry=tk.Entry(root, textvariable = lat, font = ('calibre',10,'normal'))

#positioning 
lon_label.grid(row=0,column=0)
lon_entry.grid(row=0,column=1)
lat_label.grid(row=1,column=0)
lat_entry.grid(row=1,column=1)
#no errors

# insert variables into table
def insertVaribleIntoTable(id, lon, lat, wSpeed, rainDescription, location):
    try:
        sqliteConnection = sqlite3.connect('weather.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO WEATHER
                          (id, lon, lat, Wind, Rain, name) 
                          VALUES (?, ?, ?, ?, ?,?);"""

        data_tuple = (id, lon, lat, wSpeed,rainDescription,location)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into weather table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")      


#print table contents
def selectrecord(x):
    sqliteconnection = sqlite3.connect('weather.db')
    cursor = sqliteconnection.cursor()
    #printing out values in table
    y= x-5
    for i in range (x,y):
        cursor.execute('SELECT * FROM WEATHER WHERE ID={}'.format(i))
        rainresult = cursor.fetchall()
        print (rainresult)


#request button
sub_btn=tk.Button(root,text = 'Request', command = submit)
sub_btn.grid(row=2,column=1)

root.mainloop()