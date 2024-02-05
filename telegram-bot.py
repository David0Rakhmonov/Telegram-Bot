import telebot
import requests
from datetime import datetime, timedelta
import random
import time
import asyncio
import time

BOT_TOKEN = "6733216741:AAFtBXwE8FAc3JnBlQOfZa9pWanZzpSYP6c"


GROUP_ID = -1001088428205


API_KEY = "93983d8ab5de35b2860c13aa86e26fa4"


CITY = "Moscow"


recommendations = {
    "1": "Сегодня вас ждет удача!",
    "2": "Будьте осторожны и внимательны.",
    "3": "Наслаждайтесь моментом!",
    "4": "Не бойтесь пробовать новое.",
    "5": "Сегодня ваш день!",
}

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Я бот, который отправляет погоду в чат и пишет рекомендацию на день) Тебе надо всего то добавить меня в чат и жди к 7 утра!')
bot.polling(none_stop=True)

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    data = response.json()
    return data

def get_message(weather_data, recommendation):
    message = f"**Доброе утро!**\n\n"
    message += f"**Сегодня:** {weather_data['main']['temp']}°C, {weather_data['weather'][0]['description']}\n\n"
    message += f"**Рекомендация на день:** {recommendation}"
    return message

def send_message(bot, chat_id, text):
    bot.send_message(chat_id=chat_id, text=text)

bot = telebot.TeleBot(BOT_TOKEN)

bot.polling(none_stop=True)

def send_weather_report():
    weather_data = get_weather(CITY)

    recommendation_id = str(random.randint(1, len(recommendations)))
    recommendation = recommendations[recommendation_id]

    message = get_message(weather_data, recommendation)

    send_message(bot, GROUP_ID, message)
    #time.sleep('оставшееся время до полуночи в минутах' * 60 + 60 * 60 * 7)
   # send_weather_report()
   # for _ in range(1000000):
    #    time.sleep(86400)
     #   send_weather_report()