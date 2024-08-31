from telebot import TeleBot, types
token = 'YOUR_TOKEN'
admin_id = 'admin_id'
bot = TeleBot(token)

@bot.message_handler(commands=['start'])
def start(msg):
  bot.delete_message(msg.chat.id, msg.message_id)
  bot.send_message(msg.chat.id, 'Salom men echo botman')

@bot.message_handler(content_types=['text'])
def echo(msg):
  bot.reply_to(msg, msg.text)
  bot.send_message(admin_id, msg.text)
  
@bot.message_handler(content_types=['photo'])
def photo(msg):
  bot.send_photo(msg.chat.id, msg.photo[0].file_id)
  bot.send_photo(admin_id, msg.photo[0].file_id)

@bot.message_handler(content_types=['sticker'])
def stickers(msg):
    bot.send_sticker(msg.chat.id, msg.sticker.file_id)
    bot.send_sticker(admin_id, msg.sticker.file_id)

@bot.message_handler(content_types=['video'])
def video(msg):
    bot.send_video(msg.chat.id, msg.video.file_id)
    bot.send_video(admin_id, msg.video.file_id) 

@bot.message_handler(content_types=['audio'])
def audio(msg):
    bot.send_audio(msg.chat.id, msg.audio.file_id)
    bot.send_audio(admin_id, msg.audio.file_id)

bot.polling(none_stop=True)
