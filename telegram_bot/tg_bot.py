import telebot 
from telebot import types
from controller import distribution
from main import * 
import random 
from dotenv import load_dotenv, find_dotenv
import logging
import os

load_dotenv(find_dotenv())
bot = telebot.TeleBot(os.getenv("TOKEN"))

logger = telebot.logging
logger.basicConfig(filename = 'bot_log.log', level = logging.DEBUG,
                    format = ' %(asctime)s - %(levelname)s - %(message)s')

print('Online')

value = ''
old_value = '' 
keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(   telebot.types.InlineKeyboardButton('C', callback_data = 'calc:C'),
                telebot.types.InlineKeyboardButton('<=', callback_data = 'calc:<='),
                telebot.types.InlineKeyboardButton('( )', callback_data = 'calc:('),
                telebot.types.InlineKeyboardButton('/', callback_data = 'calc:/'))

keyboard.row(   telebot.types.InlineKeyboardButton('7', callback_data = 'calc:7'),
                telebot.types.InlineKeyboardButton('8', callback_data = 'calc:8'),
                telebot.types.InlineKeyboardButton('9', callback_data = 'calc:9'),
                telebot.types.InlineKeyboardButton('*', callback_data = 'calc:*'))

keyboard.row(   telebot.types.InlineKeyboardButton('4', callback_data = 'calc:4'),
                telebot.types.InlineKeyboardButton('5', callback_data = 'calc:5'),
                telebot.types.InlineKeyboardButton('6', callback_data = 'calc:6'),
                telebot.types.InlineKeyboardButton('-', callback_data = 'calc:-'))

keyboard.row(   telebot.types.InlineKeyboardButton('1', callback_data = 'calc:1'),
                telebot.types.InlineKeyboardButton('2', callback_data = 'calc:2'),
                telebot.types.InlineKeyboardButton('3', callback_data = 'calc:3'),
                telebot.types.InlineKeyboardButton('+', callback_data = 'calc:+'))

keyboard.row(   telebot.types.InlineKeyboardButton('j', callback_data = 'calc:j'),
                telebot.types.InlineKeyboardButton('0', callback_data = 'calc:0'),
                telebot.types.InlineKeyboardButton(',', callback_data = 'calc:,'),
                telebot.types.InlineKeyboardButton('=', callback_data = 'calc:='))

item = {}
gameIsStart = False
gameGround = [" ", " ", " ",
            " ", " ", " ",
            " ", " ", " ", ]
            
CrossesOrToe = ["⭕", "❌"]
playerSymbol = CrossesOrToe[random.randint(0, 1)]
botSymbol = ""

if (playerSymbol == "⭕"):
    botSymbol = "❌"
else:
    botSymbol = "⭕"

winbool = False
losebool = False

def clear():
    global gameGround
    gameGround = [" ", " ", " ",
                " ", " ", " ",
                " ", " ", " ", ]

def win(cell_1, cell_2, cell_3):
    if cell_1 == playerSymbol and cell_2 == playerSymbol and cell_3 == playerSymbol:
        global winbool
        winbool = True

def lose(cell_1, cell_2, cell_3):
    if cell_1 == botSymbol and cell_2 == botSymbol and cell_3 == botSymbol:
        global losebool
        losebool = True

def defend(cell_1, cell_2, posDef):
    if cell_1 == playerSymbol and cell_2 == playerSymbol:
        posDef = botSymbol

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    button1 = types.KeyboardButton("👋 Привет")
    button2 = types.KeyboardButton("Кто создал бота❓")
    button3 = types.KeyboardButton("📱Приложения")
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, text = "Привет, {0.first_name}! Я Стив.".format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    global keyboard_2, gameIsStart
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

    elif(message.text == "🔙 Назад"):
        gameIsStart = False
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        button4 = types.KeyboardButton("🔢Калькулятор")
        button5 = types.KeyboardButton("❌⭕Крестики-нолики")
        back_to_menu = types.KeyboardButton("📋В главное меню")
        markup.add(button4, button5, back_to_menu)
        bot.send_message(message.chat.id, text="Выбери что тебя интересует", reply_markup = markup)
        
    elif (message.text == "📋В главное меню"):
        gameIsStart = False
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Привет")
        button2 = types.KeyboardButton("Кто создал бота❓")
        button3 = types.KeyboardButton("📱Приложения")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Ты в главном меню", reply_markup=markup)
    
    elif(message.text == "❌⭕Крестики-нолики") or (message.text == "🔄 Ещё раз"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        back = types.KeyboardButton("🔙 Назад")
        button6 = types.KeyboardButton("🔄 Ещё раз")
        back_to_menu = types.KeyboardButton("📋В главное меню")
        markup.add(back, button6, back_to_menu)
        bot.send_message(message.chat.id, text = "Готов к игре 🤖", reply_markup = markup)
        clear()
        gameIsStart = True
    else:
        bot.send_message(message.chat.id, "Такой команды нет")
    
    # game
    if gameIsStart == True:
        item = {}
        keyboard_2 = types.InlineKeyboardMarkup(row_width=3)
        i = 0
        for i in range(9):
            item[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))

        keyboard_2.row(item[0], item[1], item[2])
        keyboard_2.row(item[3], item[4], item[5])
        keyboard_2.row(item[6], item[7], item[8])
        bot.send_message(message.chat.id, f"Ходи, играешь за {playerSymbol}", reply_markup=keyboard_2)

@bot.callback_query_handler(func=lambda call: call.data.split(":")[0] == "calc")
def callback_func(query):
    global value, old_value
    data = query.data.split(":")[1]
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

@bot.callback_query_handler(func=lambda call: True)
def callbackInline(call):
    if (call.message):
        
        # bot manager
        randomCell = random.randint(0, 8)
        if gameGround[randomCell] == playerSymbol:
            randomCell = random.randint(0, 8)
        if gameGround[randomCell] == botSymbol:
            randomCell = random.randint(0, 8)
        if gameGround[randomCell] == " ":
            gameGround[randomCell] = botSymbol
        
        # player manager
        for i in range(9):
            if call.data == str(i):
                if (gameGround[i] == " "):
                    gameGround[i] = playerSymbol
            
            # lose or win
            win(gameGround[0], gameGround[1], gameGround[2])
            win(gameGround[0], gameGround[4], gameGround[8])
            win(gameGround[6], gameGround[4], gameGround[2])
            win(gameGround[6], gameGround[7], gameGround[8])
            win(gameGround[0], gameGround[3], gameGround[6])
            lose(gameGround[0], gameGround[1], gameGround[2])
            lose(gameGround[0], gameGround[4], gameGround[8])
            lose(gameGround[6], gameGround[4], gameGround[2])
            lose(gameGround[6], gameGround[7], gameGround[8])
            lose(gameGround[0], gameGround[3], gameGround[6])
            item[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))
        
        # update cells
        global  keyboard_2
        keyboard_2.row(item[0], item[1], item[2])
        keyboard_2.row(item[3], item[4], item[5])
        keyboard_2.row(item[6], item[7], item[8])

        bot.send_message(call.message.chat.id, "Твой ход", reply_markup = keyboard_2)
        global winbool
        if winbool:
            clear()
            bot.send_message(call.message.chat.id, "Ты победил 🤖")
            winbool = False
            gameIsStart = False
        global losebool
        if losebool:
            clear()
            bot.send_message(call.message.chat.id, "Я победил 🤖")
            losebool = False
            gameIsStart = False

bot.polling(none_stop = True, interval = 0)
