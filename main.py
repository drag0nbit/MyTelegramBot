import telebot, random

bot = telebot.TeleBot("6978794115:AAHK-mDHqsfbDdmyof7-qE_9x2SEMU48KLo")


@bot.message_handler(commands=["start"])
def main(msg):
    bot.send_message(msg.chat.id, "_Большой_ *привет!* Ты можешь написать мне привет или написать /game", parse_mode="Markdown")


@bot.message_handler(commands=["game"])
def game(msg):
    markup = telebot.types.InlineKeyboardMarkup(row_width=3)
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    number = number1 + number2
    val1 = number + random.randint(-5, 5)
    val2 = number + random.randint(-5, 5)
    val3 = number + random.randint(-5, 5)
    if val1 == number:
        val1 += random.choice([-3, 3])
    if val2 == number:
        val2 += random.choice([-3, 3])
    if val3 == number:
        val3 += random.choice([-3, 3])
    answer_button_id = random.randint(1, 3)
    if answer_button_id == 1:
        but1 = telebot.types.InlineKeyboardButton(str(number), callback_data="correct")
    else:
        but1 = telebot.types.InlineKeyboardButton(str(val1), callback_data="wrong")
    if answer_button_id == 2:
        but2 = telebot.types.InlineKeyboardButton(str(number), callback_data="correct")
    else:
        but2 = telebot.types.InlineKeyboardButton(str(val2), callback_data="wrong")
    if answer_button_id == 3:
        but3 = telebot.types.InlineKeyboardButton(str(number), callback_data="correct")
    else:
        but3 = telebot.types.InlineKeyboardButton(str(val3), callback_data="wrong")
    markup.add(but1, but2, but3)
    bot.send_message(msg.chat.id, f"{number1} + {number2} = ?", reply_markup=markup)


@bot.message_handler()
def message(msg):
    if "привет" in msg.text.lower() or "hi" in msg.text.lower():
        bot.send_message(msg.chat.id, "И тебе тоже *привет*!", parse_mode="Markdown")
    else:
        bot.send_message(2111817646, f"{msg.from_user.username}: {msg.text}", parse_mode="Markdown")


#        bot.send_message(msg.chat.id, msg.chat.id, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == "correct":
            bot.send_message(call.message.chat.id, "Правильно!")
        if call.data == "wrong":
            bot.send_message(call.message.chat.id, "Неправильно!")


bot.infinity_polling()
