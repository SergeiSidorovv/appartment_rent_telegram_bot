from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from user.keyboards import inline_kb
from create_bot import dp, bot
from models.session_model import favourite_session


async def view_favourites(message: Message):
    user_id = message["chat"]["id"]
    favourite_appartments = favourite_session.get_favourites(user_id)
    for i in favourite_appartments:
        await bot.send_message(chat_id=user_id,
                               text=f"🏡{i.info}\
                                \n💰{i.price}\
                                \n💻{i.url}",
                               reply_markup=inline_kb.delete_favourites())


async def add_favourites(message: Message) -> str:
    user_id = message["chat"]["id"]
    data_appartment = message["text"].split("\n")
    all_url = favourite_session.get_url_favourites(user_id)
    url_appartment = data_appartment[2][1::]

    if url_appartment in all_url:
        return "Уже было добавлено!"
    else:
        favourite_session.add_favourite(data_appartment, user_id)
        return "Вы добавили в избранное!"


async def delete_favourites(message: Message):
    user_id = message["chat"]["id"]
    data_appartment = message["text"].split("\n")

    favourite_session.delete_favourite(data_appartment, user_id)
    await message.delete()


def register_handlers_favourites(dp: Dispatcher):
    dp.register_message_handler(view_favourites, Text(
        equals='Избранные объявления❤️', ignore_case=True))
