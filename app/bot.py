from .config import config

from telegram.ext import (
    Updater,
    CommandHandler,

)

from .  import handels

def run_bot() -> None:
    updater = Updater(config.BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', handels.start))



    updater.start_polling()
    updater.idle()