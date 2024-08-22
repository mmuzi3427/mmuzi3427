from telebot import TeleBot, types


bot = TeleBot('Token')
def markup1():
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = types.KeyboardButton("👋 Salom")
    markup1.add(b1)
    return markup1
  
def markup():
    map = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton("Sayt qoidalari")
    bt2 = types.KeyboardButton("Nashrni loyihalash bo'yicha maslahatlar")
    bt3 = types.KeyboardButton("Qanday qilib XABRda muallif bo'lish mumkin?")
    map.add(bt1)
    map.add(bt2)
    map.add(bt3)
    return map

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, "👋 Salom! Men sizning yordamchi botingizman!", reply_markup=markup1())

@bot.message_handler(content_types=['text'])
def text(msg):
    if msg.text == "👋 Salom":
        bot.send_message(msg.chat.id, "❓ Sizni qiziqtirgan savolni bering", reply_markup=markup())
    elif msg.text == "Sayt qoidalari":
        bot.send_message(msg.chat.id, "Ushbu [havola](https://habr.com/ru/docs/help/rules/) orqali sayt qoidalari bilan tanishishingiz mumkin!", parse_mode='Markdown')
    elif msg.text == "Nashrni loyihalash bo'yicha maslahatlar":
        bot.send_message(msg.chat.id, "Nashrlarni loyihalash bo'yicha maslahatlar haqida ko'proq [havola orqali o'qing.](https://habr.com/ru/docs/companies/design/)", parse_mode='Markdown')
    elif msg.text == "Qanday qilib XABRda muallif bo'lish mumkin?":
        bot.send_message(msg.chat.id, "Siz birinchi xabarni yozasiz, u moderatorlar tomonidan tekshiriladi va agar hamma narsa yaxshi bo'lsa, u asosiy Habr tasmasiga yuboriladi, u erda u ko'rishlar, sharhlar va reytinglarni oladi. Kelajakda oldindan moderatsiya endi kerak bo'lmaydi. Agar postda biror narsa noto'g'ri bo'lsa, uni tahrirlashingiz so'raladi.\n\nToʻliq matnni [havolada](https://habr.com/ru/sandbox/start/) oʻqishingiz mumkin", parse_mode='Markdown')
      

bot.polling()
