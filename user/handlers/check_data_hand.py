from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from create_bot import bot, dp
from user.keyboards import user_kb
from db import add_data, get_data, update_data
from collection_data import start_pars


async def check_availability_data(message: Message, data_criteria: FSMContext):
    appartments = start_pars.collection_data(data_criteria)
    gen_appartments = await anext(appartments)

    if len(gen_appartments.keys()) == 0:
        await bot.send_message(chat_id=message.chat.id,
                               text='К сожалению по вашим критериям я ничего не смог найти!\n Попробуйте ввести другие критерии нажав на кнопку "Начать поиск".',
                               reply_markup=user_kb.menu_kb())

    elif message.from_user.id not in get_data.get_user_id():
        add_data.add_appartments(gen_appartments, message.from_user.id)
        await bot.send_message(chat_id=message.chat.id, text='Нажми на кнопку показать!', reply_markup=user_kb.view_appartment())

    else:
        update_data.update_person_appartments(
            gen_appartments, message.from_user.id)
        await bot.send_message(chat_id=message.chat.id, text='Нажми на кнопку показать!', reply_markup=user_kb.view_appartment())
