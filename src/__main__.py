from loguru import logger as log
from telegram.ext import filters, ApplicationBuilder, MessageHandler, CommandHandler

from handlers import start, message
from loader import config


@log.opt(exception=True).catch()
def main() -> None:
    app = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, message))

    log.success("Bot started")

    try:
        app.run_polling()
    except (SystemExit, KeyboardInterrupt):
        log.info("System exit")
    finally:
        log.info("Bot stopped")


if __name__ == '__main__':
    main()
