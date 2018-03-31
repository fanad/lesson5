import telebot
token  = '591382130:AAFliKpJ0tRuESg0nVm9fVR04UjuQBHkkIk'

personInfo = {'виктор':'+777777777',
              'искандер':'+788888888'}
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def check_message(message):   
    if message.text in personInfo:
        bot.send_message(message.chat.id, personInfo[message.text])
    else:
        bot.send_message(message.chat.id, ("Такого имени нет"))

bot.polling(none_stop=True)
