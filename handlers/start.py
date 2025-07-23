from telebot.types import Message
from config_data.config import DEFAULT_COMMANDS
from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.reply_to(message, f'Привет! Это твой личный ассистент.\n'
                          f'Я помогу тебе выбрать услугу и передам заявку нашей команде.\n'
                          f'Нажми /{DEFAULT_COMMANDS[1][0]} , чтобы посмотреть, что мы предлагаем,'
                          f' или выбери действие из меню ниже.')