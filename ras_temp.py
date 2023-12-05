import requests


def convert_kelvin_to_celsius(temp):
    return temp - 273.15

def get_max_day(jsonfor):
    min_day= -100000
    for i in range(0, 12):
        if jsonfor["list"][i]["main"]["temp_min"] > min_day:
            min_day = jsonfor["list"][i]["main"]["temp_min"]
    return int(convert_kelvin_to_celsius(min_day))

def get_min_day(jsonfor):
    max_day= 100000
    for i in range(0, 12):
        if jsonfor["list"][i]["main"]["temp_max"] < max_day:
            max_day = jsonfor["list"][i]["main"]["temp_max"]
    return int(convert_kelvin_to_celsius(max_day))

lat = 45.764671
lon = 4.880400
language = "en"
key = "bdeb8474ac275502254ef9113a922598"
apilinkcurrent = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
apilinkforecast = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}"

jsonfor = requests.get(apilinkforecast).json()
jsoncur = requests.get(apilinkcurrent).json()


global_weather_cur = jsoncur["weather"][0]["main"]
temp_cur = int(convert_kelvin_to_celsius(jsoncur["main"]["temp_max"]))

print("Le minimum du jour : " + str(get_min_day(jsonfor)) + "*C")
print("Le maximum du jour : " + str(get_max_day(jsonfor)) + "*C")
print("Le temps actuel : " + str(global_weather_cur))
print("La temperature actuelle : " + str(temp_cur) + "*C")

