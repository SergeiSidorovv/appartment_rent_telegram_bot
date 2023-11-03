import logging

from aiogram.utils import executor

from create_bot import dp
from user.handlers import start_hand
from user.handlers import main_menu_hand
from user.handlers import select_critaria_hand
from user.handlers import registration_hand
from user.handlers import view_appartments_hand


async def on_start(_):
    start_hand.register_handlers_start_help(dp)
    main_menu_hand.register_handlers_main_menu(dp)
    select_critaria_hand.register_handler_select_criteria(dp)
    # view_appartments_hand.register_handler_view_appartment(dp)
    registration_hand.register_handlers_registration(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
