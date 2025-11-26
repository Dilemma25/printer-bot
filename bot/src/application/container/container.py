from dependency_injector import providers
from dependency_injector import containers
from src.application.services.user_service import UserService


class Services(containers.DeclarativeContainer):
    user_service = providers.Singleton(UserService)