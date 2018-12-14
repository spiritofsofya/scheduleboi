import telebot


access_token = '727633887:AAE9dpxtJ82ybMFmHOKu7CRpNk7i83CZVtM'
bot = telebot.TeleBot(access_token)
# создадим объект нашего бота


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
# запустим бесконечный цикл получения новых записей со стороны Telegram
