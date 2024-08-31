Toggle navigation

Shared file: mmuzi's main.py
The code below has been shared by mmuzi. Want to see it run? Or fix some of mmuzi's bugs? Or introduce some of your own? Use the button above to copy it to your own account.

from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import random
import Text
import Calcbtn
import Video
import funcs
import test
import Nat
import lugat
import Tilbtn
import kvuz
import wikipedia
wikipedia.set_lang("uz")
#https://t.me/MATHtestchannel
channel = "@MATHtestchannel"
admin_id = "-1002099634180"
son1 = 0
son2 = 0
amal = ""
ildiz = 0
bot = TeleBot("7402806309:AAEcCoqOLztL3QYhC42PMgzC2oIwNBWA0HY")
def delete():
    deleteInline = InlineKeyboardMarkup()
    deleteInline.add(InlineKeyboardButton("✖️  Oʻchirirish" , callback_data="delete1"))
    return deleteInline
def tushundim():
    tush = InlineKeyboardMarkup()
    tush.add(InlineKeyboardButton("♻️ Tushundim ✅", callback_data="delete1"))
    return tush
def test10():
    test10_1 = InlineKeyboardMarkup(row_width=1)
    test10_1.add(InlineKeyboardButton("A) 502", callback_data="A10"), InlineKeyboardButton("B) 511", callback_data="B10"), InlineKeyboardButton("C) 521", callback_data="C10"))
    return test10_1
def test9():
    test9_1 = InlineKeyboardMarkup(row_width=1)
    test9_1.add(InlineKeyboardButton("A) 1766", callback_data="A9"), InlineKeyboardButton("B) 1966", callback_data="B9"), InlineKeyboardButton("C) 2266", callback_data="C9"))
    return test9_1
def test8():
    test8_1 = InlineKeyboardMarkup(row_width=1)
    test8_1.add(InlineKeyboardButton("A) 390", callback_data="A8"), InlineKeyboardButton("B) 400", callback_data="B8"), InlineKeyboardButton("C) 420", callback_data="C8"))
    return test8_1
def test7():
    test7_1 = InlineKeyboardMarkup(row_width=1)
    test7_1.add(InlineKeyboardButton("A) --211", callback_data="A7"), InlineKeyboardButton("B) --221", callback_data="B7"), InlineKeyboardButton("C) --231", callback_data="C7"))
    return test7_1
def test6():
    test6_1 = InlineKeyboardMarkup(row_width=1)
    test6_1.add(InlineKeyboardButton("A) 337", callback_data="A6"), InlineKeyboardButton("B) 347", callback_data="B6"), InlineKeyboardButton("C) 357", callback_data="C6"))
    return test6_1
def test5():
    test5_1 = InlineKeyboardMarkup(row_width=1)
    test5_1.add(InlineKeyboardButton("A) 9", callback_data="A5"), InlineKeyboardButton("B) 11", callback_data="B5"), InlineKeyboardButton("C) 12", callback_data="C5"))
    return test5_1
def test4():
    test4_1 = InlineKeyboardMarkup(row_width=1)
    test4_1.add(InlineKeyboardButton("A) 48,5", callback_data="A4"), InlineKeyboardButton("B) 49,5", callback_data="B4"), InlineKeyboardButton("C) 50,5", callback_data="C4"))
    return test4_1
def test3():
    test14 = InlineKeyboardMarkup(row_width=1)
    test14.add(InlineKeyboardButton("A) 62,5", callback_data="A3"), InlineKeyboardButton("B) 63,5", callback_data="B3"), InlineKeyboardButton("C) 64,5", callback_data="C3"))
    return test14
def test2():
    test11 = InlineKeyboardMarkup(row_width=1)
    test11.add(InlineKeyboardButton("A) 203", callback_data="A2"), InlineKeyboardButton("B) 213", callback_data="B2"), InlineKeyboardButton("C) 233", callback_data="C2"))
    return test11
