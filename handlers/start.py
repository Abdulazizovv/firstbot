from loader import bot
from telebot import types
from keyboards.main_menu import menu_kb, inline_menu_kb
from utils.db import create_or_update_user


@bot.message_handler(commands=["start"])
def start_handler(message: types.Message):
    created = False
    try:
        created = create_or_update_user(
            user_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username
        )
    except Exception as err:
        print(err)
    greeting_text = f"Assalomu alaykum <b>{message.from_user.full_name}</b>\n"\
                    f"<i>Bizning botga xush kelibsiz</i>\n"\
                    f"<a href='kun.uz'>Yangiliklar</a>"
    
    bot.send_message(message.chat.id, greeting_text, reply_markup=inline_menu_kb)


@bot.callback_query_handler()
def callback_handler(call: types.CallbackQuery):
    bot.send_message(call.from_user.id, "Kurslar ro'yxati jo'natilishi kerak edi")