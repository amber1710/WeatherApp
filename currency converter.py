from tkinter import *
import tkinter as tk
import requests,json
mywindow = Tk()
mywindow.title("Exchange Rate ")
mywindow.configure(background = 'beige')
mywindow.geometry("400x400")

headlabel=Label(mywindow,text="Currency Converter")
headlabel.place(x=100,y=1)

variable1 = StringVar(mywindow)
variable2 = StringVar(mywindow)

variable1.set("currency")
variable2.set("currency")

def get_currency():
  mycurrency=cur_entry.get()
  cur_key='6c4dc57c77cb4108b4df8583'
  url='https://v6.exchangerate-api.com/v6/6c4dc57c77cb4108b4df8583/latest/USD'
  response=requests.get(url)
  currency=response.json()
  x=result['conversion_rates']['USD']
  y=result['conversion_rates']['BGN']
  print(x,y)


#Label for Amount
label1 = Label(mywindow, text = "Amount :", fg = 'black', bg = 'pink')
label1.place(x=5,y=70)


#Label 2 for currency
label2 = Label(mywindow, text = "From Currency:", fg = 'black', bg = 'pink')
label2.place(x=5,y=100)

#Label3 for currency
label3 = Label(mywindow, text = "To Currency :",fg = 'black', bg = 'pink')
label3.place(x=5,y=130)

#Label to display converted amount
label4 = Label(mywindow, text = "Converted Amount :",fg = 'black', bg = 'pink')
label4.place(x=5,y=160)

#Entry for amount
Amount_field=Entry(mywindow)
Amount_field1_
mywindow.mainloop()
