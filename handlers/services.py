import re

from telebot.types import Message

from database.models import db
from database.CRUD import CRUDInterface
from database.models import Client
from loader import bot
from keyboards.client_request import markup
from keyboards.service_selection import keyboard
from states.user_request import UserRequest


contact = {'name': '', 'phone': ''}
db_write = CRUDInterface.create()

@bot.message_handler(commands=['services'])
def services(message: Message) -> None:
    bot.reply_to(message, 'Разработка Telegram-ботов под ключ:\n'
                          '– Автоматизация заявок, рассылок, FAQ, квизов\n'
                          '– Воронки, формы, CRM-интеграции.\n\n'
                          'Создание Mini Apps (встроенных приложений в Telegram):\n'
                          '– Интерфейс с кнопками, формами, каталогами\n'
                          '– Подключение к API, базам данных, платёжным системам\n\n'
                          'Сопровождение и доработка ботов\n'
                          '– Поддержка существующих решений\n'
                          '– Рефакторинг, добавление новых функций\n'
                          '– Оптимизация скорости\n\n'
                          'Консультации и проектирование\n'
                          '– Поможем спроектировать логику бота от А до Я под вашу задачу\n'
                          '– Оценим сложность, сроки, подскажем лучшие практики.\n\n'
                          'Оставьте заявку по кнопке ниже 👇',
                 reply_markup = markup
    )

@bot.message_handler(func=lambda message: message.text == 'Оставить заявку')
def name(message: Message) -> None:
    bot.send_message(message.from_user.id, 'Напишите ваше имя:')
    bot.set_state(message.from_user.id, UserRequest.phone, message.chat.id)


@bot.message_handler(state=UserRequest.phone)
def phone(message: Message) -> None:
    contact['name'] = message.text
    bot.send_message(message.from_user.id, 'Напишите номер телефона в формате +79990001122:')
    bot.set_state(message.from_user.id, UserRequest.service, message.chat.id)

@bot.message_handler(state=UserRequest.service)
def service(message: Message) -> None:
    pattern = r'^\+7\d{10}$'
    if not re.match(pattern, message.text):
        bot.send_message(message.from_user.id, 'Введён некорректный номер, введи повторно.')
    else:
        contact['phone'] = message.text
        bot.send_message(message.from_user.id, 'Выберите интересующую услугу.', reply_markup=keyboard)


@bot.callback_query_handler(lambda call: call.data.startswith('service_'))
def data_storage(call):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    text = call.data
    service_name = text.split('_')[1]
    data = [
        {'id': call.from_user.id,
         'name': contact['name'],
         'phone': contact['phone'],
         'service': service_name

        }
    ]
    db_write(db, Client, data)

    bot.send_message(call.from_user.id, 'Спасибо за обращение. Свяжемся с вами в ближайшее время.')


