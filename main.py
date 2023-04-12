from telebot import types
import random
import telebot

token = "5203676470:AAGzhTvM6HSlQ5nawQg3gEForS-nAimNs2M"

bot = telebot.TeleBot(token)
#pool = ["зз это херня", "поеб#мя?", "на мне черный трешер", "луна сегодня красивая", "баю бай мой калашников"]
#pool_fire = [
    #"Ты испытывала когда-нибудь чувство, что у тебя внутри мотор, который постоянно заставляет тебя действовать, мешает остановиться? Примерно так ощущают себя огненные знаки 25/8"]
#poll_wind = [
   # "Интересно, какую личность они откроют перед вами. Может даже несколько, а может у них появится какая-то новая"]
#pool_dirt = [
    #"Склонность занижать свои способности, чем превозносить их, достаточная осторожность и недоверчивость - проверка практически любой поступившей к ним информации. Усваивая принципы морали и нравственности с самого раннего детства, они следуют им всю жизнь."]
#pool_water = ["..."]

pool_oven = ["Помните, в новой компании, где никто друг-друга не знает, они будут первыми, которые со всеми познакомятся", "Если если есть желание с кем-то поспорить, можешь поспорить с овном. Закончишь примерно через год и так и не переспоришь",
             "Имеют специфическое чувство юмора и иногда смеются над своими же шутками", "Вечный двигатель на энергии адового бомбежа"]
pool_strelec = ["Если стрельцам рассказать секрет, они будут до конца жизни его хранить, однако в этом и траблы - они просто не расскажут тебе какой пздц они пережили", "Двойная жизнь свойственна для мужчин стрельцов"]
pool_lev = ["Лучше всех справятся с одиночеством", "Хорошие сммщики", "Лучшие мужчины - это львы. Это факт"]
pool_rak = ["Мужчины раки инфантильны"]
pool_ribi = ["Если ты что-то чувствуешь и тебе плохо - помни, есть рыбы ♀, которые переносят все это в 10 раз сильнее", "А не снести ли нам все соц сети, закрыться в себе и лечь спать?", "Не, ну вспомни хотя бы одного мужчину рыбы, который не запомнился тебе своим внешним видом",
             "Женщины рыбы с юпитера, их невозможно понять"]
pool_scorp = ["Лучшие психологи, которе не могут разобраться в собственных проблемах", "бухают знатно"]
pool_bliznets = ["Веселость, задорность, движы, а не стоп - надо поплакать", "Близнецы женщины очень крутые, и эмоциональные, но у них слишком много личностей в голове (",
                 "Самый открытый и веселый зз сто проц", "Терпеть его способен только овен", "Подруга-близнец ни во что не верит, говорит, что зз фигня, а потом присылает мне гороскопы на день"]
pool_vesi = ["Идеально спланировать продуктивный день, даже проснуться и выполнить все, но не ждите, что это повториться через день - мб через год", "Весы как близнецы, только взяли у них самое худшее"]
pool_vodolei = ["Игнорировать людей, которых любишь - збс", "Водолеи соглашаются на любую авантюру и всякий пиздец, если это будет весело", "У водолеев много друзей, но они боятся сближаться с кем-то"]
pool_telec = ["Стабильность и еще раз стабильность, а также бесконечный трудоголизм", "Не, ну знать про всех все, а также чуть-чуть пустить сплетни - обязательная процедура"]
pool_deva = ["Абсолютно все девы женщины не умеют бухать", "Как же круто у дев получается шутить с определенной харизмой", "Мужчин дев придумали для того, чтобы женщины страдали", "Августовские и сентябрьские девы не ладят."]
pool_cozerog = ["За словесным базаром следят, как и за деньгами", "Родились в январе, поэтому, чтобы их лед тронул надо купить на всю зарплату керосина, как пел хаски"]
pool_last_spletnya = {
            'Августовские и сентябрьские девы не ладят.': '1',
            'И жнец, и чтец, и на дуде игрец - Близнец': '2',
            'Бухают знатно - Скорпион': '3',
            'Если если есть желание с кем-то поспорить, можешь поспорить с овном. Закончишь примерно через год и так и не переспоришь': '4',
        }

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None


