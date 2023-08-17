import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('6388807339:AAEJPpiQU9Dglc0ktsSBVFigksgcCIlWuh4')

currency = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['currency'])
def currency_converter(message):
    bot.send_message(message.chat.id, 'Привет, введите сумму: ')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат. Впишите сумму')
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=3)
        btn1 = types.InlineKeyboardButton('USB/RUB', callback_data='usd/rub')
        btn2 = types.InlineKeyboardButton('RUB/USD', callback_data='rub/usd')

        btn3 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn4 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')

        btn5 = types.InlineKeyboardButton('EUR/RUB', callback_data='eur/rub')
        btn6 = types.InlineKeyboardButton('RUB/EUR', callback_data='rub/eur')

        btn7 = types.InlineKeyboardButton('Другое значение', callback_data='else')

        markup.add(btn1, btn2, btn2, btn3, btn4, btn5, btn6, btn7)

        bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Введите число больше 0. Впишите сумму')
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        result = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'{amount} в {values[0]} '
                                               f'будет равно {round(result, 2)} в {values[1]}.\n'
                                               f'Можете сделать следующую конвертацию')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Введите пару значений через /')
        bot.register_next_step_handler(call.message, my_currency)


def my_currency(message):
    try:
        values = message.text.upper().split('/')
        result = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'{amount} в {values[0]} '
                                          f'будет равно {round(result, 2)} в {values[1]}.\n'
                                          f'Можете сделать следующую конвертацию')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Что-то пошло не так. Впишите сумму заново')
        bot.register_next_step_handler(message, summa)


bot.polling(none_stop=True)
