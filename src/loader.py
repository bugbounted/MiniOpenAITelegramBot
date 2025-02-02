import openai
from loguru import logger as log

from config import Config, setup_logging


config = Config()
setup_logging(log, config.DEBUG)
openai.api_key = config.OPENAI_API_KEY
