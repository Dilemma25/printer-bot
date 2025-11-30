from src.handlers.router import router
from aiogram import F
from aiogram.types import Message
from src.keyboard import make_done_keyboard
from src.config import Config


@router.message(F.document)
async def handle_photo(message: Message):
    username = message.from_user.username
    user_id = message.from_user.id

    if message.document is None:
        return

    file_id = message.document.file_id

    await message.bot.send_document(
        chat_id=Config.ADMIN_ID,
        document=file_id,
        caption=f"От пользователя: {username}",
        reply_markup=make_done_keyboard(user_id)
    )

    await message.bot.send_document(
        chat_id=user_id,
        document=file_id,
        caption="Фото отправлено на печать."
    )
