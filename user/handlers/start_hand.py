from aiogram.types import Message
from aiogram import Dispatcher

from create_bot import dp, bot
from user.handlers import registration_hand


async def start(message: Message):
    if message.values['chat']['type'] == 'private':
        await bot.send_message(message.from_user.id,
                               f"Привет! {message.values['from']['first_name']}"
                               )
        await registration_hand.check_registration(message)
    else:
        await message.answer("Общение с ботом происходит через личные сообщения!\n https://t.me/RentAppartmentTelegrammBot")


async def help(message: Message):
    if message.values['chat']['type'] == 'private':
        await bot.send_message(message.from_user.id,
                               "/start - запустить бота или вернуться в главное меню \n/help - информация по командам"
                               )
    else:
        await message.answer("Общение с ботом происходит через личные сообщения!\n https://t.me/RentAppartmentTelegrammBot")


def register_handlers_start_help(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