def test1():
    test13 = InlineKeyboardMarkup(row_width=1)
    test13.add(InlineKeyboardButton("A) 1567", callback_data="A1"), InlineKeyboardButton("B) 1667", callback_data="B1"), InlineKeyboardButton("C) 1777", callback_data="C1"))
    return test13
def test12():
    btnm = InlineKeyboardMarkup()
    btnm.add(InlineKeyboardButton("Testni boshlash", callback_data="text"))
    return btnm
def true():
    ta = ReplyKeyboardMarkup()
    ta.add(KeyboardButton("Ma'umotlar toʻgʻri 100%"), KeyboardButton("📊 Testda qatnashish"))
    return ta
def error():
    e = InlineKeyboardMarkup()
    e.add(InlineKeyboardButton("-Orqaga" , callback_data="back"))
    return e
def obuna():
    m = InlineKeyboardMarkup(row_width=1)
    n1 = InlineKeyboardButton("Obuna boʻlish ✅", url="https://t.me/MATHtestchannel")
    n2 = InlineKeyboardButton("Obuna boʻldim ✅", callback_data='obuna')
    m.add(n1, n2)
    return m
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
    markup.add(KeyboardButton("📊 Testda qatnashish"))
    markup.add(KeyboardButton("📼 Video darslar"))
    return markup
@bot.message_handler(content_types=['video'])
def video(m):
    bot.send_message(m.chat.id, m.video.file_id)
@bot.message_handler(content_types=['photo'])
def photo(m):
    bot.delete_message(m.chat.id, m.message_id)
    bot.send_message(m.chat.id, m.photo[0].file_id)
@bot.message_handler(commands=['search', 'wiki', 'поиск'])
def search(m):
    if m.from_user.language_code == "uz":
        bot.delete_message(m.chat.id, m.message_id)
        bot.send_message(m.chat.id, "🔎", reply_markup=kvuz.kv1())
    elif m.from_user.language_code == "ru":
        bot.delete_message(m.chat.id, m.message_id)
        bot.send_message(m.chat.id, "🔎")
        bot.send_message(m.chat.id, "Введите условия поиска!")
        bot.register_next_step_handler(m, get_search)
@bot.message_handler(commands=['start'])
def start(m):
    Nat.adduser(m.from_user.id)
    funcs.adduser(m.from_user.id)
    b = bot.get_chat_member(channel, m.from_user.id).status
    if m.from_user.language_code == "uz":
        if b != "left":
            if test.getb(m.from_user.id) == "1":
                bot.send_message(m.chat.id, f"<i>Assalomu Alaykum!</i>\n<u><b>{test.familiya(m.from_user.id)} {test.ism(m.from_user.id)}!</b>\n\n<i>Bugun nimani oʻrganishni xohlaysiz! ✅</i></u> ", reply_markup=k1(), parse_mode='html')
            else:
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, f"Assalomu Alaykum {m.from_user.first_name}\n\nmen MATEMATIKA FANIDAN TESTLAR kanalining rasmiy botiman!", reply_markup=k1())
                bot.send_message(admin_id, f"Botga {m.from_user.first_name} /start buyrugʻini yubordi.\n\nIsmi:  {m.from_user.first_name}\n\nUsername:  @{m.from_user.username}\n\nID:  {m.from_user.id}")
        else:
            bot.delete_message(m.chat.id, m.message_id)
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())
    elif m.from_user.language_code == "ru":
        funcs.adduser(m.from_user.id)
        bot.delete_message(m.chat.id, m.message_id)
        bot.send_message(m.chat.id, f"Привет {m.from_user.first_name}\n\nЯ официальный бот канала MATEMATIKADAN TESTLAR!", reply_markup=Tilbtn.ru())
