# 7082039182:AAEQEGrXjsYW70JBY7tsH1dyYwf68V765ng
import psutil
import time
import telebot

# Function to track the running time of an application
def get_process_time(process_name):
    for proc in psutil.process_iter(['name', 'create_time']):
        if proc.info['name'] == process_name:
            return time.time() - proc.info['create_time']
    return None



# Your Telegram Bot Token
bot = telebot.TeleBot('7082039182:AAEQEGrXjsYW70JBY7tsH1dyYwf68V765ng')

# Handling the start command
@bot.message_handler(commands=['start', 'restart'])
def start(message):
    chat_id = message.chat.id
    # Initial message
    bot.send_message(chat_id, "Hi there! Let's start monitoring some apps.")

    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    btn1 = telebot.types.KeyboardButton('Track')
   
    keyboard.row(btn1)
    bot.send_message(
        chat_id, "Here are the available options.\n What would you like to do?", reply_markup=keyboard)
    bot.register_next_step_handler(message, click)

def click(message):
    chat_id = message.chat.id
    if message.text == 'Track':
        list_of_apps_for_track(message)
    

def list_of_apps_for_track(message):
    chat_id = message.chat.id

    markup = telebot.types.InlineKeyboardMarkup()   # Keyboard for tracking buttons
    btn1 = telebot.types.InlineKeyboardButton(
        'VALORANT', callback_data='Valorant')
    btn2 = telebot.types.InlineKeyboardButton(
        'Telegram', callback_data='Telegram')
    btn3 = telebot.types.InlineKeyboardButton(
        'BIGFOOT', callback_data='BIGFOOT')
    btn4 = telebot.types.InlineKeyboardButton(
        'Discord', callback_data='Discord')





    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    bot.send_message(chat_id, 'Select an app to close', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):
    chat_id = callback.message.chat.id
    if callback.data == 'Valorant':  # Track Valorant
        process_name = "Valorant.exe"     # Process name
        uptime = get_process_time(process_name)
        if uptime is not None:
            bot.send_message(chat_id, f'The running time for Valorant is {int(uptime/60)} minutes and {int(uptime % 60)} seconds')
       
    if callback.data == 'Telegram':  # Track Telegram
        process_name = "Telegram.exe"     # Process name
        uptime = get_process_time(process_name)
        if uptime is not None:
            bot.send_message(chat_id, f'The running time for Telegram is {int(uptime/60)} minutes and {int(uptime % 60)} seconds')
       
    if callback.data == 'Discord':  # Track Discord
        process_name = "Discord.exe"     # Process name
        uptime = get_process_time(process_name)
        if uptime is not None:
            bot.send_message(chat_id, f'The running time for Discord is {int(uptime/60)} minutes and {int(uptime % 60)} seconds')
       
    if callback.data == 'BIGFOOT':  # Track BIGFOOT
        process_name = "BIGFOOT.exe"     # Process name
        uptime = get_process_time(process_name)
        if uptime is not None:
            bot.send_message(chat_id, f'The running time for Discord is {int(uptime/60)} minutes and {int(uptime % 60)} seconds')
      

# Starting the bot
bot.polling()
