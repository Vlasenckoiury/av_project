## -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext as _


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Car(models.Model):
    category = models.ForeignKey(Category, related_name='av_car', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    price = models.CharField(max_length=50)
    price_usd = models.CharField(max_length=50)
    image = models.TextField(max_length=1000)
    parameter = models.TextField(max_length=500)
    description = models.TextField(max_length=500)
    modification = models.TextField(max_length=500)
    all_modification = models.TextField(max_length=500)
    location = models.TextField(max_length=500)
    comment = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'name'),)

    def __str__(self):
        return self.name


class BotUser(models.Model):
    telegram_id = models.PositiveBigIntegerField(_('ID Telegram'), db_index=True, unique=True)
    username = models.CharField(_('Username'), max_length=100, blank=True, null=True)
    first_name = models.CharField(_('Имя'), max_length=100, blank=True, null=True)
    last_name = models.CharField(_('Фамилия'), max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь бота'
        verbose_name_plural = 'Пользователи бота'

    def __str__(self):
        return f'{self.telegram_id}: {self.username}'


class TelegramChat(models.Model):
    bot_user = models.ForeignKey(BotUser, verbose_name=_('Пользователь бота'), on_delete=models.CASCADE)
    name = models.CharField(_('Имя канала'), max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Телеграм канал'
        verbose_name_plural = 'Телеграм каналы'


class InviteLink(models.Model):
    # Пригласительные ссылки
    telegram_chat = models.ForeignKey(TelegramChat, verbose_name=_('Телеграм канал'), on_delete=models.CASCADE)
    creates_join_request = models.BooleanField(_('Запрос на добавление'), default=True)
    creator = models.CharField(_('Создатель'), max_length=250, blank=True, null=True)
    expire_date = models.CharField(_('expire_date'), max_length=150, blank=True, null=True)
    link = models.CharField(_('Ссылка'), max_length=150, blank=True, null=True)
    is_primary = models.BooleanField(_('Is_primary'), blank=True, null=True)
    is_revoked = models.BooleanField(_('Is_revoked'), blank=True, null=True)
    member_limit = models.IntegerField(_('Лимит подписок'), blank=True, null=True)
    name = models.CharField(_('name'), max_length=150, blank=True, null=True)
    pending_join_request_count = models.IntegerField(_('pending_join_request_count'), blank=True, null=True)

    def __str__(self):
        return f'{self.link}'

    class Meta:
        verbose_name = 'Пригласительная ссылка'
        verbose_name_plural = 'Пригласительные ссылки'


class TelegramSubscriber(models.Model):
    invite_link = models.ForeignKey(TelegramChat, verbose_name=_('Пригласительная ссылка'), on_delete=models.CASCADE)
    telegram_id = models.PositiveBigIntegerField(_('ID Telegram'), db_index=True, unique=True)
    username = models.CharField(_('Username'), max_length=100, blank=True, null=True)
    first_name = models.CharField(_('Имя'), max_length=100, blank=True, null=True)
    last_name = models.CharField(_('Фамилия'), max_length=100, blank=True, null=True)
    subcribed = models.BooleanField(_('Подписан'), default=False)
    datetime_subscribe = models.DateTimeField(_('Время подписки'), blank=True, null=True)
    datetime_unsubscribe = models.DateTimeField(_('Время отписки'), blank=True, null=True)

    def __str__(self):
        return f'{self.telegram_id}: {self.username}'

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