@bot.message_handler(content_types=['text'])
def get_text(m):
    channeltest = bot.get_chat_member(channel, m.from_user.id).status
    if m.from_user.language_code == "uz":
        if channeltest != "left":
            if m.text == 'Kalkulyator':
                funcs.toza(m.from_user.id)
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Kalkulyatorga xush kelibsiz!\nIltimos sonni kiriting", reply_markup=Calcbtn.calcb())
            elif m.text == "Chiqish ↩️ va tugatish ✔️":
                try:
                    bot.delete_message(m.chat.id, m.message_id)
                    bot.delete_message(m.chat.id, m.message_id - 1)
                    bot.send_message(m.chat.id, f"{Nat.natol(m.from_user.id)}", reply_markup=Nat.yangi())
                    bot.send_message(m.chat.id, f"Jami savollar soni: 10 ta\n✅ Toʻgʻri javoblar soni: {Nat.h(m.from_user.id)} ta")
                    Nat.delete(m.from_user.id)
                except:
                    bot.delete_message(m.chat.id, m.message_id)
                    bot.send_message(m.chat.id, Nat.natol(m.from_user.id), reply_markup=Nat.yangi())
            elif m.text == "📼 Video darslar":
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Oʻzingizga kerakli boʻlimni tanlang!" , reply_markup=Video.menu())
            elif m.text == "Asosiy sahifa ♻️":
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_photo(m.chat.id, "AgACAgIAAxkBAAIyoma_KaX2QQqmipHzYzxENl2OOHl8AAKI3DEbAi35SVl4Lc0KppayAQADAgADcwADNQQ", f"<i><b>Salom! <u>{test.familiya(m.from_user.id)} {test.ism(m.from_user.id)}</u></b>\n\nTayyor boʻlsangiz quyidagi tugmani bosing!👇</i>", reply_markup=test12(), parse_mode="html")
            elif m.text == "Ma'umotlar toʻgʻri 100%":
                test.editb(m.from_user.id, 1)
                bot.delete_message(m.chat.id, m.message_id)
                bot.delete_message(m.chat.id, m.message_id - 1)
                bot.send_photo(m.chat.id, "AgACAgIAAxkBAAIXSWaspaVrVUD18yKuDiar-pWONgLKAAIi3jEbzBVoSYtUEULV8z14AQADAgADcwADNQQ", "Tayyor boʻlsngiz qiyidagi tugmani bosing! 👇", reply_markup=test12())
            elif m.text == "📊 Testda qatnashish":
                f = test.getb(m.from_user.id)
                if f == "1":
                    bot.send_photo(m.chat.id, "AgACAgIAAxkBAAI-LWbEiAtZ5wcT2j6vdxAsoLIBC9LyAAL_4DEbCXIgSsGVoZSC9z76AQADAgADcwADNQQ", f"<b><i>Salom!</i> <u>{test.familiya(m.from_user.id)} {test.ism(m.from_user.id)}</u></b> \n\n<i>Tayyor boʻlsangiz quyidagi tugmani bosing!👇</i>", reply_markup=test12(), parse_mode="html")
                else:
                    test.adduser(m.from_user.id)
                    bot.delete_message(m.chat.id, m.message_id)
                    bot.send_message(m.chat.id, "👋")
                    bot.send_message(m.chat.id, "👋\nKeling testni boshlashdan oldin siz bilan tanishib olamiz! ✅")
                    bot.send_message(m.chat.id, "Iltimos ismingizni kiriting!")
                    bot.register_next_step_handler(m, get_name)
            elif m.text == 'Tasodifiy raqam':
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Tasodifiy raqam tanlandi : " + str(random.randint(1, 100)) + " ✅", reply_markup=delete())
            elif m.text == 'Ildiz':
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Sonni kiriting")
                bot.register_next_step_handler(m, get_Ildiz)
            elif m.text == 'Kvadrat²':
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Sonni kiriting")
                bot.register_next_step_handler(m, get_kv)
            elif m.text == 'Kub³':
                bot.delete_message(m.chat.id, m.message_id)
                bot.send_message(m.chat.id, "Sonni kiriting")
                bot.register_next_step_handler(m, get_kub)
            else:
                bot.send_message(m.chat.id, "❌ Noma'lum buyruq!\n\nSiz to'g'ridan-to'g'ri bot chatiga xabar yubordingiz, yoki\nbot tuzilishi yaratuvchisi tomonidan o'zgartirilgan boʻlishi mumkin.\n\nℹ️ Xabarlarni to'g'ridan-to'g'ri botga yubormang yoki\n/start orqali bot menyusini yangilang")
        else:
            bot.delete_message(m.chat.id, m.message_id)
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())
    elif m.from_user.language_code == "ru":
        if m.text == "Калькулятор":
            bot.delete_message(m.chat.id, m.message_id)
            bot.send_message(m.chat.id, "Добро пожаловать в калькулятор!\nПожалуйста, введите номер", reply_markup=Calcbtn.calcb())
        elif m.text == "Случайное число":
            bot.delete_message(m.chat.id, m.message_id)
            bot.send_message(m.chat.id, f"Было выбрано случайное число: {str(random.randint(1, 100))} ✅", reply_markup=Tilbtn.rudel())
        else:
            bot.send_message(m.chat.id, "❌ Неизвестная команда!\n\nВы отправили сообщение прямо в чат бота, или\nСтруктура бота могла быть изменена создателем.\n\nℹ️ Не отправляйте сообщения напрямую боту или\nОбновите меню бота через /start")
