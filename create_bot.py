from aiogram import Bot, Dispatcher
from os import getenv
from dotenv import load_dotenv, find_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

load_dotenv(find_dotenv())
bot = Bot(getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)
