from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from .client_kb import submit_markup, cancel_markup
from config import bot

from database.bot_db import sql_command_insert


class FSMAdmin(StatesGroup):
    mentor_id = State()
    mentor_name = State()
    study_direction = State()
    mentor_age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.mentor_id.set()
        await message.answer("Give me the mentor ID.", reply_markup=cancel_markup)
    else:
        await message.answer("Write to direct!")


async def load_mentor_id(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("It should be number. Check yourself!")
    else:
        async with state.proxy() as data:
            data["mentor_id"] = message.text
            print(data)
        await FSMAdmin.next()
        await message.answer("Give me the mentor name.", reply_markup=cancel_markup)


async def load_mentor_name(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await message.answer("It should be letter. Check yourself!")
    elif len(message.text) > 16:
        await message.answer("Length of name con not be longer then 16 characters!")
    else:
        async with state.proxy() as data:
            data["mentor_name"] = message.text
            print(data)
        await FSMAdmin.next()
        await message.answer("Give me the study direction.", reply_markup=cancel_markup)


async def load_study_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["study_direction"] = message.text
        print(data)
    await FSMAdmin.next()
    await message.answer("Give me the mentor age.", reply_markup=cancel_markup)


async def load_mentor_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("It should be number. Check yourself!")
    elif not 16 < int(message.text) < 60:
        await message.answer("Access Denied!")
    else:
        async with state.proxy() as data:
            data["mentor_age"] = message.text
            print(data)
        await FSMAdmin.next()
        await message.answer("Give me the study group.", reply_markup=cancel_markup)


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["group"] = message.text
        await message.answer(f"Mentor's id: {data['mentor_id']}\nMentor's name: {data['mentor_name']}\n"
                             f"Study direction: {data['study_direction']}\nMentor's age: {data['mentor_age']}\n"
                             f"Group: {data['group']}")
        print(data)
    await FSMAdmin.next()
    await message.answer("Is collected data correct?", reply_markup=submit_markup)


async def submit_state(message: types.Message, state: FSMContext):
    if message.text.lower() not in ['yes', 'no']:
        await message.answer("Use buttons!")
    elif message.text.lower() == "yes":
        await sql_command_insert(state)  # calling sql commands
        await state.finish()  # here cash is cleaned (that's why we have to write data to DB before call this func)
        await message.answer("The data about mentor collected. Thank you!")
    elif message.text.lower() == "no":
        await FSMAdmin.mentor_id.set()
        await message.answer("Give me the mentor ID.", reply_markup=cancel_markup)


async def cansel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.answer("Registration is canceled.")


def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(cansel_reg, Text(equals='cancel', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, Text(equals='reg', ignore_case=True))
    dp.register_message_handler(load_mentor_id, state=FSMAdmin.mentor_id)
    dp.register_message_handler(load_mentor_name, state=FSMAdmin.mentor_name)
    dp.register_message_handler(load_study_direction, state=FSMAdmin.study_direction)
    dp.register_message_handler(load_mentor_age, state=FSMAdmin.mentor_age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit_state, state=FSMAdmin.submit)
