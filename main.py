import sys

import openai
from loguru import logger as log
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, MessageHandler

from config import Config


def openai_request(prompt: str) -> str:
    return openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.2,    # TODO: add user control and random option
    )["choices"][0]["text"].strip()


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(
        f"<b>{update.message.text}</b> {openai_request(prompt=update.message.text)}"
    )


@log.catch()
def main(config: Config) -> None:
    openai.api_key = config.OPENAI_API_KEY

    app = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT, message))

    app.run_polling()


if __name__ == '__main__':
    try:
        main(config=Config())
    except (SystemExit, KeyboardInterrupt):
        sys.exit("SystemExit")
