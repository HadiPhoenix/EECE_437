from abc import ABC, abstractmethod
from Profile import Profile
from usersControlRoom import UsersControlRoom


class UniversalUsersAdapter(ABC):
    @abstractmethod
    def add_profile(self, _profile: Profile):
        pass



class UsersAdapter(UniversalUsersAdapter):

    def __init__(self):
        
        self.users_control_room = UsersControlRoom('/home/abed/Desktop/DataBase.db')

    
    def add_profile(self, prof: Profile):
        
        return self.users_control_room.put_profile(prof)

    def get_profile(self, username: str, password: str):
        return self.users_control_room.get_profile(username, password)

