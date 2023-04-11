from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from decouple import config
import logging
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from bs4 import BeautifulSoup

TOKEN = config("TOKEN")
BASE_URL = "https://imgflip.com/i/"
MEM_TEMP = "<div><img src={}></div>"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

def get_random_meme():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        img_url = 'https:' + soup.find('img', id='im')['src']
    except TypeError:
        img_url = 'https:' + soup.find('video', id='vid')[poster]
    return img_url



@dp.message_handler(commands=['quiz'])
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
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Soon you will become a python developer!",
        open_period=10,
        reply_markup=markup,
    )

@dp.callback_query_handler(text="quiz_1_button")
async def quiz_2(call: types.CallbackQuery):
    question = 'Which of the following types of loops are not supported in Python?'
    answers = [
        'for',
        'while',
        'do-while'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Soon you will become a python developer!",
        open_period=10,
    )


@dp.message_handler(commands=['mem'])
async def echo(message: types.Message):
    await message.reply(get_random_meme())


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(chat_id=message.from_user.id, text=int(message.text)**2)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

