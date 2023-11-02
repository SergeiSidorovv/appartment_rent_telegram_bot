import logging
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import bot, dp
from user.criteria.criteria import get_citys, get_count_rooms, get_types_rent, get_filters
from user.criteria.view_criteria import view_citys, view_count_rooms, view_filters
from user.handlers import check_data_hand


class SelectCriteria(StatesGroup):
    city = State()
    count_room = State()
    type_rent = State()
    filter_output = State()


async def start_select_criteria(message: Message):
    await bot.send_message(message.from_user.id,
                           "Вы начали выбирать критерии, если захотите отменить написанное, напишите 'отменить'")

    await SelectCriteria.city.set()
    await bot.send_message(chat_id=message.from_user.id, text=f"{await view_citys(get_citys())}")
    await bot.send_message(chat_id=message.from_user.id, text="Напишите город из списка")


async def cancel_handler_select_criteria(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)

    await state.finish()
    await message.reply('отменить')
    await start_select_criteria(message)


async def select_city(message: Message, state: FSMContext):
    async with state.proxy() as data_criteria:
        citys = get_citys()
        if message.text.lower() in citys.keys():
            data_criteria['city'] = citys[message.text.lower()]

            await SelectCriteria.next()
            await bot.send_message(chat_id=message.from_user.id, text=f"{await view_count_rooms(get_count_rooms())}")
            await bot.send_message(chat_id=message.from_user.id, text="Напишите кол-во комнат")
        else:
            await bot.send_message(chat_id=message.from_user.id,
                                   text="По такому городу я пока не могу найти варианты, извините( \n Попробуйте написать другой город!")


async def select_count_rooms(message: Message, state: FSMContext):
    async with state.proxy() as data_criteria:
        count_rooms = get_count_rooms()
        if message.text.lower() in count_rooms.keys():
            data_criteria['count_rooms'] = count_rooms[message.text.lower()]

            await SelectCriteria.next()
            await bot.send_message(chat_id=message.from_user.id, text="Теперь напишите тип аредны: 'Посуточно' или 'На длительный срок'")
        else:
            await bot.send_message(chat_id=message.from_user.id,
                                   text="По такому запросу я ничего не нашёл, извините( \n Попробуйте написать другое количество комнат!")


async def select_types_rent(message: Message, state: FSMContext):
    async with state.proxy() as data_criteria:
        types_rent = get_types_rent()
        if message.text.lower() in types_rent.keys():
            data_criteria['type_rent'] = types_rent[message.text.lower()]

            await SelectCriteria.next()
            await bot.send_message(chat_id=message.from_user.id, text=f"{await view_filters(get_filters())}")
            await bot.send_message(chat_id=message.from_user.id, text="Напишите по какому фильтру вывести предложения")
        else:
            await bot.send_message(chat_id=message.from_user.id,
                                   text="По такому запросу я ничего не нашёл, извините( \n Попробуйте написать другой тип аренды!")


async def select_filter_output(message: Message, state: FSMContext):
    async with state.proxy() as data_criteria:
        filters_output = get_filters()
        if message.text.lower() in filters_output.keys():
            data_criteria['filter'] = filters_output[message.text.lower()]
            await check_data_hand.check_availability_data(message, data_criteria)
            await state.finish()
        else:
            await bot.send_message(chat_id=message.from_user.id,
                                   text="По такому запросу я ничего не нашёл, извините( \n Попробуйте написать другой тип фильтра !")


def register_handler_select_criteria(dp: Dispatcher):
    dp.register_message_handler(start_select_criteria, Text(
        equals='Начать поиск🏡', ignore_case=True), state=None)
    dp.register_message_handler(cancel_handler_select_criteria, Text(
        equals='отменить', ignore_case=True), state='*')
    dp.register_message_handler(select_city, state=SelectCriteria.city)
    dp.register_message_handler(
        select_count_rooms, state=SelectCriteria.count_room)
    dp.register_message_handler(
        select_types_rent, state=SelectCriteria.type_rent)
    dp.register_message_handler(
        select_filter_output, state=SelectCriteria.filter_output)
