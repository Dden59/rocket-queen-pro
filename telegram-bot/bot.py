import os
import telebot
from telebot.types import WebAppInfo
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('7921478924:AAEveJLy-VD0JXC---Aq-Bj9kqOOCqJy8X0'))

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = telebot.types.KeyboardButton(
        text="🚀 Открыть Rocket Queen Pro",
        web_app=WebAppInfo(url="https://dden59.github.io/rocket-queen-pro/")
    )
    markup.add(btn)
    
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в *Rocket Queen Pro*!\n\n"
        "Нажмите кнопку ниже для запуска помощника",
        reply_markup=markup,
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    bot.polling()
