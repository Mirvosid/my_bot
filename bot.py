from wikipedia import*
import telebot

API_TOKEN = '6403247429:AAEBzVD7KvMvyWs0dj7Zgmu-nSTQMDUUuy0'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\ Salom men content manager botman ya'ni ma'lum bir mavzu bo'yicha ma'lumot beraman!\
""")

@bot.message_handler(content_types=["text"])
def send_wiki(message: str):
    bot.reply_to(message)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
