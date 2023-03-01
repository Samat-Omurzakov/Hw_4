from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from KeyBoard.Client_kb import *


class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    photo = State()
    gender = State()
    region = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.name.set()
        await message.answer('Кто ты воин?', reply_markup=cancel_markup)
    else:
        await message.answer('Только 1vs1')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['id'] = message.from_user.id
        date['username'] = message.from_user.username
        date['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Сколько годиков?', reply_markup=cancel_markup)


async def fsm_age(message: types.Message, state: FSMContext):
    try:
        if 18 <= int(message.text) <= 99:
            async with state.proxy() as date:
                date['age'] = int(message.text)
                await FSMAdmin.gender.set()
                await message.answer('Пол?', reply_markup=gender_markup)
        elif int(message.text) < 18:
            await message.answer('Маловат школьник')
        elif 99 < int(message.text):
            await message.answer('Отдыхай дедуля')
    except:
        await message.answer('Только числа!!!')


async def fsm_gender(message: types.Message, state: FSMContext):
    if message.text.isalpha():
        async with state.proxy() as date:
            date['gender'] = message.text
            await FSMAdmin.next()
            await message.answer('Скажи где ты находишся?', reply_markup=cancel_markup)
    else:
        await message.answer('Быть не может')


async def fsm_region(message: types.Message, state: FSMContext):
    if message.text.isalpha():
        async with state.proxy() as date:
            date['region'] = message.text
            await message.answer('Фотку давай', reply_markup=cancel_markup)
            await FSMAdmin.photo.set()
    else:
        await message.answer('Не нашел')


async def fsm_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['photo'] = message.photo[0].file_id
        await message.answer_photo(date['photo'],
                                   caption=f'{date["name"]} {date["age"]} {date["gender"]} @{date["username"]}')
    await FSMAdmin.submit.set()
    await message.answer('Ну как?', reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text == 'Пушка':
        await message.answer('DONE!')
        await state.finish()
    elif message.text == 'Так себе':
        await message.answer('Кто ты воин?')
        await FSMAdmin.name.set()
    else:
        await message.answer('???')


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Пока')


def reg_hand_anketa(db: Dispatcher):
    db.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state='*')
    db.register_message_handler(fsm_start, commands=['reg'])
    db.register_message_handler(load_name, state=FSMAdmin.name)
    db.register_message_handler(fsm_age, state=FSMAdmin.age)
    db.register_message_handler(fsm_gender, state=FSMAdmin.gender)
    db.register_message_handler(fsm_region, state=FSMAdmin.region)
    db.register_message_handler(fsm_photo, state=FSMAdmin.photo, content_types=['photo'])
    db.register_message_handler(submit, state=FSMAdmin.submit)
