from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # linking cash to the bot, stores data in RAM

storage = MemoryStorage()  # creating object of MemoryStorage class

TOKEN = config("TOKEN")

BASE_URL = 'https://imgflip.com/i/'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

ADMINS = (6193713465,)
