from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import bot, dp
from models.session_model import get_data
from user.keyboards import inline_kb


async def gen_view_appartment_data(message: Message):
    global gen_veiw_appartment
    gen_veiw_appartment = get_data.get_appartment(message.from_user.id)


async def view_appartment(message: Message):
    await gen_view_appartment_data(message)
    appartment = next(gen_veiw_appartment)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"🏡{appartment['info']}\
                                \n💰{appartment['price']}\
                                \n💻{appartment['url']}",
                           reply_markup=inline_kb.show_action())


async def view_next_appartment(message: Message):
    appartment = next(gen_veiw_appartment)
    availability_app = appartment['info']
    if availability_app is not None:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"🏡{appartment['info']}\
                                \n💰{appartment['price']}\
                                \n💻{appartment['url']}",
                               reply_markup=inline_kb.show_action())


async def callback_appartment(callback: CallbackQuery):
    button_click = callback.data
    if button_click == 'next_app':
        await view_next_appartment(message=callback.message)
        await callback.answer(cache_time=True)

    elif button_click == 'add_favourites':
        pass


def register_handler_view(dp: Dispatcher):
    dp.register_message_handler(view_appartment, Text(
        equals='Показать🏡', ignore_case=True))
    dp.register_message_handler(view_next_appartment, Text())