@bot.message_handler(commands=['start', 'button'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "Самый серьзный бот про знаки зодиака. Информация, предостовляемая им не является на 100% достоверной, "
                     "но поможет начинающим парочкам выстроить гармоничные отношения, а друзьям укрепить узы 🙄 ")
    bot.send_message(message.chat.id, "Разработку ведет @Wiharo, все претензии и что он мудак к нему")
    bot.send_message(message.chat.id, "Бот только запустился, инфы мыло, обновление сплетен по вечерам")
    bot.send_message(message.chat.id, "Выбирай стихию знака, а дальше поймешь")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Огонь 🔥")
    markup.add(item1)
    item2 = types.KeyboardButton("Вода 💧")
    markup.add(item2)
    item3 = types.KeyboardButton("Воздух 🌪")
    markup.add(item3)
    item4 = types.KeyboardButton("Земля ⛰")
    markup.add(item4)
    item4 = types.KeyboardButton("Последние сплетни")
    markup.add(item4)
    bot.send_message(message.chat.id, 'Выбирай уже давай 😴', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if 'Огонь 🔥' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton("Овен ♈")
        item6 = types.KeyboardButton("Стрелец ♐")
        item7 = types.KeyboardButton("Лев ♌")
        item8 = types.KeyboardButton("Назад ⬅")
        markup.add(item5, item6, item7, item8)
        bot.send_message(message.chat.id, "Выбирай зз", reply_markup=markup)
    elif 'Последние сплетни' in message.text:
        for spletnya in pool_last_spletnya:
            bot.send_message(message.chat.id, spletnya)
    elif 'Овен ♈' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Еще про овнов 😶")
        markup.add(item1)
        item2 = types.KeyboardButton("Напишу сплетню, мнение насчет овнов 😏")
        markup.add(item2)
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        bot.send_message(message.chat.id, random.choice(pool_oven), reply_markup=markup)
    elif 'Напишу сплетню, мнение насчет овнов 😏' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(1148456593, "овен")
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        msg = bot.reply_to(message, "Пиши давай, это анонимно")
        bot.register_next_step_handler(msg, process_name_step)
    elif 'Напишу сплетню, мнение насчет стрельцов 😏' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(1148456593, "стрелец")
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        msg = bot.reply_to(message, "Пиши давай, это анонимно")
        bot.register_next_step_handler(msg, process_name_step)
    elif 'Напишу сплетню, мнение насчет львов 😏' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(1148456593, "лев")
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        msg = bot.reply_to(message, "Пиши давай, это анонимно")
        bot.register_next_step_handler(msg, process_name_step)
    elif 'Напишу сплетню, мнение насчет тельцов 😏' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(1148456593, "телец")
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        msg = bot.reply_to(message, "Пиши давай, это анонимно")
        bot.register_next_step_handler(msg, process_name_step)
    elif 'Напишу сплетню, мнение насчет козерогов 😏' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(1148456593, "козерог")
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        msg = bot.reply_to(message, "Пиши давай, это анонимно")
        bot.register_next_step_handler(msg, process_name_step)
    elif 'Напишу сплетню, мнение насчет дев 😏' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(1148456593, "дева")
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        msg = bot.reply_to(message, "Пиши давай, это анонимно")
        bot.register_next_step_handler(msg, process_name_step)
    elif 'Напишу сплетню, мнение насчет близнецов 😏' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(1148456593, "близнецы")
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        msg = bot.reply_to(message, "Пиши давай, это анонимно")
        bot.register_next_step_handler(msg, process_name_step)
    elif 'Напишу сплетню, мнение насчет водолеев 😏' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(1148456593, "водолей")
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        msg = bot.reply_to(message, "Пиши давай, это анонимно")
        bot.register_next_step_handler(msg, process_name_step)
    elif 'Напишу сплетню, мнение насчет весов 😏' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(1148456593, "весы")
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        msg = bot.reply_to(message, "Пиши давай, это анонимно")
        bot.register_next_step_handler(msg, process_name_step)
    elif 'Напишу сплетню, мнение насчет рыб 😏' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(1148456593, "рыбы")
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        msg = bot.reply_to(message, "Пиши давай, это анонимно")
        bot.register_next_step_handler(msg, process_name_step)
    elif 'Напишу сплетню, мнение насчет рака 😏' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(1148456593, "рак")
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        msg = bot.reply_to(message, "Пиши давай, это анонимно")
        bot.register_next_step_handler(msg, process_name_step)
    elif 'Напишу сплетню, мнение насчет скорпиона 😏' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(1148456593, "скорпион")
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        msg = bot.reply_to(message, "Пиши давай, это анонимно")
        bot.register_next_step_handler(msg, process_name_step)
    elif 'Стрелец ♐' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Еще про стрельцов 😶")
        markup.add(item1)
        item2 = types.KeyboardButton("Напишу сплетню, мнение насчет стрельцов 😏")
        markup.add(item2)
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        bot.send_message(message.chat.id, random.choice(pool_strelec), reply_markup=markup)
    elif 'Лев ♌' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Еще про львов 😶")
        markup.add(item1)
        item2 = types.KeyboardButton("Напишу сплетню, мнение насчет львов 😏")
        markup.add(item2)
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        bot.send_message(message.chat.id, random.choice(pool_lev), reply_markup=markup)
    elif 'Назад ⬅' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Огонь 🔥")
        markup.add(item1)
        item2 = types.KeyboardButton("Вода 💧")
        markup.add(item2)
        item3 = types.KeyboardButton("Воздух 🌪")
        markup.add(item3)
        item4 = types.KeyboardButton("Земля ⛰")
        markup.add(item4)
        item5 = types.KeyboardButton("Последние сплетни")
        markup.add(item5)
        bot.send_message(message.chat.id, 'Выбирай уже давай 😴', reply_markup=markup)
    elif 'Вода 💧' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton("Рыбы ♓")
        item6 = types.KeyboardButton("Рак ♋")
        item7 = types.KeyboardButton("Скорпион ♏")
        item8 = types.KeyboardButton("Назад ⬅")
        markup.add(item5, item6, item7, item8)
        bot.send_message(message.chat.id, "Выбирай зз", reply_markup=markup)
    elif 'Рак ♋' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Еще про рака 😶")
        markup.add(item1)
        item2 = types.KeyboardButton("Напишу сплетню, мнение насчет рака 😏")
        markup.add(item2)
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        bot.send_message(message.chat.id, random.choice(pool_rak), reply_markup=markup)
    elif 'Рыбы ♓' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Еще про рыб 😶")
        markup.add(item1)
        item2 = types.KeyboardButton("Напишу сплетню, мнение насчет рыб 😏")
        markup.add(item2)
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        bot.send_message(message.chat.id, random.choice(pool_ribi), reply_markup=markup)
    elif 'Скорпион ♏' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Еще про скорпионов 😶")
        markup.add(item1)
        item2 = types.KeyboardButton("Напишу сплетню, мнение насчет скорпиона 😏")
        markup.add(item2)
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        bot.send_message(message.chat.id, random.choice(pool_scorp), reply_markup=markup)
    elif 'Воздух 🌪' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton("Вододей ♒")
        item6 = types.KeyboardButton("Весы ♎")
        item7 = types.KeyboardButton("Близнецы ♊")
        item8 = types.KeyboardButton("Назад ⬅")
        markup.add(item5, item6, item7, item8)
        bot.send_message(message.chat.id, "Выбирай зз", reply_markup=markup)
    elif 'Вододей ♒' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Еще про водолеев 😶")
        markup.add(item1)
        item2 = types.KeyboardButton("Напишу сплетню, мнение насчет водолеев 😏")
        markup.add(item2)
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        bot.send_message(message.chat.id, random.choice(pool_vodolei), reply_markup=markup)
    elif 'Весы ♎' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Еще про весы 😶")
        markup.add(item1)
        item2 = types.KeyboardButton("Напишу сплетню, мнение насчет весов 😏")
        markup.add(item2)
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        bot.send_message(message.chat.id, random.choice(pool_vesi), reply_markup=markup)
    elif 'Близнецы ♊' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Еще про близнецов 😶")
        markup.add(item1)
        item2 = types.KeyboardButton("Напишу сплетню, мнение насчет близнецов 😏")
        markup.add(item2)
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        bot.send_message(message.chat.id, random.choice(pool_bliznets), reply_markup=markup)
    elif 'Земля ⛰' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item5 = types.KeyboardButton("Телец ♉")
        item6 = types.KeyboardButton("Козерог ♑")
        item7 = types.KeyboardButton("Дева ♍")
        item8 = types.KeyboardButton("Назад ⬅")
        markup.add(item5, item6, item7, item8)
        bot.send_message(message.chat.id, "Выбирай зз", reply_markup=markup)
    elif 'Телец ♉' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Еще про тельцов 😶")
        markup.add(item1)
        item2 = types.KeyboardButton("Напишу сплетню, мнение насчет тельцов 😏")
        markup.add(item2)
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        bot.send_message(message.chat.id, random.choice(pool_telec), reply_markup=markup)
    elif 'Козерог ♑' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Еще про козерогов 😶")
        markup.add(item1)
        item2 = types.KeyboardButton("Напишу сплетню, мнение насчет козерогов 😏")
        markup.add(item2)
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        bot.send_message(message.chat.id, random.choice(pool_cozerog), reply_markup=markup)
    elif 'Дева ♍' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Еще про дев 😶")
        markup.add(item1)
        item2 = types.KeyboardButton("Напишу сплетню, мнение насчет дев 😏")
        markup.add(item2)
        item3 = types.KeyboardButton("Назад ⬅")
        markup.add(item3)
        bot.send_message(message.chat.id, random.choice(pool_deva), reply_markup=markup)
    elif 'Еще про дев 😶' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, random.choice(pool_deva), reply_markup=markup)
    elif 'Еще про козерогов 😶' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, random.choice(pool_cozerog), reply_markup=markup)
    elif 'Еще про тельцов 😶' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, random.choice(pool_telec), reply_markup=markup)
    elif 'Еще про овнов 😶' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, random.choice(pool_oven), reply_markup=markup)
    elif 'Еще про стрельцов 😶' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, random.choice(pool_strelec), reply_markup=markup)
    elif 'Еще про львов 😶' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, random.choice(pool_lev), reply_markup=markup)
    elif 'Еще про рыб 😶' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, random.choice(pool_ribi), reply_markup=markup)
    elif 'Еще про рака 😶' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, random.choice(pool_rak), reply_markup=markup)
    elif 'Еще про скорпионов 😶' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, random.choice(pool_scorp), reply_markup=markup)
    elif 'Еще про весы 😶' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, random.choice(pool_vesi), reply_markup=markup)
    elif 'Еще про водолеев 😶' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, random.choice(pool_vodolei), reply_markup=markup)
    elif 'Еще про близнецов 😶' in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, random.choice(pool_bliznets), reply_markup=markup)



def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        bot.send_message(1148456593, ' ' + user.name)
    except Exception as e:
        bot.reply_to(message, 'упс, походу слишком много символов - давай разбей на два сообщения')





bot.infinity_polling()
