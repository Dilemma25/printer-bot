import asyncio
import logging
from src.dispatcher import bot
from src.dispatcher import dp


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
