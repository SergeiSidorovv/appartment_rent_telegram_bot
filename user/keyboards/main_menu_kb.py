from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def menu_kb() -> ReplyKeyboardMarkup:

    button_start_search = KeyboardButton(text='Начать поиск🏡')
    buttun_view_favourite = KeyboardButton(text='Избранные объявления❤️')

    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
        )
    keyboard.add(button_start_search).add(buttun_view_favourite)

    return keyboard
