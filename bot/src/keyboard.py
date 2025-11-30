from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def make_done_keyboard(user_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Готово👍",
                    callback_data=f"done:{user_id}"
                )
            ]
        ]
    )
