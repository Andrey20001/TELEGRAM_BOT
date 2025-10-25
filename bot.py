import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin


bot = telebot.TeleBot("СВОЙ ТОКЕН")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бешеная Змейка 3000!")


@bot.message_handler(commands=['Привет!'])
def send_hello(message):
    bot.send_message(message.chat.id, "Привет! Как дела?")


@bot.message_handler(commands=['Пока!'])
def send_bye(message):
    bot.send_message(message.chat.id, "Пока! Удачи!")

@bot.message_handler(commands=['password'])
def send_password(message):
    bot.reply_to(message, gen_pass(12))

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, "Вот эмоджи: " + emodji)

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, "Монетка выпала так: " + coin)




@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Ты тупой":
        bot.send_message(message.chat.id, "Сам тупой")
    else:
        bot.send_message(message.chat.id, "Чё надо?")


bot.polling()
