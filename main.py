import config
import telebot
from telebot import types
import config_token

bot = telebot.TeleBot(config_token.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('начать работу', callback_data='data_collection'))
    markup.add(types.InlineKeyboardButton('изучить преимущества', callback_data='advantages'))
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!\n{config.DESCRIPTION}', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'data_collection':
        bot.send_message(callback.message.chat.id, f'Введите ваш возраст')
    if callback.data == 'advantages':
        bot.send_message(callback.message.chat.id, f'{config.ADVANTAGES}')

bot.polling(none_stop=True)
