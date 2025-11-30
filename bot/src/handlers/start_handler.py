from aiogram.types import Message
from src.handlers.router import router
from aiogram.filters import CommandStart


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Здравствуйте,\n\nОтправьте пожалуйста фотографию в формате файла (без сжатия) для распечатки"
    )
