import requests
import telebot
import datetime

bot = telebot.TeleBot('6388807339:AAEJPpiQU9Dglc0ktsSBVFigksgcCIlWuh4')
weather_api = 'b40831904944d1d993818578a2133983'


def get_current_weather():
    # city = message.text.strip().lower()
    url_base = 'https://api.openweathermap.org/data/2.5/'

    response = requests.get(url_base + 'forecast', params={'q': 'London', 'appid': weather_api,
                                                           'units': 'metric', 'cnt': 7})

    if response.status_code == 200:
        data = response.json()
        daily_forecast = data['list']

        weather_info = ''
        for day in daily_forecast:
            date = day['dt_txt']
            weather = day['weather'][0]['description']
            curr_temp = day['main']['temp']
            max_temp = day['main']['temp_max']
            min_temp = day['main']['temp_min']
            humidity = day['main']['humidity']
            wind_speed = day['wind']['speed']

            day_info = f'Дата: {date}\n' \
                       f'Подробности: {weather}\n' \
                       f'Текущая температура: {curr_temp}°C\n' \
                       f'Макс. температура: {max_temp}°C\n' \
                       f'Мин. температура: {min_temp}°C\n' \
                       f'Влажность %: {humidity}\n' \
                       f'Скорость ветра: {wind_speed} м/с\n' \
                       f'==========================================\n'
            weather_info += day_info
        print(weather_info)


get_current_weather()
    # if response:
    #     weather_info = ''
    #     for day in response['list']:
    #         date = day['dt_txt']  # Дата для текущего дня
    #         weather = day['weather'][0]['description']
    #         curr_temp = day['main']['temp']
    #         max_temp = day['main']['temp_max']
    #         min_temp = day['main']['temp_min']
    #         humidity = day['main']['humidity']
    #         wind_speed = day['wind']['speed']
    #
    #         day_of_week = week_days[datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').weekday()]

            # day_info = f'День недели: {day_of_week}\n' \
            #            f'Подробности: {weather}\n' \
            #            f'Текущая температура: {curr_temp}°C\n' \
            #            f'Макс. температура: {max_temp}°C\n' \
            #            f'Мин. температура: {min_temp}°C\n' \
            #            f'Влажность %: {humidity}\n' \
            #            f'Скорость ветра: {wind_speed} м/с\n' \
            #            f'==========================================\n'
            # weather_info += day_info


# import requests
# import telebot
# import datetime
#
#
# bot = telebot.TeleBot('6388807339:AAEJPpiQU9Dglc0ktsSBVFigksgcCIlWuh4')
# weather_api = 'b40831904944d1d993818578a2133983'
# url_base = 'https://api.openweathermap.org/data/2.5/'
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')
#
#
# @bot.message_handler(content_types=['text'])
# def get_current_weather(message):
#     city = message.text.strip().lower()
#
#     response = requests.get(url_base + 'forecast', params={'q': city, 'appid': weather_api,
#                                                            'units': 'metric'}).json()
#
#     week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#
#     if response:
#         weather_info = ''
#         for i in range(7):
#             day = response['list'][i]
#             date = day['dt_txt']
#             weather = day['weather'][0]['description']
#             curr_temp = day['main']['temp']
#             max_temp = day['main']['temp_max']
#             min_temp = day['main']['temp_min']
#             humidity = day['main']['humidity']
#             wind_speed = day['wind']['speed']
#
#             day_of_week = week_days[datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').weekday()]
#
#             day_info = f'День недели: {day_of_week}\n' \
#                            f'Подробности: {weather}\n' \
#                            f'Текущая температура: {curr_temp}°C\n' \
#                            f'Макс. температура: {max_temp}°C\n' \
#                            f'Мин. температура: {min_temp}°C\n' \
#                            f'Влажность %: {humidity}\n' \
#                            f'Скорость ветра: {wind_speed} м/с\n' \
#                            f'==========================================\n'
#             weather_info += day_info
#
#         bot.reply_to(message, f'Прогноз погоды на неделю: {weather_info}')
#
#
# bot.polling(none_stop=True)
