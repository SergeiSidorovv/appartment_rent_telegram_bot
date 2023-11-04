from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import dp, bot
from user.keyboards.user_kb import menu_kb


async def main_menu(message: Message):
    await bot.send_message(message.from_user.id, "выберите один из пунктов меню!", reply_markup=menu_kb())


def register_handlers_main_menu(dp: Dispatcher):
    dp.register_message_handler(main_menu, Text(
        equals='Главное меню', ignore_case=True))
