from django.conf import settings
from telebot.async_telebot import AsyncTeleBot
import aiohttp


# '6613313841:AAEyd57MKTPC-pL13saMn5sDl2pxFzTf3Hk'
bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='html')


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.send_message(message.chat.id, """Добро пожаловать в Av Car""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)
