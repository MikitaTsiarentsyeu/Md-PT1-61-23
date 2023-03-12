import telebot
from bs4 import BeautifulSoup
from urllib.request import urlopen

bot = telebot.TeleBot("6157354287:AAEOCLM4bfO6qaFFBVC2hPeqZqRh5k-3LPs")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "hello there!")

@bot.message_handler(commands=['kurs'])
def kurs_message(message):
    html = urlopen('https://kurs.onliner.by/')
    soup = BeautifulSoup(html)
    tag_list = soup.find_all('p', {'class':'value'})
    buy = tag_list[0].text
    sell = tag_list[1].text
    bot.send_message(message.chat.id, f"buy - {buy}, sell - {sell}")

bot.polling()