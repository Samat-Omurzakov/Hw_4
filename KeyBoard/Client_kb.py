from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_button = KeyboardButton('/start')
info_button = KeyboardButton('/info')
quiz_button = KeyboardButton('/quiz')
reg_button = KeyboardButton('/reg')

location = KeyboardButton('location', request_location=True)
contact = KeyboardButton('contact', request_contact=True)

start_markup.add(start_button, info_button, quiz_button, location, contact, reg_button)

cancel = KeyboardButton('Cancel')

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton('Пушка'),
    KeyboardButton('Так себе'),
    cancel
)

gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton('Мужчина'),
    KeyboardButton('Женщина'),
    cancel
)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    cancel
)
