from telebot.handler_backends import State, StatesGroup

class UserRequest(StatesGroup):
    phone = State()
    service = State()