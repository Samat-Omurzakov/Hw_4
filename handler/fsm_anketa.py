from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text


class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    photo = State()
    gender = State()
    region = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.name.set()
        await message.answer('Кто ты воин?')
    else:
        await message.answer('Только 1vs1')


async def fsm_age(message: types.Message, state: FSMContext):
    try:
        if 18 <= int(message.text) <= 99:
            async with state.proxy() as date:
                date['age'] = int(message.text)
                await FSMAdmin.gender.set()
                await message.answer('Пол?')
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
            await message.answer('Скажи где ты находишся?')
    else:
        await message.answer('Быть не может')


async def fsm_region(message: types.Message, state: FSMContext):
    if message.text.isalpha():
        async with state.proxy() as date:
            date['region'] = message.text
            await message.answer('DONE')
    else:
        await message.answer('Не нашел')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['id'] = message.from_user.id
        date['username'] = message.from_user.username
        date['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Сколько годиков?')


def reg_hand_anketa(db: Dispatcher):
    db.register_message_handler(fsm_start, commands=['reg'])
    db.register_message_handler(load_name, state=FSMAdmin.name)
    db.register_message_handler(fsm_age, state=FSMAdmin.age)
    db.register_message_handler(fsm_gender, state=FSMAdmin.gender)
    db.register_message_handler(fsm_region, state=FSMAdmin.region)
