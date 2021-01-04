from Profile import *
from adapter import *
from users_adapter import *
class Passenger:

    def __init__(self, user_profile: Profile, dispatcher_adapter: UniversalAdapter):
        '''
            In the constructor:
            - initialize the profile of the user
            - assign an adapter which implements the 'UniversalAdapter' interface in order to assure certain functionalities
            - create the timer object, which may be needed later for storing time delay waiting for a car
            - create the fees object, for the passenger to know how much he's supposed to pay
        '''
        self.profile = user_profile
        self.dispatcher_adapter = dispatcher_adapter

    def get_profile(self):
        return self.profile

    def add_balance(self, amount:int):
        self.dispatcher_adapter.add_balance(self.profile.get_user_name(), amount)
        self.profile.add_balance(amount)

    def create_profile(self):
        '''
            returns a response which contains a confirmation for creating a profile
            - response 200/OK
            - response 409/CONFLICT - may be caused by a bad input like duplicate user name or weak password
            - other responsed may be added later, related to service being not available (error 500/503)
        '''
        
        response = self.dispatcher_adapter.add_profile(self.profile)

        return response

    def request_ride(self, from_location: str, to_location: str):
        '''
        Input:
            - from_location str
            - to_location str

        Output:
            - response: tuple containg 2 items, delay_time int & fees int

        After the passenger requests a ride, the backend server returns info about the
        best availabe ride encapsulated in the 'resposne'
        '''

        response = self.dispatcher_adapter.check_car(self.profile, from_location, to_location)

        #self.timer = response(0)
        #self.fees = response(1)

        return response

    def confirm_ride(self, decision: bool)-> bool:
        '''
        trigger a confirmation request
        '''
        return self.dispatcher_adapter.book_ride(self.profile.user_name, decision)
        

    def send_feedback(self, feedback: str):
        '''
        feedback sent after the ride
        '''
        self.dispatcher_adapter.send_feedback(feedback)



        

