import telebot, os, requests, random
from bot_logic import gen_pass, gen_emodji, flip_coin


bot = telebot.TeleBot("СВОЙ ТОКЕН")

##################################################################
@bot.message_handler(commands=['mem'])
def send_mem(message):
    img = random.choice(os.listdir("images"))
    with open(f'images/{img}', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['animals'])
def send_mem_animals(message):
    img = random.choice(os.listdir("images_animals"))
    with open(f'images_animals/{img}', 'rb') as f:
        bot.send_photo(message.chat.id, f)


#КОМАНДА /duck
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.message_handler(commands=['duck'])
def duck(message):
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

##################################################################

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

####&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# Обработчик команды '/hi'
@bot.message_handler(commands=['hi'])
def send_hi(message):
    count_hi = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "Привет! " * count_hi)

# Обработчик команды '/e1'
@bot.message_handler(commands=['e1'])
def send_cross_e(message):
    cross = (message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "⊹⊹⊹")

# Обработчик команды '/e2'
@bot.message_handler(commands=['e2'])
def send_bu_e(message):
    bu = (message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "👻👻👻")


# Обработчик команды '/e3'
@bot.message_handler(commands=['e3'])
def send_hello_e(message):
    hello = (message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "👋👋👋")

####&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Ты тупой":
        bot.send_message(message.chat.id, "Сам тупой")
    else:
        bot.send_message(message.chat.id, "Чё надо?")


bot.polling()
