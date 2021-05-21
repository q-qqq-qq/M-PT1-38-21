import telebot
from urllib.request import urlopen
from bs4 import BeautifulSoup

bot = telebot.TeleBot("1796998154:AAFoGbpB1tJThiKcNvzKr7vtBKPq6xIDSyo")
x = 5
x = []
x = "test"

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello there!")

@bot.message_handler(commands=['update'])
def update_message(message):
    content = urlopen("https://kurs.onliner.by/")
    soup = BeautifulSoup(content)

    data = soup.findAll('p', {'class': 'value fall'})
    x = data[0].contents[0].contents[0]

    bot.send_message(message.chat.id, x)

bot.polling()
print("test")

