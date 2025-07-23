from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup()


keyboard.add(InlineKeyboardButton('Telegram-бот под ключ', callback_data='service_Telegram-бот'))
keyboard.add(InlineKeyboardButton('Создание Mini Apps', callback_data='service_Mini Apps'))
keyboard.add(InlineKeyboardButton('Сопровождение и доработка ботов', callback_data='service_Сопровождение и доработка'))
keyboard.add(InlineKeyboardButton('Консультации и проектирование', callback_data='service_Консультации и проектирование'))



