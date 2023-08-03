import tkinter as tk
import customtkinter as ctk
import bs4
import requests
import re

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Stupid Weather Application")

label = ctk.CTkLabel(root, text="Enter Your City Name!",
                     font=("Arial", 22, "bold"))
label.grid(padx=20, pady=20, row=1, columnspan=2)

entry_box = ctk.CTkEntry(root, height=3, font=("Arial", 16))
entry_box.grid(row=2, column=0, padx=(30, 5))

text = ctk.CTkLabel(root, text="--°C", font=("Arial", 20))
text.grid(row=3, column=0, columnspan=2, pady=20)


def get_input():
    # progressbar = ctk.CTkProgressBar(master=root, indeterminate_speed=3)
    # progressbar.grid(row=4)
    weather_info = re.compile(r"(\d+)°C")
    input_entry = entry_box.get()
    try:
        print(root['bg'][-2:])

        query = "https://www.google.com/search?q=location+weather".replace(
            'location', input_entry)

        print(query)

        req_obj = requests.get(query)

        soup = bs4.BeautifulSoup(req_obj.content, 'html.parser')
        # fp = open('./res.google.weather.html', mode="w+", encoding="utf-8")
        # fp.write(str(soup))
        # fp.close()
        temp = re.search(weather_info, str(soup))[0]
        print(temp)
        if root['bg'].startswith('gray') and int(root['bg'][-2:]) < 50:
            text.configure(text=temp, text_color="white",
                           font=("Arial", 20, 'bold'))
        else:
            text.configure(text=temp, text_color="black",
                           font=("Arial", 20, 'bold'))
    except Exception as e:
        print("Exception occured", e)
        # if()
        text.configure(text="Please enter valid city name",
                       text_color="red", font=("Arial", 14))
    # finally:
        # progressbar.destroy()


btn = ctk.CTkButton(root, font=("Arial", 14, "bold"),
                    text="Go →", command=get_input)
btn.grid(row=2, column=1, padx=(5, 30))

# Starting the main application --

root.mainloop()
