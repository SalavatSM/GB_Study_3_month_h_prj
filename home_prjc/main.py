from aiogram.utils import executor
import logging

from config import dp
from handlers import clients, extra, callback

clients.register_handlers_clients(dp)
callback.register_handlers_callback(dp)

extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
