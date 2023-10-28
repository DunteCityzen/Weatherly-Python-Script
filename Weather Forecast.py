import requests
from datetime import datetime

api_key = "e770e6e35eb48d53ddd46f147c11743c"
city = input("Enter your city's name: ")
full_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
api_link = requests.get(full_api_link)
api_data = api_link.json()

#Now creating variables to store the data and help in displaying them

temperature = ((api_data['main']['temp']) - 273.5)
weather = api_data['weather'][0]['description']
humidity = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now()

#Now Printing Information on the screen

print('-' * 50)
print("\nWeather Stats for {} || {}\n".format(city.upper(), date_time))
print("-" * 50)
print("The weather Today is: {}\n".format(weather))
print("Current temperature is: {} degrees C\n".format(temperature))
print("Current humidity is: {}%\n".format(humidity))
print("Current wind speed is: {} Kmh\n".format(wind_speed))
print("=" * 50)

#Printing details into a text file

details_list = [weather,temperature,humidity,wind_speed,date_time]
with open('weather_forecast.txt', mode='w', encoding= 'utf-8') as wf :
  wf.write("\nWeather Stats for {} || {}\n".format(city.upper(), date_time))
  wf.write("-" *50)
  wf.write("The weather Today is: {}\n".format(details_list[0]))
  wf.write("Current temperature is: {} degrees C\n".format(details_list[1]))
  wf.write("Current humidity is: {}%\n".format(details_list[2]))
  wf.write("Current wind speed is: {} Kmh\n".format(details_list[3]))
  wf.write("=" *50)
