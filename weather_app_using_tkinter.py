import tkinter
from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk
import requests
import json
from datetime import datetime

def func_get_weather():
    city = select_city_dropdown.get()

    if not city or city == "Select City":
        output_label.config(text="Please select a city.")
        output_frame.pack(pady=10)
        return
    
    api_key = "bfee43b016e8e47a8d4669b0de409b29"
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    server_data = requests.get(api_url)
    server_data_json = server_data.json()
    # print(server_data_json)

    # hum_server_data_json = json.dumps(server_data_json,indent=4)
    # print(hum_server_data_json)

    try:
        temp = server_data_json["main"]["temp"]
        feels = server_data_json["main"]["feels_like"]
        temp_min = server_data_json["main"]["temp_min"]
        temp_max = server_data_json["main"]["temp_max"]
        pressure = server_data_json["main"]["pressure"]
        humidity = server_data_json["main"]["humidity"]
        sea_level = server_data_json["main"].get("sea_level", "N/A")
        ground_level = server_data_json["main"].get("grnd_level", "N/A")
        description = server_data_json["weather"][0]["description"]

        output_label.config(text=f"Temperature: {temp}°C\n"
                            f"Feels like: {feels}°C\n"
                            f"Temperature Minimum: {temp_min}°C\n"
                            f"Temperature Maximum: {temp_max}°C\n"
                            f"Pressure: {pressure}\n"
                            f"Humidity: {humidity}%\n"
                            f"Sea Level: {sea_level}\n"
                            f"Ground Level: {ground_level}\n"
                            f"Condition: {description.capitalize()}" 
                            )
    except KeyError:
        output_label.config(text=f"Weather data for \'{city}\' is unavailable. \nPlease check the city name.")

    output_frame.pack(pady=10)
    

root = Tk()


def key_input(event):
    key = event.char

    if key == "\r":
        func_get_weather()

root.bind("<Key>",key_input)


def update_time():
    now = datetime.now()
    current_time = now.strftime("%A %d %B %Y, %I:%M %p")
    time_label.config(text=current_time)
    root.after(60000,update_time)
    

root.title("My Weather App")
root.geometry("500x600")

image_path = r"D:\Python Projects\pr-05\used_images\weather_image.png"
bg_image = PhotoImage(file=image_path)

set_bg_image = Label(root, image = bg_image)
set_bg_image.place(relheight=1, relwidth=1)

# app_header = Label(root, text="My Weather App", font= ("Georgia", 24), bg = "White", fg = "Blue", bd=2, relief = "solid", highlightbackground="blue",highlightthickness=5)
app_header = Label(root, text="My Weather App", font= ("Georgia", 24), bg = "White", fg = "Blue", bd=2, relief = "solid")
app_header.pack(pady=20)

time_label = Label(root, font=("Georgia", 15))
time_label.pack(pady=10)
update_time()

select_city_label = Label(root, text="Select a City", font=("Georgia", 15), fg = "Black", bg="White")
select_city_label.pack(pady=20)

cities = ["Mumbai","Pune","Hyderabad","Lucknow","Bangalore"]
select_city_dropdown = ttk.Combobox(root, values=cities, font=("Georgia", 10))
select_city_dropdown.pack(pady=20)
select_city_dropdown.set("Select City")

get_weather_button = Button(root, text="Get Weather", font=("Georgia",15), bg="white", fg="black", command= func_get_weather)
get_weather_button.pack(pady=10)

output_frame = Frame(root, highlightbackground="Light Green", highlightthickness=5)

output_label = Label(output_frame, text="", font=("Georgia", 15))
output_label.pack(pady=10)

root.mainloop()