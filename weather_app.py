from tkinter import *
import requests
import json
from API_KEY import key
from tkinter import messagebox

# creating the main gui window of the project
root = Tk()
root.title('Weather')

def check_weather():
    # getting the zip code from the user
    zip_code = entry.get()

    # getting the data using api according to the zip code
    api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='+zip_code+'&distance=5&API_KEY='+key)
    api = json.loads(api_request.content)
    
    # changing the color of the label according the weather category
    if len(api) == 0:
        messagebox.showinfo('message', 'Region Unavilable')
    else:
        if api[0]['Category']['Name'] == 'Good':
            color = '#00E400'
        elif api[0]['Category']['Name'] == 'Moderate':
            color = '#ffff00'
        elif api[0]['Category']['Name'] == 'Unhealthy for Sensitive Groups':
            color = '#ff7e00'
        elif api[0]['Category']['Name'] == 'Unhealthy':
            color = '#ff0000'
        elif api[0]['Category']['Name'] == 'Very Unhealthy':
            color = '#99004c'
        else:
            color = '#7e0023'

        text = f"{api[0]['ReportingArea']}, {api[0]['StateCode']}\nAir Quality Index: {api[0]['AQI']}"
        Label(root, text=text, font='Arial 15', width=25, bg=color).grid(row=3, column=0, columnspan=2, pady=10)

# design of the app
Label(root, text='Weather Conditions\nIn Your Region', font='Arial 20').grid(row=0, column=0, columnspan=2, padx=75, pady=10)
Label(root, font='Arial 15', text='Zip Code:').grid(row=1, column=0, sticky='e', pady=10)
entry = Entry(root, font='Arial 15', width=11)
entry.grid(row=1, column=1, sticky='w', pady=10)
Button(root, text='Check Weather', font='Arial 12', command=check_weather).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()