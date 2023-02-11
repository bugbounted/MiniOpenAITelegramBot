from dataclasses import dataclass

from environs import Env
from loguru import logger

env = Env()
env.read_env()


@dataclass
class Config:
    TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
    TELEGRAM_USERS = env.list("TELEGRAM_USERS", validate=lambda n: all(user.isdecimal() for user in n))
    OPENAI_API_KEY = env.str("OPENAI_API_KEY")
    DEBUG = env.bool("DEBUG", default=False)


def setup_logging(log: logger, debug=False):
    if debug:
        log.add(
            'logs/debug.log',
            level='DEBUG',
            colorize=True,
            backtrace=True,
            diagnose=True,
            enqueue=True,
            catch=True,
            delay=True,
        )

    log.add(
        'logs/error.log',
        level='ERROR',
        colorize=True,
        backtrace=True,
        diagnose=debug,
        enqueue=True,
        catch=True,
        rotation='10 MB' if debug else None,
        compression='zip' if debug else None,
        delay=True,
    )
