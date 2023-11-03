from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def view_appartment() -> ReplyKeyboardMarkup:
    view_button = KeyboardButton(text='Показать🏡')

    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(view_button)

    return keyboard
