from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from create_bot import bot, dp
from models.session_model import update_data
from models.session_model import get_data
from user.keyboards import user_kb
from models.session_model import add_data
from collection_data import start_pars


async def gen_search_appartment_data(data_criteria: FSMContext):
    global gen_search_appartment
    gen_search_appartment = start_pars.collection_data(data_criteria)


async def check_availability_data(message: Message, data_criteria: FSMContext):
    await gen_search_appartment_data(data_criteria)

    gen_appartments = await anext(gen_search_appartment)
    count_appartments = len(gen_appartments.keys())

    if count_appartments == 0:
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
