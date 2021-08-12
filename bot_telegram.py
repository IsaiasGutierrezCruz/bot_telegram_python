from helper import gsheet_helper
from telegram.ext import Updater, CommandHandler, updater
from helper import gsheet_helper

from cfg import TOKEN

gsconn = gsheet_helper()

def start(update, context):
    user_dic = {
            'id': update.message.from_user.id,
            'first_name': update.message.from_user.first_name,
            'is_bot': update.message.from_user.is_bot,
            'last_name': update.message.from_user.last_name,
            'username': update.message.from_user.username,
            'language_code': update.message.from_user.language_code
    }
    
    gsconn.store_user(user_dic)

    saludos = f"""
    Holis {user_dic["username"]}! Esto es Nani cocina! 
    /promo_dia te dice El mejor pan del mundo!
    """
    update.message.reply_text(saludos)

def promo_dia(update, context):
    items = gsconn.get_items()
    update.message.reply_text(f"{items}")
    

def main():
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("promo_dia", promo_dia))


    # start 
    updater.start_polling()

    # Me quedo esperando 
    updater.idle()

if __name__ == "__main__":
    main()
