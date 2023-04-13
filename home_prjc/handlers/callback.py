from aiogram import Dispatcher, types
from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# @dp.callback_query_handler(text="quiz_1_button")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton("NEXT", callback_data="quiz_2_button")
    markup.add(button_2)

    question = 'Which of the following types of loops are not supported in Python?'
    answers = [
        'for',
        'while',
        'do-while'
    ]
    await bot.send_poll(
        # chat_id=call.from_user.id,
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Soon you will become a python developer!",
        open_period=10,
        reply_markup=markup,
    )


async def quiz_3(call: types.CallbackQuery):
    question = 'Which of the following is false statement in python?'
    answers = [
        'int(114) == 144',
        'int(114.0) == 144',
        'None of the above'
    ]
    await bot.send_poll(
        # chat_id=call.from_user.id,
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Soon you will become a python developer!",
        open_period=10,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="quiz_1_button")
    dp.register_callback_query_handler(quiz_3, text="quiz_2_button")
