import requests
from datetime import datetime

api_key = 'e67e6054f0f940d42728df1ab59cfda1'
city = input("Enter the city name: ")

api_web_link = "https://api.openweathermap.org/data/2.5/weather?q={} &appid={}".format(city,api_key)
api_link = requests.get(api_web_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdty = api_data['main']['humidity']
wind = api_data['wind']['speed']
clouds = api_data['clouds']['all']
date_time = datetime.now().strftime("%d %b %Y | %I:%M %p")
deg_sign=u"\N{DEGREE SIGN}"

print ("-------------------------------------")
print ("Weather Stats for - {}  \n  {}".format(city.upper(), date_time))
print ("-------------------------------------")

print ("Temperature           : {:.0f}{}C".format(temp_city, deg_sign))
print ("Weather Description   :",weather_desc)
print ("Humidity              :",hmdty, '%')
print ("Wind Speed            :",wind ,'km/h')
print ("Cloud Coverage        :",clouds, '%')

print("======================================")
