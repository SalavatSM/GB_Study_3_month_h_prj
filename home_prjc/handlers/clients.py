from aiogram import Dispatcher, types
from config import bot, dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from time import sleep
import random
import requests
from bs4 import BeautifulSoup
from config import BASE_URL


# shows random meme
def get_random_meme():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        img_url = 'https:' + soup.find('img', id='im')['src']
    except TypeError:
        img_url = 'https:' + soup.find('video', id='vid')[poster]
    return img_url


# pin message
async def pin_message(message: types.Message):
    await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)


# dice game
async def dice_message(message: types.Message):
    await message.answer(f'Ok, let us play some game! \n I go first.')
    a = await message.answer_dice(emoji='🎲')
    sleep(4)
    await message.answer(f'This is my dice number.')
    b = await message.answer_dice(emoji='🎲')
    sleep(4)
    await message.answer((f'This is your dice number.'))
    sleep(1)
    if a.dice.value > b.dice.value:
        await message.answer(f'My number: {a.dice.value} and it is bigger then yours!\n So, I win the game!')
    elif a.dice.value == b.dice.value:
        await message.answer(f'Our numbers is iqual. It is draw.')
    else:
        await message.answer(f'Your number: {b.dice.value} and it is bigger then mine!\n So, you win the game!')


# quiz
# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="quiz_1_button")
    markup.add(button_1)

    question = 'Which of the following concepts is not a part of Python?'
    answers = [
        'Pointers',
        'Loops',
        'Dynamic Typing'
    ]
    await bot.send_poll(
        # chat_id=message.from_user.id,
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Soon you will become a python developer!",
        open_period=10,
        reply_markup=markup,
    )


# @dp.message_handler(commands=['mem'])
async def start_command(message: types.Message):
    await message.reply(get_random_meme())


def register_handlers_clients(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin_message, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(dice_message, commands=['dice'])
