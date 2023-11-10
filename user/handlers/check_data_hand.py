from aiogram.types import Message, ChatActions
from aiogram.dispatcher import FSMContext

from models.session_model import appartment_session
from user.keyboards import user_kb
from collection_data import start_pars
from create_bot import bot, dp


async def gen_search_appartment_data(message: Message, data_criteria: FSMContext):
    global gen_search_appartment
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    gen_search_appartment = start_pars.collection_data(data_criteria)


async def check_availability_data(message: Message, data_criteria: FSMContext):
    await gen_search_appartment_data(message, data_criteria)

    gen_appartments = await anext(gen_search_appartment)
    count_appartments = len(gen_appartments.keys())

    if count_appartments == 0:
        await bot.send_message(chat_id=message.chat.id,
                               text="К сожалению по вашим критериям я ничего не смог найти!\
                               \nПопробуйте ввести другие критерии нажав на кнопку 'Начать поиск'.",
                               reply_markup=user_kb.menu_kb()
                               )

    elif message.from_user.id not in appartment_session.get_user_id():
        appartment_session.add_appartments(
            gen_appartments, message.from_user.id)

        await bot.send_message(chat_id=message.chat.id,
                               text="Нажми на кнопку показать!",
                               reply_markup=user_kb.view_appartment()
                               )

    else:
        await chande_data(message.from_user.id, gen_appartments)


async def check_next_page_availability_data(person_id: int):
    gen_appartments = await anext(gen_search_appartment)
    count_appartments = len(gen_appartments.keys())

    if count_appartments == 0:
        await bot.send_message(chat_id=person_id,
                               text="К сожалению, по вашим критериям предложения закончились.\n\
                                    Попробуйте ввести другие критерии нажав на кнопку 'Начать поиск'.",
                               reply_markup=user_kb.menu_kb()
                               )

    else:
        await chande_data(person_id, gen_appartments)


async def chande_data(person_id: int, gen_appartments):
    appartment_session.update_person_appartments(
        gen_appartments,
        person_id
    )

    await bot.send_message(chat_id=person_id,
                           text="Нажми на кнопку показать!",
                           reply_markup=user_kb.view_appartment()
                           )
