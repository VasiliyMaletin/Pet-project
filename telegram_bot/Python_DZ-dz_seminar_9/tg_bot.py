import telebot 
from telebot import types 
from controller import distribution
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
bot = telebot.TeleBot(os.getenv("TOKEN")) # 5822101823:AAFpIcEd5CiajDT-R_Hzzpeb1riElJBA4QM

print('Online')

value = ''
old_value = ''   
keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(   telebot.types.InlineKeyboardButton('C', callback_data = 'C'),
                telebot.types.InlineKeyboardButton('<=', callback_data = '<='),
                telebot.types.InlineKeyboardButton('( )', callback_data = '('),
                telebot.types.InlineKeyboardButton('/', callback_data = '/'))

keyboard.row(   telebot.types.InlineKeyboardButton('7', callback_data = '7'),
                telebot.types.InlineKeyboardButton('8', callback_data = '8'),
                telebot.types.InlineKeyboardButton('9', callback_data = '9'),
                telebot.types.InlineKeyboardButton('*', callback_data = '*'))

keyboard.row(   telebot.types.InlineKeyboardButton('4', callback_data = '4'),
                telebot.types.InlineKeyboardButton('5', callback_data = '5'),
                telebot.types.InlineKeyboardButton('6', callback_data = '6'),
                telebot.types.InlineKeyboardButton('-', callback_data = '-'))

keyboard.row(   telebot.types.InlineKeyboardButton('1', callback_data = '1'),
                telebot.types.InlineKeyboardButton('2', callback_data = '2'),
                telebot.types.InlineKeyboardButton('3', callback_data = '3'),
                telebot.types.InlineKeyboardButton('+', callback_data = '+'))

keyboard.row(   telebot.types.InlineKeyboardButton('j', callback_data = 'j'),
                telebot.types.InlineKeyboardButton('0', callback_data = '0'),
                telebot.types.InlineKeyboardButton(',', callback_data = ','),
                telebot.types.InlineKeyboardButton('=', callback_data = '='))
   
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    button1 = types.KeyboardButton("👋 Привет")
    button2 = types.KeyboardButton("Кто создал бота❓")
    button3 = types.KeyboardButton("📱Приложения")
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, text = "Привет, {0.first_name}! Я Стив.".format(message.from_user), reply_markup=markup)

@bot.callback_query_handler(func = lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data
    if data == '(':
        if value == '':
            value = '('
        elif '(' in value:
            data = ')'
            value += data
        else:
            data = '('
            value += data
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value) - 1]
    elif data == '=':
        try:
            value = str(distribution(value))
        except:
            value = 'Ошибка!'
    else:
        value += data

    if (value != old_value and value != '') or ('0' != old_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id = query.message.chat.id, message_id = query.message.message_id, text = '0', reply_markup = keyboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id = query.message.chat.id, message_id = query.message.message_id, text = value, reply_markup = keyboard)
    old_value = value

    old_value = value
    if value == 'Ошибка!': value = ''

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Привет"):
        bot.send_message(message.chat.id, text="Рад что ты зашёл!)")
    
    elif(message.text == "Кто создал бота❓"):
        bot.send_message(message.chat.id,'[Василий Малетин](t.me/maletin_vo)\n' + 'Здесь можно посмотреть его ' + '[GitHub](https://github.com/VasiliyMaletin)', parse_mode = 'Markdown')
    
    elif(message.text == "📱Приложения"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        button4 = types.KeyboardButton("🔢Калькулятор")
        button5 = types.KeyboardButton("❌⭕Крестики-нолики")
        back_to_menu = types.KeyboardButton("📋В главное меню")
        markup.add(button4, button5, back_to_menu)
        bot.send_message(message.chat.id, text="Выбери что тебя интересует", reply_markup = markup)

    elif(message.text == "🔢Калькулятор"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        back = types.KeyboardButton("🔙 Назад")
        back_to_menu = types.KeyboardButton("📋В главное меню")
        markup.add(back, back_to_menu)
        bot.send_message(message.chat.id, text = "Готов к работе", reply_markup = markup)
        if value == '':
            bot.send_message(message.chat.id, '0', reply_markup = keyboard)
        else:
            bot.send_message(message.chat.id, value, reply_markup = keyboard)

    elif(message.text == "❌⭕Крестики-нолики"):
        pass
    
    elif(message.text == "🔙 Назад"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        button4 = types.KeyboardButton("🔢Калькулятор")
        button5 = types.KeyboardButton("❌⭕Крестики-нолики")
        back_to_menu = types.KeyboardButton("📋В главное меню")
        markup.add(button4, button5, back_to_menu)
        bot.send_message(message.chat.id, text="Выбери что тебя интересует", reply_markup = markup)
        
    elif (message.text == "📋В главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Привет")
        button2 = types.KeyboardButton("Кто создал бота❓")
        button3 = types.KeyboardButton("📱Приложения")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Ты в главном меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Такой команды нет")

bot.polling(none_stop = True, interval = 0)
