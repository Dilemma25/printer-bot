from dependency_injector import containers
from dependency_injector import providers
from src.infrastructure.db.repositories.user_repository import UserRepository


class Repositories(containers.DeclarativeContainer):
    user_repository = providers.Singleton(UserRepository)