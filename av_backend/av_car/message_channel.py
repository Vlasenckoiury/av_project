import logging

import pytz
import schedule
import time
import telebot
from django.conf import settings
# from telebot import types
# from telegram import Bot

from av_project.av_backend.av_car.db_tg import *
from datetime import datetime
from datetime import time


bot_channel = telebot.TeleBot(settings.TOKEN_BOT, parse_mode='HTML')
telebot.logger.setLevel(settings.LOG_LEVEL)

logger = logging.getLogger(__name__)


def send_message():
    channel = get_channel()
    if channel:
        for result in channel:
            bot_channel.send_message(chat_id=result[0], text=result[1])
    else:
        logger.info(f'Сообщение не отправлено в канал')


def scheduled_message():
    new_records = get_time()
    if new_records:
        now = datetime.now(pytz.timezone('Europe/Moscow'))
        current_time = now.time()
        start_time = new_records[0][0]
        end_time = time(hour=7, minute=00, second=0)
        if (start_time <= current_time <= end_time
            or start_time >= current_time <= end_time
                or start_time <= current_time >= end_time):
            logger.info("Текущее время заданно в диапазоне заданному времени")
            send_message()
        else:
            logger.info("Текущее время заданно вне диапазоне заданному времени")
    # if start >= curr <= end_time or start <= curr >= end_time:
        #     logger.info("Текущее время заданно в диапазоне заданному времени")
        # if current_time <= start_time and current_time <= end_time or current_time <= start_time and current_time <= end_time:
        #     logger.info("Текущее время заданно в диапазоне заданному времени")
        #     send_message()
        # else:
        #     logger.info("Текущее время вне заданного времени")


schedule.every().seconds.do(scheduled_message)

while True:
    schedule.run_pending()
    # time.sleep(1)
