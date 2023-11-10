from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def show_action() -> InlineKeyboardMarkup:
    inlkb = InlineKeyboardMarkup(row_width=2)

    button_like = InlineKeyboardButton(
        text='❤️', callback_data='add_favourites')
    button_next_appartment = InlineKeyboardButton(
        'Следующее объявление⬇️', callback_data='next_app')

    inlkb.add(button_like, button_next_appartment)

    return inlkb


def delete_favourites() -> InlineKeyboardMarkup:
    inlkb = InlineKeyboardMarkup(row_width=1)
    button_delete = InlineKeyboardButton(
        text='Удалить❌', callback_data='delete')

    inlkb.add(button_delete)

    return inlkb
