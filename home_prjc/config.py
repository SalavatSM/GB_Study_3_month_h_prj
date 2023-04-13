from aiogram import Bot, Dispatcher
from decouple import config

TOKEN = config("TOKEN")

BASE_URL = 'https://imgflip.com/i/'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

ADMINS = (6193713465,)
