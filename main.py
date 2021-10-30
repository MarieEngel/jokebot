import logging
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    CallbackContext,
    ConversationHandler
)
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

LANGUAGES = [
    'cs',
    'de',
    'en',
    'es',
    'fr',
    'pt',
]

PORT = int(os.environ.get('PORT', '8443'))
TOKEN = os.environ.get('TOKEN', '')

def start(update: Update, _: CallbackContext) -> int:
    logger.info(f"started for {update.message.from_user['username']}")

    keyboard = []
    for language in LANGUAGES:
        keyboard.append(InlineKeyboardButton(language, callback_data=language))
    reply_markup = InlineKeyboardMarkup([keyboard])

    update.message.reply_text('Language?', reply_markup=reply_markup)
    return 0


def language_selected(update: Update, _: CallbackContext) -> int:
    logger.info(f"language selected: {update.callback_query.data}")

    query = update.callback_query
    joke = [update.callback_query.data]

    query.answer()

    query.edit_message_text("\n".join(joke))

    return ConversationHandler.END

def help_command(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Use /start to test this bot.')


def main():
    updater = Updater(TOKEN)

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            0: [CallbackQueryHandler(language_selected)]
        },
        fallbacks=[MessageHandler(Filters.text, help_command)],
    )

    updater.dispatcher.add_handler(conv_handler)

    logger.info(f"Starting webhook on PORT {PORT}")
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.setWebhook(f"https://jokebot.herokuapp.com/{TOKEN}")

    updater.idle()


if __name__ == '__main__':
    main()
