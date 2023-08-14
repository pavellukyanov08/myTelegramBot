import webbrowser
import telebot
from telebot import types

bot = telebot.TeleBot('6388807339:AAEJPpiQU9Dglc0ktsSBVFigksgcCIlWuh4')

# В этом файле созданы обычные функции для работы с ботом


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)

    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Удалить текст')
    markup.row(btn2, btn3)

    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='www.google.com')
    markup.row(btn1)

    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить фото', callback_data='edit')
    markup.row(btn2, btn3)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.delete_message('Edit text', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['start'])
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id,
                     f'Что хотите увидеть?: \n'
                     f'Телеграм разработчика: {webbrowser.open("https://t.me/Lukianov08")} \n'
                     f'GitHub разработчика : {webbrowser.open("https://github.com/pavellukyanov08")}')


bot.polling(none_stop=True)
