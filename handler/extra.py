from aiogram import Dispatcher, types
from config import bot


async def python(massage: types.Message):
    if massage.text.lower() == 'python':
        await bot.send_dice(massage.chat.id)


users = {}


async def check_ban(message: types.Message):
    username = message.from_user.username
    if username:
        username = username
    else:
        username = message.from_user.first_name
    if message.from_user.username is not users:
        users[f'@{username}'] = message.from_user.id


def reg_hand_extra(db: Dispatcher):
    db.register_message_handler(check_ban)
    db.register_message_handler(python)
