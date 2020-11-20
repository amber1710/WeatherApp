from tkinter import *
from tkinter import messagebox
import requests

mywindow=Tk()
mywindow.title("Amber Weather App")
mywindow.geometry("500x500")
mywindow.config(background="light blue")

def get_weather():
 mycity=city_entry.get()
 weatherkey = '7f65701f025236c354d7754c5a4e0b71'
 url = 'https://api.openweathermap.org/data/2.5/weather'
 params1 = {'appid': weatherkey, 'q': mycity, 'units': 'Metric'}
 response = requests.get(url, params=params1)
 weather = response.json()
 result = weather['main']['temp']
 result2 = weather['main']['humidity']
 result3 = weather['wind']['speed']
 mylabel.config(text=str(result))
 mylabel_2.config(text=str(result2))
 mylabel_3.config(text=str(result3))


 print(weather)
def clear():
  pass

#  Label for entry
city_label=Label(mywindow, text="Enter the name of the city")
city_label.place(x=5, y=10)

#Entry for city name
city_entry=Entry(mywindow)
city_entry.place(x=250, y=10)

#Label temperature
label1=Label(mywindow, text="Temperature:")
label1.place(x=5, y=50)
mylabel = Label(mywindow)
mylabel.place(x=250, y=50)

#Label for humidity
label2=Label(mywindow,text="Humidity:")
label2.place(x=5,y=90)
mylabel_2=Label(mywindow)
mylabel_2.place(x=250,y=90)

#Label for wind speed
label3=Label(mywindow,text="Wind Speed:")
label3.place(x=5,y=130)
mylabel_3=Label(mywindow)
mylabel_3.place(x=250,y=130)

#Button to check weather
mybutton=Button(mywindow, text="Check weather", command=get_weather)
mybutton.place(x=10, y=160 )

#Button to clear data
mybutton=Button(mywindow, text="Clear", command=clear)
mybutton.place(x=180, y=160 )

#Button to exit window
mybutton=Button(mywindow, text="Exit", command=mywindow.destroy)
mybutton.place(x=280, y=160)


mywindow.mainloop()
