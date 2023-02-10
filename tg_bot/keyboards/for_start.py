from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from emoji import emojize
from enum import StrEnum


class ActionText(StrEnum):
    CATALOG = emojize(":green_book: Каталог")
    PROFILE = emojize("😊 Мой профиль")
    ORDERS = emojize(":clipboard: Мои заказы")
    CONTACTS = emojize("📱 Наши контакты")
    INVITE = emojize(":link: Пригласить друга")


def get_start_keyboard() -> InlineKeyboardMarkup:
    keybaord_builder = InlineKeyboardBuilder()
    for action_text in ActionText:
        web_app_info = WebAppInfo(url="https://google.com")
        keybaord_builder.row(InlineKeyboardButton(text=action_text, web_app=web_app_info))
    return keybaord_builder.as_markup()
