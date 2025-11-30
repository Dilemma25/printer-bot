from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot
from aiogram.enums import ParseMode
from src.handlers.router import router
from src.config import Config
from src.handlers import start_handler
from src.handlers import document_handler
from src.handlers import done_handler


bot = Bot(
    token=Config.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

dp.include_router(router)
