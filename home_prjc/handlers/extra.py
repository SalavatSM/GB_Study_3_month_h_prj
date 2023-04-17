from aiogram import Dispatcher, types
# from config import bot, dp
import random


async def filter_bad_words(message: types.Message):
    bad_words = ['html', 'java', 'жинди', 'дурак']
    username = f'@{message.from_user.username}' if message.from_user.username else message.from_user.full_name
    for word in bad_words:
        if word in message.text.lower().replace(' ', ''):
            await message.answer(
                f'Не матерись @{username}!\n'
                f'Сам ты {word}!'
            )

    if message.text == 'game':
        emoji = ['⚽️', '🏀', '🎲', '🎯', '🎳', '🎰']
        await message.answer_dice(random.choice(emoji))

    # if message.text.isdigit():
    #     await message.answer(text=int(message.text)**2)
    # else:
    #     await message.answer(f'Bot does not know command like "{message.text}"!\n'
    #                          f'Please check your typing!')


# @dp.message_handler()
# async def echo(message: types.Message):
#     if message.text.isdigit():
#         await bot.send_message(chat_id=message.from_user.id, text=int(message.text)**2)
#     else:
#         await bot.send_message(chat_id=message.from_user.id, text=message.text)

def register_handlers_extra(dp: Dispatcher):
    # dp.register_message_handler(echo)
    dp.register_message_handler(filter_bad_words)
