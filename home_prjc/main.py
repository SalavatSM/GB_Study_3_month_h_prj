from aiogram.utils import executor
import logging

from config import dp, ADMINS, bot
from handlers import clients, extra, callback, fsmAdminMentor
from database.bot_db import sql_create

# admin.register_handlers_admin(dp)

clients.register_handlers_clients(dp)
callback.register_handlers_callback(dp)
fsmAdminMentor.register_handlers_fsm(dp)

extra.register_handlers_extra(dp)


async def on_startup(db):
    await bot.send_message(ADMINS[0], "I am live now!")
    sql_create()


async def on_shutdown(db):
    await bot.send_message(ADMINS[0], "I am done for today. Bay!")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)
