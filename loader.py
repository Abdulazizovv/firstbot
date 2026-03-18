from telebot import TeleBot
from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN", None)
ADMINS = env.list("ADMINS")

if not TOKEN:
    raise Exception("Token sozlanmagan")

bot = TeleBot(token=TOKEN, parse_mode="HTML")