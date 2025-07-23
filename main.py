from telebot.custom_filters import StateFilter
import handlers # noqa
from loader import bot
from  database.core import initialize_database
from utils.set_bot_command import set_default_commands

if __name__ == "__main__":
    initialize_database()
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    bot.infinity_polling()