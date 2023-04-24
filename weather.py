from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


root = Tk()
root.title('Weather app')
root.geometry('900x500+300+200')
root.resizable(False, False)


def getweather():
    try:

        city = textfield.get()

        geolocator = Nominatim(user_agent='geoapiExercises')
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        # print(location.latitude, location.longitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime('%I:%M %p')
        clock.config(text=current_time)
        name.config(text='CURRENT WEATHER')
        lat = str(location.latitude)
        lon = str(location.longitude)

        # weather
        api = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + \
              lon + "&appid=cd283637632abf2f8d752bf9b79b9426"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(condition, '|', 'FEELS', 'LIKE', temp, '°'))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception:
        messagebox.showerror("Weather app", "Invalid Entry!")


# search box
search_image = PhotoImage(file='search.png')
myimage = Label(image=search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify='center', width=17, font=('poppins', 25, 'bold'), bg="#1a1919", border=0, fg='white')
textfield.place(x=50, y=40)
textfield.focus()

search_icon = PhotoImage(file='search_icon.png')
myimage_icon = Button(image=search_icon, borderwidth=0, cursor='hand2', bg='#1a1919', command=getweather)
myimage_icon.place(x=400, y=32)

# logo
logo_image = PhotoImage(file='logo.png')
logo = Label(image=logo_image)
logo.place(x=150, y=100)

# bottom box
frame_image = PhotoImage(file='box.png')
frame_myimage = Label(image=frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# time
name = Label(root, font=('arial', 15, 'bold'))
name.place(x=30, y=100)
clock = Label(root, font=('Helvetica', 20))
clock.place(x=30, y=130)

# label
label_1 = Label(root, text='WIND', font=('Helvetica', 15, 'bold'), fg='white', bg='#13a1d6')
label_1.place(x=120, y=400)

label_2 = Label(root, text='HUMIDITY', font=('Helvetica', 15, 'bold'), fg='white', bg='#13a1d6')
label_2.place(x=250, y=400)

label_3 = Label(root, text='DESCRIPTION', font=('Helvetica', 15, 'bold'), fg='white', bg='#13a1d6')
label_3.place(x=430, y=400)

label_4 = Label(root, text='PRESSURE', font=('Helvetica', 15, 'bold'), fg='white', bg='#13a1d6')
label_4.place(x=650, y=400)

t = Label(font=('arial', 70, 'bold'), fg='#13a1d6')
t.place(x=400, y=150)
c = Label(font=('arial', 15, 'bold'))
c.place(x=400, y=250)

w = Label(text='...', font=('arial', 20, 'bold'), bg='#13a1d6')
w.place(x=120, y=430)
h = Label(text='...', font=('arial', 20, 'bold'), bg='#13a1d6')
h.place(x=280, y=430)
d = Label(text='...', font=('arial', 20, 'bold'), bg='#13a1d6')
d.place(x=430, y=430)
p = Label(text='...', font=('arial', 20, 'bold'), bg='#13a1d6')
p.place(x=670, y=430)


root.mainloop()
