from abc import ABC, abstractmethod
import time
from Profile import Profile
import passenger
from usersControlRoom import UsersControlRoom
from DispatcherControlRoom import Dispatcher_Control_Room


class UniversalAdapter(ABC):
    #This is walk-around to have interfaces in python
   # @abstractmethod
    #def add_profile(self, _profile: Profile):
     #   pass

    @abstractmethod
    def check_car(self, user: Profile, from_location: str, to_location: str):
        pass

    @abstractmethod
    def book_ride(self, username: str):
        pass

   # @abstractmethod
  #  def send_feedback(self, feedback):
   #     pass


class RoomsAdapter(UniversalAdapter):

    def __init__(self):

        self.dispatcher_room = Dispatcher_Control_Room('/home/abed/Desktop/DataBase.db')
        self.users_room = UsersControlRoom('/home/abed/Desktop/DataBase.db')

    
    def check_car(self, user: str, from_location: str, to_location: str):
        
        return self.dispatcher_room.RequestRide(user.user_name, from_location, to_location) #for now we are returning an str,
                                                                                            #but a tuple of ints is expected

    def book_ride(self, user: str, decision: bool):

        return self.dispatcher_room.ConfirmDeclineRide(user, decision)

    def add_balance(self, user: str, amount: int):
        self.users_room.Add_To_Balance(user, amount)

   # def send_feedback(self, feedback):
    #   ...
    #    self.dispatcher_room.SubmitReview(...)





