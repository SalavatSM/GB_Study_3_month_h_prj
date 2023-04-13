from aiogram import Dispatcher, types
from config import bot, ADMINS
from time import sleep


# async def pin_message(message: types.Message):
#     if message.reply_to_message:
#         await message.pin()