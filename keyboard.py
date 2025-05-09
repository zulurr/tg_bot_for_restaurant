from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,
                           InlineKeyboardMarkup, KeyboardButtonPollType)

b1 = KeyboardButton(text='/start')
b2 = KeyboardButton(text='Меню')



keyboard_start = ReplyKeyboardMarkup(keyboard=[[b1, b2]], resize_keyboard=True)


c1 = KeyboardButton(text='Завтраки')
c2 = KeyboardButton(text='Холодные закуски')
c3 = KeyboardButton(text='Горячие блюда')
c4 = KeyboardButton(text='Супы')
c5 = KeyboardButton(text='Десерты')
c6 = KeyboardButton(text='Напитки')

keyboard_category = ReplyKeyboardMarkup(keyboard=[[c1, c2], [c3, c4], [c5, c6]])