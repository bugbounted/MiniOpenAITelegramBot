import sys

import openai
from loguru import logger as log
from openai.error import RateLimitError
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, MessageHandler, CommandHandler

from config import Config


config = Config()   # TODO: remove from global scope


def openai_request(prompt: str) -> str:
    return openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.2,    # TODO: add user control and random option
    )["choices"][0]["text"].strip()


async def start_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Send me any prompt to get OpenAI answer.")


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.id in map(int, config.TELEGRAM_USERS):
        log.trace(f"Received a prompt: {update.message.text}")
        response = openai_request(prompt=update.message.text)
        log.trace(f"Received a response: {response}")

        try:
            await update.message.reply_html(
                f"<b>{update.message.text}</b> {openai_request(prompt=update.message.text)}"
            )
        except RateLimitError as e:
            log.error(e)
            await update.message.reply_html(f"Something went wrong:\n<code>{e}</code>")

    else:
        log.trace(f"User {update.effective_user.id} not in the list of allowed users")
        await update.message.reply_text("Access denied!")


@log.opt(exception=True).catch()
def main() -> None:
    openai.api_key = config.OPENAI_API_KEY
    log.success('OpenAI API key loaded successfully')

    app = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start_command_handler))
    app.add_handler(MessageHandler(filters.TEXT, message_handler))

    log.success("Bot started")
    app.run_polling()


if __name__ == '__main__':
    # Configure logging
    log.add(
        'logs/debug.log',
        level='DEBUG',
        colorize=True,
        backtrace=True,
        diagnose=True,
        enqueue=True,
        catch=True,
        rotation='10 MB',
        compression='zip',
        delay=True,
    )

    log.add(
        'logs/error.log',
        level='ERROR',
        colorize=True,
        backtrace=True,
        diagnose=False,
        enqueue=True,
        catch=True,
        rotation='10 MB',
        compression='zip',
        delay=True,
    )

    try:
        main()
    except (SystemExit, KeyboardInterrupt):
        log.info("System exit")
    except Exception as err:
        log.opt(exception=True).error(err)
    finally:
        log.info("Bot stopped")
