from loader import bot, ADMINS
from time import sleep
import handlers
from utils.db import create_user_table

def notify_admin():
    """
    BOT ishga tushganda adminlarga xabar berish funksiyasi
    """
    for admin in ADMINS:
        sleep(0.3)
        try:
            bot.send_message(admin, "Men ishga tushdim!")
        except:
            pass
    print("Bot ishga tushdi")

if __name__ == "__main__":
    notify_admin()
    create_user_table()
    bot.infinity_polling()