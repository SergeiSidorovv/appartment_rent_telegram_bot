from aiogram.types import Message
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters import Text

from collection_data import start_pars
from create_bot import bot, dp
from models.session_model import get_data


async def gen_view_appartment_data(message: Message):
    global gen_veiw_appartment
    gen_veiw_appartment = get_data.get_appartment(message.from_user.id)


async def view_appartment(message: Message):
    await gen_view_appartment_data(message)
    appartment = next(gen_veiw_appartment)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"🏡{appartment['info']}\
                                \n💰{appartment['price']}\
                                \n💻{appartment['url']}")


def register_handler_view(dp: Dispatcher):
    dp.register_message_handler(view_appartment, Text(
        equals='Показать🏡', ignore_case=True))
