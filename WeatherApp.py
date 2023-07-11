import tkinter as tk
import requests
import sqlite3
import json



root = tk.Tk()
#set screeen
root.geometry('600x400')
root.title('Weather app')



#function for api
def submit():
    lat = lat_entry.get()
    lon = lon_entry.get()
    data1 = requests.get('https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=74109a70b2f459c87c25409811f4e6be'.format(lat,lon))
    json_data = data1.json()
    wSpeed=json_data['wind']['speed']
    location = json_data['name']
    rainDescription = json_data['weather'][0]['main']



    return lat,lon,wSpeed,rainDescription,location




lon = tk.StringVar()
lat = tk.StringVar()

lon_label = tk.Label(root, text = 'Longitude', font=('calibre',10, 'bold'))
lon_entry = tk.Entry(root,textvariable = lon, font=('calibre',10,'normal'))
  
lat_label = tk.Label(root, text = 'Latitude', font = ('calibre',10,'bold'))
lat_entry=tk.Entry(root, textvariable = lat, font = ('calibre',10,'normal'))

#button
sub_btn=tk.Button(root,text = 'Request', command = submit)

#positioning 
lon_label.grid(row=0,column=0)
lon_entry.grid(row=0,column=1)
lat_label.grid(row=1,column=0)
lat_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)




# #function for creating table
# def table1():
#     for i in range(total_rows):
#                 for j in range(total_columns):
                    
#                     e = tk.Entry(root, width=15, fg='blue',
#                                 font=('Arial',16,'bold'))
                    
#                     e.grid(row=i+15, column=j)
#                     e.insert(tk.END, lst[i][j])
 
# # take the data
# lst = [('','Lon','Lat','Rain Description','Windspeed','Location Name'),
#        (1,'','','','',''),
#        (2,'','','','',''),
#        (3,'','','','',''),
#        (4,'','','','',''),
#        (5, '','','','','')]
  
# # find total number of rows and
# # columns in list
# total_rows = len(lst)
# total_columns = len(lst[0])

# table1()


#create sqlite3 table 
# try:
#     connection_obj = sqlite3.connect('weather.db')
#     sql_weather = '''CREATE TABLE WEATHER (
#         id integer PRIMARY KEY,
#         lat text NOT NULL,
#         lon text NOT NULL,
#         Wind text NOT NULL,
#         Rain Description text NOT NULL,
#         name text);'''
#     cursor = connection_obj.cursor()
#     print("Successfully connected")
#     cursor.execute(sql_weather)
#     connection_obj.commit()
#     print("SQLite table created")

#     cursor.close()

# except sqlite3.Error as error:
#     print("Error while creatiing a sqlite table",error)
# finally:
#     if connection_obj:
#         connection_obj.close()
#         print("sqlite connection is closed")
def insertvariables(id, lat, lon, Wind, Rain, Name):

    try:
        sqliteconnection = sqlite3.connect('weather.db')
        cursor = sqliteconnection.cursor()
        print("Sucessfully connected")

        query = ''' INSERT INTO weather
                (id,lat, lon, Wind, Rain Description,name) 
                VALUES (?,?,?,?,?,?)'''
        data_tuple = (id, lat, lon, Wind, Rain, Name)
        cursor.execute(query data_tuple)
        sqliteconnection.commit()
        print("Successful")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert",error)
    finally:
        if sqliteconnection:
            sqliteconnection.close()
            print("The connection is closed")

insertvariables(1,lat, lon, wSpeed, rainDescription, location)


root.mainloop()