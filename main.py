import sys

from loguru import logger as log
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config import Config


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


def main(config: Config):

    app = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("hello", hello))

    app.run_polling()


if __name__ == '__main__':
    try:
        main(config=Config())
    except (SystemExit, KeyboardInterrupt):
        sys.exit("SystemExit")
