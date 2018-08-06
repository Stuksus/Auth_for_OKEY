import telebot
import re
token = "489178856:AAGZDAq_7tgeyAtfUokfvrp4yNu9XHB8JKg"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def handel_text(message):
    keyboard = telebot.InlineKeyboardMarkup()
    url_button = telebot.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)
    print('Сообщение удалено')

