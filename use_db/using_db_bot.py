import telebot
import sqlite3 as sq

from dotenv import load_dotenv
import os

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))


# В этом файле будет работа с базой данных для бота

name, password = None, None


@bot.message_handler(commands=['start'])
def start(message):
    conn = sq.connect('myTeleBot.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    pass VARCHAR(50) NOT NULL);
                    ''')
    conn.commit()

    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем!')
    bot.send_message(message.chat.id, 'Введи свое имя: ')
    bot.register_next_step_handler(message, get_username)


# def get_userdata(message):
#     global name, password
#
#     bot.send_message(message.chat.id, 'Введи свое имя: ')
#     name = message.text.strip()
#
#     bot.send_message(message.chat.id, 'Введи пароль: ')
#     password = message.text.strip()
#
#     bot.register_next_step_handler(message, add_user)

def get_username(message):
    global name
    name = message.text.strip()

    bot.send_message(message.chat.id, 'Введи пароль: ')
    bot.register_next_step_handler(message, get_password)


def get_password(message):
    global password
    password = message.text.strip()
    bot.register_next_step_handler(message, add_user)


def add_user(message):
    conn = sq.connect('myTeleBot.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, pass) VALUES (?, ?)", (name, password))
    conn.commit()

    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sq.connect('myTeleBot.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    lst_users = ''
    for us in users:
        lst_users += f'Имя: {us[1]}, пароль: {us[2]}\n'

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, str(lst_users))


bot.polling(none_stop=True)
