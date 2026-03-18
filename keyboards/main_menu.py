from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def menu_kb():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("Web dasturlash")
    btn2 = KeyboardButton("Frontend dasturlash")
    btn3 = KeyboardButton("Backend dasturlash")
    btn4 = KeyboardButton("English")
    btn0 = KeyboardButton("Telefon raqamni jo'natish", request_contact=True)
    btn = KeyboardButton("Joylashuvni jo'natish", request_location=True)

    markup.add(btn0)
    markup.add(btn)

    markup.add(btn1, btn4)
    markup.add(btn2, btn3)
    return markup
