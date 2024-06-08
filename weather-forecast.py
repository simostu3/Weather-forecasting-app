from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d474ebc8319569ba80ed9dd28f35a56d").json()

    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("The Weather Today")
win.config(bg="light blue")
win.geometry("500x510")

name_label = Label(win, text="The Weather Today", font=("Time New Roman", 35, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh",
             "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir",
             "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
             "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
             "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
             "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
             "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
             "National Capital Territory of Delhi", "Puducherry"]
com = ttk.Combobox(win, values=list_name,
                   font=("Time New Roman", 20), textvariable=city_name)
com.place(x=50, y=120, height=50, width=400)

done_button = Button(win, text="Done", font=("Time New Roman", 20, "bold"),  command=data_get)
done_button.place(x=200, y=190, height=50, width=100)

w_label = Label(win, text="Weather Climate :",
                font=("Time New Roman", 15), bg="light blue", fg="black")
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(win, text="", font=("Time New Roman", 15), bg="light blue", fg="black")
w_label1.place(x=250, y=260, height=50, width=210)


wb_label = Label(win, text="Weather Description :",
                 font=("Time New Roman", 15), bg="light blue", fg="black")
wb_label.place(x=25, y=310, height=50, width=210)
wb_label1 = Label(win, text="",
                  font=("Time New Roman", 15), bg="light blue", fg="black")
wb_label1.place(x=250, y=310, height=50, width=210)


temp_label = Label(win, text="Temperature :",
                   font=("Time New Roman", 15), bg="light blue", fg="black")
temp_label.place(x=25, y=360, height=50, width=210)
temp_label1 = Label(win, text="",
                    font=("Time New Roman", 15), bg="light blue", fg="black")
temp_label1.place(x=250, y=360, height=50, width=210)


per_label = Label(win, text="Pressure :",
                  font=("Time New Roman", 15), bg="light blue", fg="black")
per_label.place(x=25, y=410, height=50, width=210)
per_label1 = Label(win, text="",
                   font=("Time New Roman", 15), bg="light blue", fg="black")
per_label1.place(x=250, y=410, height=50, width=210)


win.mainloop()
