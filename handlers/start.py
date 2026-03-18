from loader import bot
from telebot import types
from keyboards.main_menu import menu_kb


@bot.message_handler(commands=["start"])
def start_handler(message: types.Message):
    greeting_text = f"Assalomu alaykum <b>{message.from_user.full_name}</b>\n"\
                    f"<i>Bizning botga xush kelibsiz</i>\n"\
                    f"<a href='kun.uz'>Yangiliklar</a>"
    
    bot.send_message(message.chat.id, greeting_text, reply_markup=menu_kb())