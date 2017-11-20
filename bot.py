# -*- coding: utf-8 -*-
#import redis
import os
import telebot
#import botWiki
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
#some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
#r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)


# Substituir TOKEN abaixo:
bot = telebot.TeleBot(token)

# Responde a comandos: (/comando)
@bot.message_handler(commands=['acorde', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Bom dia!")

#@bot.message_handler(content_types=['wikipedia'])
#def wiki(message):
#	bot.reply_to(message, "Sobre o que você quer saber?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()