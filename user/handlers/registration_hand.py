import logging
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters import Text

from models.session_model import registration_session
from user.handlers import main_menu_hand
from create_bot import dp, bot


class RegistrationUser(StatesGroup):

    user_telegram_id = State()
    nick_name = State()


async def start_registration(message: Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Для начала работы бота, необходимо зарегестрироваться!")
    await bot.send_message(chat_id=message.from_user.id,
                           text="Если захотите отменить действие напишите отменить")

    await RegistrationUser.user_telegram_id.set()
    await bot.send_message(chat_id=message.from_user.id, text="Пожалуйста введите любой текст!")


async def cancel_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)
    await state.finish()
    await message.reply('отменить')


async def add_user_telegram_id(message: Message, state: FSMContext) -> None:
    async with state.proxy() as reg_data:
        reg_data['user_telegram_id'] = message.from_user.id
        await RegistrationUser.next()
        await bot.send_message(chat_id=message.from_user.id, text="Пожалуйста введите свой никнейм!")


async def add_nick_name(message: Message, state: FSMContext):
    nick_name_length = 100
    async with state.proxy() as reg_data:
        if len(message.text) <= nick_name_length and "@" not in message.text and "/" not in message.text:
            reg_data['nick_name'] = message.text
            registration_session.add_user(reg_data)
            await state.finish()
            await main_menu_hand.main_menu(message)
        else:
            await bot.send_message(message.from_user.id,
                                   "Никнейм не должен превышать 100 символов, и содержать символы '@'' '/'")


async def check_registration(message: Message):
    registered_users = registration_session.get_users_telegram_id()

    if message.from_user.id not in registered_users:
        await start_registration(message)
    else:
        await bot.send_message(message.from_user.id, "Вы уже зарегистрированы!")
        await main_menu_hand.main_menu(message)


def register_handlers_registration(dp: Dispatcher):
    dp.register_message_handler(start_registration, state=None)
    dp.register_message_handler(cancel_handler, Text(
        equals='отменить', ignore_case=True), state='*')
    dp.register_message_handler(
        add_user_telegram_id, state=RegistrationUser.user_telegram_id)
    dp.register_message_handler(
        add_nick_name, state=RegistrationUser.nick_name)
