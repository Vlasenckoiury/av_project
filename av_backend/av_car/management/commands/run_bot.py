import asyncio

from django.core.management.base import BaseCommand

from av_project.av_backend.av_car.main_bot import bot


class Command(BaseCommand):
    help = "Запуск бота"

    def handle(self, *args, **options):
        asyncio.run(bot.polling())
