from dataclasses import dataclass

from environs import Env


env = Env()
env.read_env()


@dataclass
class Config:
    TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
    TELEGRAM_USERS = env.list("TELEGRAM_USERS", validate=lambda n: all(user.decimal() for user in n))
    OPENAI_API_KEY = env.list("OPENAI_API_KEY")
