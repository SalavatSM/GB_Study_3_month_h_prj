from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
).add(
    KeyboardButton('Cancel')
)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
)

yes_button = KeyboardButton('Yes')
no_button = KeyboardButton('No')
cancel_button = KeyboardButton('Cancel')

submit_markup.add(yes_button, no_button, cancel_button)
