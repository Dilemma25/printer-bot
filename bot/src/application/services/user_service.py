from src.domain.repository_interfaces.user_repository_interface import IUserRepository
from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject


class UserService:
    @inject
    def __init__(
                self,
                user_repository: IUserRepository = Provide["repositories.user_repository"]
    ):
        print("Init UserService")
        self.user_repository = user_repository

    def create(self):
        self.user_repository.create()

    def get_by_id(self, user_id: str):
        self.user_repository.get_by_id(user_id)