def get_search(m):
    channeltest1 = bot.get_chat_member(channel, m.from_user.id).status
    if m.from_user.language_code == "uz":
        if channeltest1 != "left":
            if m.text == "seks" or m.text == "Seks" or m.text == "am" or m.text == "Am" or m.text == "qoʻtoq":
                bot.send_message(m.chat.id, "Siz uyatsiz soʻz yubordingiz!!!❌")
            else:
                try:
                    bot.delete_message(m.chat.id, m.message_id)
                    bot.delete_message(m.chat.id, m.message_id - 1)
                    bot.delete_message(m.chat.id, m.message_id - 2)
                    bot.send_message(m.chat.id, f"<u><b>{wikipedia.summary(m.text)}</b></u>", reply_markup=delete(), parse_mode="html")
                    bot.send_message(admin_id, f"Wikipedia 🔎 \nFoydalanuvchi: {m.from_user.first_name}\nXabari: {m.text}\nOlgan javobi: {wikipedia.summary(m.text)}\nID: {m.from_user.id}", reply_markup=Text.btn())
                except:
                    try:
                        bot.send_message(m.chat.id, lugat.pydev[(m.text).lower()].title())
                    except:
                        bot.send_message(m.chat.id, "<u><b>Men ma'lumot izlayotgan saytda siz qidirgan ma'lumot yoʻq tushunarli boʻldimi?</b></u>", reply_markup=tushundim(), parse_mode="html")
        else:
            bot.send_message(m.chat.id, "Kanallarga obuna boʻling!", reply_markup=obuna())
    elif m.from_user.language_code == "ru":
        try:
            bot.delete_message(m.chat.id, m.message_id)
            bot.delete_message(m.chat.id, m.message_id - 1)
            bot.delete_message(m.chat.id, m.message_id - 2)
            wikipedia.set_lang('ru')
            bot.send_message(m.chat.id, wikipedia.summary(m.text), reply_markup=Tilbtn.rudel())
        except:
            bot.send_message(m.chat.id, "У меня нет информации,\nкоторый вы ищете!", reply_markup=Tilbtn.tu())
def get_Ildiz(m):
    global ildiz
    ildiz = m.text
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(m.chat.id, f"Javob: {int(ildiz) ** 0.5}", reply_markup=k1())
def get_kv(m):
    global ildiz
    ildiz = m.text
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(m.chat.id, f"Javob: {int(ildiz) ** 2}", reply_markup=k1())
def get_kub(m):
    global ildiz
    ildiz = m.text
    bot.delete_message(m.chat.id, m.message_id)
    bot.delete_message(m.chat.id, m.message_id - 1)
    bot.send_message(m.chat.id, f"Javob: {int(ildiz) ** 3}", reply_markup=k1())
