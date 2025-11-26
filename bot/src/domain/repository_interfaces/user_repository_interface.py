from abc import ABC
from abc import abstractmethod

class IUserRepository(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def get_by_id(self, user_id:str):
        pass


