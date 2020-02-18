import pyowm

owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key



# Search for current weather in London (Great Britain)

location = input("Please enter your city:")
observation = owm.weather_at_place(location)
w = observation.get_weather()
temperature = round(w.get_temperature('celsius')['temp'], 0)

#print(w)                      # <Weather - reference time=2013-12-18 09:20, # status=Clouds>

# Weather details
##w.get_wind()                  # {'speed': 4.6, 'deg': 330}
#w.get_humidity()              # 87
#temp = str(w[0])
print("Temperature in " + location + " is :",temperature)