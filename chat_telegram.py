import telebot
import random

from chat_smart import get_answer

token = '7584894804:AAEB80w-_kBopjbvnuL8BSUm5ml7UtlFJGs'
bot = telebot.TeleBot(token)

data = {'привет': ['здравствуй!', 'привет'], 'как дела?': ['хорошо', 'нормально'], 'в чем смысл жизни?': [42]}

@bot.message_handler(commands=['start'])
def weather(message):
    print(message)
    bot.reply_to(message, 'Привет! Я бот - чат. Пиши текст, и я отвечу.')


@bot.message_handler(func=lambda message: True)
def get_task(message):
    text = message.text
    ans = get_answer(text)
    bot.reply_to(message, ans)

bot.infinity_polling()

