import telebot
import requests
import json

bot = telebot.TeleBot("6461469889:AAFrtWDxbJkw1SfqhRJLqnb0qtO1ELyO3WY")
API = "8ed60efc2ab417a63a2385ddc5bee6e2"


@bot.message_handler(commands=["start"])
def start(mess):
    bot.send_message(mess.chat.id, "Hello! Please, type name of the city")


@bot.message_handler(content_types=['text'])
def main(mess):
    city = mess.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code == 200:
        info = json.loads(res.text)
        bot.reply_to(mess, f"Temperature: {info['main']['temp']} °C, feels like: {info['main']['feels_like']} °C;\n"
                           f"Description: {info['weather'][0]['description']};\n"
                           f"Humidity: {info['main']['humidity']}%;\n"
                           f"Atmospheric pressure: {info['main']['pressure']} hPa;\n"
                           f"Wind speed: {info['wind']['speed']} m/s.")
    else:
        bot.reply_to(mess, "There are no such city or country!")


bot.infinity_polling()
