from aiogram import Dispatcher, types
from config import bot


async def quiz2(call: types.CallbackQuery):
    ques = 'Что за клуб?'
    answer = [
        'Бавария',
        'Боруссия',
        'Барселона',
        'Байер'
    ]
    photo = open('media/logo.webp', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='Не верно! Это Бавария'
    )


def reg_hand_callback(db: Dispatcher):
    db.register_callback_query_handler(quiz2, text='button')
