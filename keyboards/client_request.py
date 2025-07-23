from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
button = types.KeyboardButton('Оставить заявку')
markup.add(button)
