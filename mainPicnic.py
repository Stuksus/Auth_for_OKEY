import telebot
import re
token = ""
bot = telebot.TeleBot(token)
bot.send_message(248785589,'[hello]')
@bot.message_handler(content_types=["text"])
def handel_text(message):

    keyboard = telebot.InlineKeyboardMarkup()
    url_button = telebot.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)
    print('Сообщение удалено')

