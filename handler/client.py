from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from KeyBoard.Client_kb import start_markup


async def start_handler(massage: types.Message):
    await bot.send_message(massage.chat.id, f'привет {massage.from_user.first_name}', reply_markup=start_markup)


async def quiz1(massage: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)

    ques = 'Откуда мем?'
    answer = [
        'Винкс',
        'Том и Джерри',
        'Спанч боб',
        'Симпсоны'
    ]
    photo = open('media/fdKZ-ZpN7iw.jpg', 'rb')
    await bot.send_photo(massage.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=massage.chat.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='Правильный ответ: Спанч боб',
        reply_markup=markup
    )


async def info_hand(message: types.Message):
    await message.answer('New function')


def reg_client(db: Dispatcher):
    db.register_message_handler(start_handler, commands=['start', 'hello'])
    db.register_message_handler(quiz1, commands=['quiz'])
    db.register_message_handler(info_hand, commands=['info'])
