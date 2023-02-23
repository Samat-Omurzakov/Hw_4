from aiogram import Dispatcher, types
from config import bot


async def ban(message: types.Message):
    if message.chat.type != 'private':
        await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await message.answer('Он вышел сам!')
    else:
        await message.answer('Попутал')


def reg_ban(db: Dispatcher):
    db.register_message_handler(ban, commands=['ban'], commands_prefix=['!'])