from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from collection_data import start_pars
from create_bot import bot, dp
from user.keyboards import view_app_kb, main_menu_kb
from db.add_data import add_appartments
from db.delete_data import delete_appartments


async def check_availability_data(message: Message, data_criteria: FSMContext):
    appartments = start_pars.collection_data(data_criteria)
    app = await anext(appartments)
