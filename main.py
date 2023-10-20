import logging

from aiogram.utils import executor

from create_bot import dp

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
