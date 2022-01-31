import requests
import tkinter as tk
from tkinter import ttk, messagebox
import time
from tkinter.font import Font


def get_all_weather_data(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = "7275af378cb206667b9ae030ec07a4c2"
    url = f'{base_url}q={city}&appid={api_key}'
    resp = requests.get(url)
    return resp.json()


# Functions to fetch data and display to the GUI


def fetch_data():
    city = user_input.get()
    json = get_all_weather_data(city)
    print(json)

    if json['cod'] == 200:
        clock_time = time.strftime('%I:%M %p', time.gmtime(json['timezone']))
        time_zone.set(f'{clock_time}')

        current_temp.set(f"{round((json['main']['temp']) - 273.15)}°C")

        feels_temp.set(f"{round((json['main']['feels_like']) - 273.15)}°C")

        summary_report.set(json['weather'][0]['description'])

        wind_speed.set(f"{round(json['wind']['speed'] * 18/5)} km/h")

        img["file"] = f"icons/{json['weather'][0]['icon']}.png"  # Function to get weather images

        if 'gust' in json['wind']:
            wind_gusts.set(f"{round(json['wind']['gust'] * 18/5)} km/h")
        else:
            wind_gusts.set('NO DATA')

    elif json['cod'] == 404:
        messagebox.showerror(f"'Error', 'CITY NOT FOUND'{city}")


# Object for Font, Font size, Color
# app_font = Font(family="roboto", size=14, weight="bold")

# 1. Make a root window
root = tk.Tk()
root.title('Weather App')
root.iconbitmap(r'weather_root_icon.ico')
root.geometry('630x400')

# 2. Make the main frame
root_frame = tk.Frame(root, background='#817bbd')
root_frame.pack(fill=tk.BOTH, expand=True)

# 3. Will display weather images
img = tk.PhotoImage(file="")
image = tk.Label(root_frame, image=img, bg='#817bbd')
image.grid(column=5, row=5, ipadx=100, padx=10)

# 4. Make label and Entry box for user input
tk.Label(root_frame, text='Enter City:', font='bold', background='#817bbd').grid(column=0, row=1, pady=(10, 10))

user_input = tk.StringVar()
tk.Entry(root_frame, textvariable=user_input, justify='center', bg='#817bbd').grid(column=1, row=1, pady=(10, 10))

# 5. Make the get weather Button
tk.Button(root_frame, text='Search Weather', command=fetch_data, justify='center', bg='#817bbd').grid(column=0, row=3,
                                                                                                      columnspan=3,
                                                                                                      ipadx=100,
                                                                                                      padx=10)

###
# 6. Make label and Entry box to show current temp
tk.Label(root_frame, text='Current Temp:', font='bold', background='#817bbd').grid(column=0, row=4, pady=(10, 10))
current_temp = tk.StringVar()
tk.Entry(root_frame, textvariable=current_temp, justify='center', bg='#817bbd').grid(column=1, row=4, pady=(10, 10))

###
# 7. Make label and Entry box to show feels like temp
tk.Label(root_frame, text='Feels Like Temp: ', font='bold', background='#817bbd').grid(column=0, row=5, pady=(10, 10))
feels_temp = tk.StringVar()
tk.Entry(root_frame, textvariable=feels_temp, justify='center', bg='#817bbd').grid(column=1, row=5, pady=(10, 10))

###
# 8. Make label and Entry box to show summary
tk.Label(root_frame, text='Summary:', font='bold', background='#817bbd').grid(column=0, row=6, pady=(10, 10))
summary_report = tk.StringVar()
tk.Entry(root_frame, textvariable=summary_report, justify='center', bg='#817bbd').grid(column=1, row=6, pady=(10, 10))

###
# 9. Make label and Entry box to show Wind Speed
tk.Label(root_frame, text='Wind Speed:', font='bold', background='#817bbd').grid(column=0, row=7, pady=(10, 10))
wind_speed = tk.StringVar()
tk.Entry(root_frame, textvariable=wind_speed, justify='center', bg='#817bbd').grid(column=1, row=7, pady=(10, 10))

###
# 10. Make label and Entry box to show wind gusts
tk.Label(root_frame, text='Wind Gusts', font='bold', background='#817bbd').grid(column=0, row=8, pady=(10, 10))
wind_gusts = tk.StringVar()
tk.Entry(root_frame, textvariable=wind_gusts, justify='center', bg='#817bbd').grid(column=1, row=8, pady=(10, 10))

###
# 11. Time Zone
# ttk.Label(root_frame, text='Time Zone', font='bold', background='#666293').grid(column=0, row=10, pady=(10, 10))
time_zone = tk.StringVar()
tk.Entry(root_frame, textvariable=time_zone, bd=0, justify='center', bg='#817bbd').grid(column=5, row=7, pady=(10, 10))

###
# 12. Exit Button
tk.Button(root_frame, text="Exit", justify='center', bg='#817bbd', command=root.quit).grid(column=0, row=11,
                                                                                           columnspan=5, ipadx=100,
                                                                                           padx=10)

root.mainloop()
