from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, ADMINS
from database.bot_db import sql_command_all, sql_command_delete
from handlers.clients import delete_data

# async def delete_data(message: types.Message):
#     if message.from_user.id not in ADMINS:
#         await message.answer("You are not BOSS her!")
#     else:
#         users = await sql_command_all()
#         for user in users:
#             await message.answer(
#                 f"{user[2]} was chosen to be deleted",
#                 reply_markup=InlineKeyboardMarkup().add(
#                     InlineKeyboardMarkup(
#                         f"DELETE {user[2]}",
#                         callback_data=f"delete {user[0]}"
#                     )
#                 )
#             )

#
# def register_handlers_admin(dp: Dispatcher):
#     dp.register_message_handler(delete_data, commands=['delete'])

# async def pin_message(message: types.Message):
#     if message.reply_to_message:
#         await message.pin()
