from aiogram.types import Message
from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from src.application.services.user_service import UserService
from src.presentation.handlers.router import router
from aiogram.filters import CommandStart


@router.message(CommandStart())
@inject
async def start_handler(
    message: Message,
    user_service: UserService = Provide["services.user_service"]
):
    user_id = message.from_user.id
    user_service.get_by_id(user_id)
    user_service.create()