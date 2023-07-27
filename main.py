import telebot
from telebot import types

token ="///TOKEN///"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Проходка🎫', callback_data='button1')
    button2 = types.InlineKeyboardButton('Донат💗', callback_data='button2')
    button3 = types.InlineKeyboardButton('Ссылки🌿', callback_data='button3')
    markup.add(button1)
    markup.add(button2, button3)
    photo = open('home.png', 'rb')
    bot.send_photo(message.chat.id, photo=photo, caption='Привет ! 👋\n\nЭто официальный бот PretzelCraft🥨\n\nДля приобретения проходки нажми "Проходка🎫"\n\nПо всем вопросам к ➡️ @ItzKeeni', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'button1':
        photo = open('pass.png', 'rb')
        caption='Проходка на 1 сезон🥨\nЦена: 65р\n\nПроходка выдается на 1 сезон❗️\nДля игры ОБЯЗАТЕЛЬНО нужен Java Minecraft лицензионный🔑\n\nДобавляем в вайтлист в течении 24ч'
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Купить💳', url='https://play.pretzelcraft.fun/')
        button2 = types.InlineKeyboardButton('Назад🔙', callback_data='main')
        markup.add(button1)
        markup.add(button2)
        bot.edit_message_media(media=types.InputMediaPhoto(photo), chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.edit_message_caption(caption=caption, reply_markup=markup, chat_id=call.message.chat.id, message_id=call.message.message_id)

    if call.data == 'button2':
        photo = open('donate.png', 'rb')
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Донат💗', url='https://www.donationalerts.com/r/itzkeeni')
        button2 = types.InlineKeyboardButton('Назад🔙', callback_data='main')
        markup.add(button1)
        markup.add(button2)
        bot.edit_message_media(media=types.InputMediaPhoto(photo), chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.edit_message_caption(caption='Если не сложно, можешь поддержать нас копеечкой \nза любую сумму будет тебе очень благодарны)', reply_markup=markup, chat_id=call.message.chat.id, message_id=call.message.message_id)

    if call.data == 'button3':
        photo = open('link.png', 'rb')
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Сайт 🎮', url='https://play.pretzelcraft.fun/')
        button2 = types.InlineKeyboardButton('Дискорд сервер 💾', url='https://play.pretzelcraft.fun/')
        button3 = types.InlineKeyboardButton('Тг канал 💵', url='https://play.pretzelcraft.fun/')
        button4 = types.InlineKeyboardButton('Назад🔙', callback_data='main')
        markup.add(button1)
        markup.add(button2, button3)
        markup.add(button4)
        bot.edit_message_media(media=types.InputMediaPhoto(photo), chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.edit_message_caption(caption='', reply_markup=markup, chat_id=call.message.chat.id, message_id=call.message.message_id)
    if call.data =='main':
        photo = open('home.png', 'rb')
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Проходка🎫', callback_data='button1')
        button2 = types.InlineKeyboardButton('Донат💗', callback_data='button2')
        button3 = types.InlineKeyboardButton('Ссылки🌿', callback_data='button3')
        markup.add(button1)
        markup.add(button2, button3)
        bot.edit_message_media(media=types.InputMediaPhoto(photo), chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.edit_message_caption(caption='Привет ! 👋\n\nЭто официальный бот PretzelCraft🥨\n\nДля приобретения проходки нажми "Проходка🎫"\n\nПо всем вопросам к ➡️ @ItzKeeni', reply_markup=markup, chat_id=call.message.chat.id, message_id=call.message.message_id)


bot.polling(non_stop=True)
