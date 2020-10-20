# -*- coding: utf-8 -*-
# author: asyncvk
import six
import aiohttp
import requests
import time
import asyncio

"""
:authors: sergeyfilippov1, YamkaFox
:license: Mozilla Public License, version 2.0, see LICENSE file
:copyright: (c) 2020 asyncvk
"""


class API:
    def __init__(self, token, loop, api_version="5.124"):
        self.token = token
        self.api_version = api_version
        self.base_url = "https://api.vk.com/method/"
        self.session = aiohttp.ClientSession()

    async def call(self, method_name, data):
        data["access_token"] = self.token
        data["v"] = self.api_version
        url = self.base_url + method_name
        self.last_request_time = time.time()
        response = await self.session.post(url, data=data)
        response = await response.json()
        return response       

    def sync_call(self, method_name, data):
        data["access_token"] = self.token
        data["v"] = self.api_version
        url = self.base_url + method_name
        response = requests.post(url, data=data).json()
        return response["response"]

    def getEventType(self, id):
        if id == 1:
            return 'REPLACE_MESSAGE_FLAGS' # Замена флагов сообщения
        if id == 2:
            return 'SET_MESSAGE_FLAGS' # Установка флагов сообщения
        if id == 3:
            return 'RESET_MESSAGE_FLAGS' # Сброс флагов сообщения
        if id == 4:
            return 'ADD_NEW_MESSAGE' #  Добавление нового сообщения
        if id == 5:
            return 'EDIT_MESSAGE' # Редактирование сообщения
        if id == 6:
            return 'INCOMING_MESSAGE_READ' # Прочтение входящего вообщения
        if id == 7:
            return 'OUTCOMING_MESSAGE_READ' # Прочтение исходящего сообщения
        if id == 8:
            return 'FRIEND_ONLINE' # Друг стал онлайн
        if id == 9:
            return 'FRIEND_OFFLINE' # Друг стал оффлайн
        if id == 10:
            return 'RESET_DIALOG_FLAGS' # Сброс флагов диалога
        if id == 11:
            return 'REPLACE_DIALOG_FLAGS' # Замена флагов диалога
        if id == 12:
            return 'SET_DIALOG_FLAGS' # Установка флагов диалога
        if id == 13:
            return 'DELETE_MESSAGE' # Удаление сообщения
        if id == 14:
            return 'UNDO_DELETE_MESSAGE' # Отмена удаления сообщения
        if id == 20:
            return 'MAJOR_ID_CHANGED' # Изменился major id
        if id == 21:
            return 'MINOR_ID_CHANGED' # Изменился minor id
        if id == 51:
            return 'CONTENT_OR_TOPIC_CHANGED' # Состав или тема изменены
        if id == 52:
            return 'CHANGE_CHAT_INFO' # Изменена информация чата
        if id == 61:
            return 'USER_TYPING_IN_DIALOG' # Пользователь печатает в диалоге
        if id == 62:
            return 'USER_TYPING_IN_CONVERSATION' # Пользователь печатает в беседа
        if id == 63:
            return 'USERS_TYPING_IN_CONVERSATION' # Пользователи печатают в беседе
        if id == 64:
            return 'USERS_AUDIO_RECORDING_IN_CONVERSTION' # Пользователи записывают аудиосообщение в беседе
        if id == 70:
            return 'USER_CALLED' # Пользователь совершил аудиозвонок
        if id == 80:
            return 'COUNTER_CHANGE' # Счетчик изменен
        if id == 114:
            return 'NOTIFY_SETTINGS_CHANGED' # Изменены настройки уведомлений
        return 'NON_VK_EVENT' # Не явяется событием ВКонтакте