@bot.callback_query_handler(func=lambda call: True)
def call(call):
    test = bot.get_chat_member(channel, call.from_user.id).status
    if call.from_user.language_code == "uz":
        if test != "left":
            if call.data == "obuna":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id, f"Assalomu Alaykum {call.from_user.first_name}\n\nmen MATEMATIKA FANIDAN TESTLAR kanalining rasmiy botiman ", reply_markup=k1())
            elif call.data == "enter":
                try:
                    d = wikipedia.search(funcs.getmatn(call.from_user.id))
                    m = ""
                    for l in d:
                        m += f"{l}\n\n"
                    bot.send_message(call.message.chat.id, wikipedia.summary(funcs.getmatn(call.from_user.id)), reply_markup=delete())
                    bot.send_message(call.message.chat.id, f"Balki xato qilgandirsiz!!! 👇\n\n{m}", reply_markup=kvuz.kv())
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    funcs.del1(call.from_user.id)
                except:
                    try:
                        bot.send_message(call.message.chat.id, lugat.pydev[(funcs.getmatn(call.from_user.id).lower())], reply_markup=kvuz.kv())
                        funcs.del1(call.from_user.id)
                        bot.delete_message(call.message.chat.id, call.message.message_id)
                    except:
                        bot.answer_callback_query(callback_query_id=call.id, text="❌ Topa olmadim! ✏️", show_alert=True)
                        funcs.del1(call.from_user.id)
            elif call.data == "del":
                try:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔎\n\n|", reply_markup=kvuz.kv())
                    funcs.del1(call.from_user.id)
                except:
                    bot.answer_callback_query(callback_query_id=call.id, text="Allaqachon tozalangan! ✅", show_alert=True)
            elif call.data == "toza":
                try:
                    funcs.toza(call.from_user.id)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Kalkulyator tarixi tozalandi hisoblashda davom etishingiz mumkin!...", reply_markup=Calcbtn.calcb())
                except:
                    bot.answer_callback_query(callback_query_id=call.id, text="Juda koʻp urunishlar ❌\nMa'lumotlar tozalangan!\nRaqamlar hustiga bosib hisoblashda davom etishingiz mumkin. Hammasi 0 dan boshlanadi✅", show_alert=True)
            def wiki(m):
                try:
                    funcs.addwiki(call.from_user.id, m)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"🔎\n\n{funcs.getmatn(call.from_user.id)}|", reply_markup=kvuz.kv1())
                except:
                    bot.answer_callback_query(callback_query_id=call.id, text="❌ Xatolik\nJuda koʻp tugmani bosib yubordingiz!", show_alert=True)
            if call.data == "a":
                wiki("a")
            elif call.data == "q":
                wiki("q")
            elif call.data =="w":
                wiki("w")
            elif call.data =="e":
                wiki("e")
            elif call.data =="r":
                wiki("r")
            elif call.data =="t":
                wiki("t")
            elif call.data =="y":
                wiki("y")
            elif call.data =="u":
                wiki("u")
            elif call.data =="i":
                 wiki("i")
            elif call.data =="o":
                wiki("o")
            elif call.data =="p":
                wiki("p")
            elif call.data =="o1":
                wiki("oʻ")
            elif call.data =="s":
                wiki("s")
            elif call.data =="d":
                wiki("d")
            elif call.data =="f":
                wiki("f")
            elif call.data =="g":
                wiki("g")
            elif call.data == "h":
                wiki("h")
            elif call.data =="j":
                wiki("j")
            elif call.data =="k":
                wiki("k")
            elif call.data =="l":
                wiki("l")
            elif call.data =="g1":
                wiki("gʻ")
            elif call.data =="tutuq":
                wiki("ʼ")
            elif call.data =="z":
                wiki("z")
            elif call.data =="x":
                wiki("x")
            elif call.data =="c":
                wiki("c")
            elif call.data =="v":
                wiki("v")
            elif call.data =="b":
                wiki("b")
            elif call.data =="n":
                wiki("n")
            elif call.data =="m":
                wiki("m")
            elif call.data ==",":
                wiki(",")
            elif call.data =="pro":
                wiki(" ")
            elif call.data ==".":
                funcs.addwiki(call.from_user.id, ". ")
                bot.edit_messa
