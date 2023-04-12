# coding=utf-8
import requests
import datetime
from pprint import pprint
from config import open_weather_token
from PIL import Image, ImageDraw, ImageFont

code_to_smile = {
    "Clear": "Ясно",
    "Clouds": "Облачно",
    "Rain": "Дождь",
    "Drizzle": "Дождь",
    "Thunderstorm": "Гроза",
    "Snow": "Снег",
    "Mist": "Туман"
}

r = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={'tashkent'}&appid={open_weather_token}&units=metric&lang={'ru'}"
)
data = r.json()

city = data["name"]
cur_weather = data["main"]["temp"]

weather_description = data["weather"][0]["main"]
if weather_description in code_to_smile:
    wd = code_to_smile[weather_description]
else:
    wd = "Посмотри в окно, не пойму что там за погода!"

humidity = data["main"]["humidity"]
pressure = str(data["main"]["pressure"]) + ' мм рт.ст.'
wind = str(data["wind"]["speed"]) + ' м/c'
sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
    data["sys"]["sunrise"])
date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

print(f"*** {date} ***\n"
      f"Погода в городе {city}\nТемпература: {cur_weather}°C {wd}\n"
      f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\nВетер: {wind} м/с\n"
      f"Восход солнца: {sunrise_timestamp}\nЗакат солнца {sunset_timestamp}\n"
      f"Продолжительность дня: {length_of_the_day}\n"
      f"Хорошего дня"
      )

img = Image.open('images/main.png')
text = str(int(cur_weather)) + '°'
draw = ImageDraw.Draw(img)

font_main = ImageFont.truetype('fonts/Overpass-Medium.ttf', size=150)
font_secondary = ImageFont.truetype('fonts/Overpass-Bold.ttf', size=38)
font_third = ImageFont.truetype('fonts/Overpass-Regular.ttf', size=30)

W, H = (1080, 1080)
w, h = draw.textsize(text, font=font_main)
w1, h1 = draw.textsize(code_to_smile[weather_description], font=font_secondary)
w2, h2 = draw.textsize(date, font=font_third)

draw.text(((W - w) / 2, (H - h) / 2 + 30), text, font=font_main)
draw.text(((W - w1) / 2, (H - h1) / 2 + 150), code_to_smile[weather_description], font=font_secondary)
draw.text(((W - w2) / 2, (H - h2) / 2 - 70), date, font=font_third)

draw.text(((W - w2) / 2 + 200, (H - h2) / 2 + 215), wind, font=font_third)
draw.text(((W - w2) / 2 + 200, (H - h2) / 2 + 275), pressure, font=font_third)

img.save('images/main1.png')
