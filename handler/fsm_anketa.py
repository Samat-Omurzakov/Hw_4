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
        await message.answer('Whats your name?')
    else:
        await message.answer('Only 1vs1')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['id'] = message.from_user.id
        date['username'] = message.from_user.username
        date['name'] = message.text
        print(date)
    await FSMAdmin.next()
    await message.answer('How old are you?')


def reg_hand_anketa(db: Dispatcher):
    db.register_message_handler(fsm_start, commands=['reg'])
    db.register_message_handler(load_name, state=FSMAdmin.name)
