import logging

from aiogram.utils import executor

from create_bot import dp
from user.handlers import hand_start

async def on_start(_):
    hand_start.register_handlers_start_help(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
