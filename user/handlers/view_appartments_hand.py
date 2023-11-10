from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import bot, dp
from models.session_model import appartment_session
from user.keyboards import inline_kb
from user.handlers import check_data_hand, favourites_hand


async def gen_view_appartment_data(message: Message):
    global gen_veiw_appartment
    gen_veiw_appartment = appartment_session.get_appartment(
        message.from_user.id)


async def view_appartment(message: Message):
    await gen_view_appartment_data(message)
    appartment = next(gen_veiw_appartment)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"🏡{appartment['info']}\
                                \n💰{appartment['price']}\
                                \n💻{appartment['url']}",
                           reply_markup=inline_kb.show_action())


async def view_next_appartment(message: Message):
    try:
        appartment = next(gen_veiw_appartment)
        await bot.send_message(chat_id=message.chat.id,
                               text=f"🏡{appartment['info']}\
                                \n💰{appartment['price']}\
                                \n💻{appartment['url']}",
                               reply_markup=inline_kb.show_action())
    except:
        await bot.send_message(chat_id=message.chat.id,
                               text="Собираем ещё данные по вашему запросу.\n\
                                    Пожалуйста подождите!",
                               )
        await check_data_hand.check_next_page_availability_data(message.chat.id)


async def callback_appartment(callback: CallbackQuery):
    button_click = callback.data
    if button_click == 'next_app':
        await view_next_appartment(message=callback.message)
        await callback.answer(cache_time=True)

    elif button_click == 'add_favourites':
        check_message = await favourites_hand.add_favourites(message=callback.message)
        await callback.answer(check_message)
        await callback.answer(cache_time=True)

    elif button_click == 'delete':
        await favourites_hand.delete_favourites(message=callback.message)
        await callback.answer('Удалено из избранного')
        await callback.answer(cache_time=True)


def register_handler_view(dp: Dispatcher):
    dp.register_message_handler(view_appartment, Text(
        equals='Показать🏡', ignore_case=True))
    dp.register_callback_query_handler(callback_appartment)
