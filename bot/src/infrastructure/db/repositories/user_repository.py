from src.domain.repository_interfaces.user_repository_interface import IUserRepository


class UserRepository(IUserRepository):

    def __init__(self):
        pass

    def create(self):
        print("create user")

    def get_by_id(self, user_id):
        print("get user")