from aiogram.types import CallbackQuery
from src.handlers.router import router


@router.callback_query(lambda c: c.data and c.data.startswith("done:"))
async def handle_done(callback: CallbackQuery):

    user_id_str = callback.data.split(":")[1]
    user_id = int(user_id_str)

    await callback.bot.send_document(
        chat_id=user_id,
        document=callback.message.document.file_id,
        caption="Ваше фото распечатано!"
    )
    await callback.message.edit_reply_markup(None)
