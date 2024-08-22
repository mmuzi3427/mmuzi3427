from telebot import TeleBot, types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import random
#https://t.me/MATHtestchannel
channel = "@MATHtestchannel"


son1 = 0
son2 = 0
amal = ""
ildiz = 0

bot = TeleBot('7405501253:AAE2imBmE61Z2CJMonymeHa2f2QoK-IideQ')

def obuna():
    m = InlineKeyboardMarkup(row_width=1)
    n1 = InlineKeyboardButton("Obuna boʻlish ✅", url="https://t.me/MATHtestchannel")
    n2 = InlineKeyboardButton("Obuna boʻldim ✅", callback_data='obuna')
    m.add(n1, n2)
    return m

def btns():
    button = types.InlineKeyboardMarkup()
    button.add(types.InlineKeyboardButton("Obuna bolish", url="https://t.me/MATHtestchannel"))
    button.add(types.InlineKeyboardButton("Tekshirish ✅", callback_data="tekshirish"))
    return button

def ishora():
    i = ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = KeyboardButton("Qoʻshish")
    b2 = KeyboardButton("Ayrish")
    b3 = KeyboardButton("Koʻpaytirish")
    b4 = KeyboardButton("Boʻlish")
    i.add(b1, b2)
    i.add(b3, b4)
    return i
    
def k1():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Kalkulyator'), KeyboardButton("Ildiz"))
    markup.add(KeyboardButton("Kvadrat²"), KeyboardButton("Kub³"))
    markup.add(KeyboardButton("Tasodifiy raqam"))
    return markup

@bot.message_handler(commands=['start'])
def start(m):
    b = bot.get_chat_member(channel, m.from_user.id).status
    if b != "left":
        bot.delete_message(m.chat.id, m.message_id)
        bot.send_message(m.chat.id, "Assalomu Alaykum men kalkulyator botman", reply_markup=k1())
    else:
        bot.delete_message(m.chat.id, m.message_id)
        bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())

@bot.message_handler(content_types=['text'])
def get_text(m):
    if m.text == 'Kalkulyator':
        channeltest = bot.get_chat_member(channel, m.from_user.id).status
        if channeltest != "left":
            bot.send_message(m.chat.id, "Sonni kiriting")
            bot.register_next_step_handler(m, get_son1)
        else:
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())
    elif m.text == 'Tasodifiy raqam':
        channeltest = bot.get_chat_member(channel, m.from_user.id).status
        if channeltest != "left":
            bot.send_message(m.chat.id, "Tasodifiy raqam tanlandi : " + str(random.randint(1, 100)) + " ✅")
        else:
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())
    elif m.text == 'Ildiz':
        channeltest = bot.get_chat_member(channel, m.from_user.id).status
        if channeltest != "left":
            bot.send_message(m.chat.id, "Sonni kiriting")
            bot.register_next_step_handler(m, get_Ildiz)
        else:
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())
    elif m.text == 'Kvadrat²':
        channeltest = bot.get_chat_member(channel, m.from_user.id).status
        if channeltest != "left":
            bot.send_message(m.chat.id, "Sonni kiriting")
            bot.register_next_step_handler(m, get_kv)
        else:
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())
    elif m.text == 'Kub³':
        channeltest = bot.get_chat_member(channel, m.from_user.id).status
        if channeltest != "left":
            bot.send_message(m.chat.id, "Sonni kiriting")
            bot.register_next_step_handler(m, get_kub)
        else:
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())



def get_son1(m):
    global son1
    son1 = m.text
    bot.send_message(m.chat.id, "Ishorani tanlang", reply_markup=ishora())
    bot.register_next_step_handler(m, get_amal)

def get_amal(m):
    global amal
    amal = m.text
    bot.send_message(m.chat.id, "Ikkinchi sonni kiriting")
    bot.register_next_step_handler(m, get_son2)


def get_son2(m):
    global son2
    son2 = m.text
    if amal == "Qoʻshish":
        channeltest = bot.get_chat_member(channel, m.from_user.id).status
        if channeltest != "left":
            bot.send_message(m.chat.id, f"Javob: {int(son1) + int(son2)}", reply_markup=k1())
    elif amal == "Ayrish":
        channeltest = bot.get_chat_member(channel, m.from_user.id).status
        if channeltest != "left":
            bot.send_message(m.chat.id, f"Javob: {int(son1) - int(son2)}", reply_markup=k1())
        else:
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())
    elif amal == "Koʻpaytirish":
        channeltest = bot.get_chat_member(channel, m.from_user.id).status
        if channeltest != "left":
            bot.send_message(m.chat.id, f"Javob: {int(son1) * int(son2)}")
        else:
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())
    elif amal == "Boʻlish":
        if son2 > "0" or son2 < "0":
            channeltest = bot.get_chat_member(channel, m.from_user.id).status
            if channeltest != "left":
                bot.send_message(m.chat.id, f"Javob: {int(son1) / int(son2)}", reply_markup=k1())
            else:
                bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())
        elif son2 == "0":
             bot.send_message(m.chat.id, "Boʻlish imkonsiz", reply_markup=k1())
    else:
        channeltest = bot.get_chat_member(channel, m.from_user.id).status
        if channeltest != "left":
            bot.send_message(m.chat.id, "Amal notoʻgʻri", reply_markup=k1())
        else:
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())

def get_Ildiz(m):
    global ildiz
    ildiz = m.text
    bot.send_message(m.chat.id, f"Javob: {int(ildiz) ** 0.5}", reply_markup=k1())

def get_kv(m):
    global ildiz
    ildiz = m.text
    bot.send_message(m.chat.id, f"Javob: {int(ildiz) ** 2}", reply_markup=k1())
def get_kub(m):
    global ildiz
    ildiz = m.text
    bot.send_message(m.chat.id, f"Javob: {int(ildiz) ** 3}", reply_markup=k1())
    
@bot.callback_query_handler(func=lambda call: True)
def call(call):
    if call.data == "obuna":
        test = bot.get_chat_member(channel, call.from_user.id).status
        if test != "left":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, "Assalomu Alaykum men kalkulyator botman", reply_markup=k1())
        else:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())

bot.polling()
