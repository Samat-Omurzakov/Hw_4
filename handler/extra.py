from aiogram import Dispatcher, types
from config import bot


async def python(massage: types.Message):
    if massage.text.lower() == 'python':
        await bot.send_dice(massage.chat.id)


def reg_hand_extra(db: Dispatcher):
    db.register_message_handler(python)
