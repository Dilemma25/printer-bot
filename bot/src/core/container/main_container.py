from dependency_injector import containers
from dependency_injector import providers
from src.core.config.config import Config
from src.application.container.container import Services
from src.infrastructure.db.container.container import Repositories


class Container(containers.DeclarativeContainer):
    config = providers.Singleton(Config)
    services: providers.Container[Services] = providers.Container(Services)
    repositories: providers.Container[Repositories] = providers.Container(Repositories)