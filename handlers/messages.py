from loader import bot
from telebot import types
from utils.db import record_message


@bot.message_handler()
def all_message_handler(message: types.Message):
    if message.content_type.lower() == "text":
        try:
            record_message(message.from_user.id, message.id, message.text)
        except Exception as err:
            print(err)