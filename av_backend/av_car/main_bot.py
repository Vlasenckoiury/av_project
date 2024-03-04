import logging
import telebot
from django.conf import settings
from telebot.async_telebot import AsyncTeleBot
import aiohttp


bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')
telebot.logger.setLevel(settings.LOG_LEVEL)

logger = logging.getLogger(__name__)


@bot.chat_member_handler()
async def chat_member_handler_bot(message):
    status = message.difference.get('status')
    invite_link = message.invite_link
    full_name = message.from_user.full_name
    username = message.from_user.username
    id = message.from_user.id
    invite_link_name = ''
    invite_link_url = ''
    try:
        invite_link_name = getattr(invite_link, 'name')
        invite_link_url = getattr(invite_link, 'invite_link')
    except AttributeError as err:
        logger.info(f'Не получил пригласительную ссылку: {err}')
    current_subscriber_status = status[1]
    if current_subscriber_status == 'creator':
        status_text = '🚀 Подписались'
    else:
        status_text = '😔 Отписались'
    text_message = (f'Статус: {status_text}\n'
                    f'Имя: {full_name}\n'
                    f'ID: {id}')
    if username:
        text_message += f'\n<b>Никнейм:</b> @{username}'
    if invite_link_name:
        text_message += f'\nИмя ссылки: {invite_link_name}'
    if invite_link_url:
        text_message += f'\n<b>URL</b>: {invite_link_url}'
    await bot.send_message(chat_id=settings.TELEGRAM_ID_ADMIN, text=text_message)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.send_message(message.chat.id, """Добро пожаловать в Av Car 🚗""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, 'Упс ошибка 😔')
