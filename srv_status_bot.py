#!/usr/bin/env python3
import os
import subprocess
import telebot
import settings #модуль содержит токен досутпа к телеграм боту

'''
Установка модулья telebot:
pip3 install pyTelegramBotAPI
'''

'''settings.token - ссылка на токен из модуля settings.py
пример settings.py :
#!/usr/bin/env python3
token = '142341236387:Aasd6e8ddQfP-WLU9asdOMqwepqwnemFmY'
'''
bot = telebot.TeleBot(settings.token, parse_mode=None)


# Функция ping
def ping(host):
    hostname = host
    response = os.system("ping -c 1 " + hostname)
    command = ['ping', '-c', '2', hostname]
    output = subprocess.run(command, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, encoding='utf-8')
    send_output = str(output.stdout)
    if response == 0:
        send_message = hostname + ' ' + 'is up!'
        print(send_message)
    else:
        print(hostname, 'is down!')
        send_message = hostname + ' ' + 'is down!'
    return send_message, send_output


@bot.message_handler(content_types=['text'])
def send_ping_message(message):
    send_message_user_up_down, send_message_user_output = ping(message.text)
    bot.send_message(message.chat.id, send_message_user_up_down + '\n' + send_message_user_output)


bot.polling(none_stop=True)
