from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot
from aiogram.enums import ParseMode
from src.core.container.main_container import Container
from src.presentation.handlers.router import router
import src.presentation.handlers.start_handler as start_handler_module

container = Container()
container.wire(modules=[start_handler_module])

bot = Bot(
    token=container.config().BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

dp.include_router(router)