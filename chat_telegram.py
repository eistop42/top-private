import telebot
import random

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
    if text in data.keys():
        ans = data.get(text)
        ans = random.choice(ans)
    else:
        ans = 'эмм'
    bot.reply_to(message, ans)

bot.infinity_polling()

