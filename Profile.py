class Profile:

    def __init__(self, fname: str, lname: str, user: str, password: str, balance: str):
        
        self.first_name = fname
        self.last_name = lname
        self.user_name = user
        self.password = password
        self.balance = balance

    def get_first_name(self):
        return self.first_name

    def get_last_name (self):
        return self.last_name

    def get_user_name(self):
        return self.user_name

    def get_password(self):
        return self.password

    def get_balance(self):
        return self.balance

    def add_balance(self, amount: int):
        self.balance = self.balance + amount
        
    @staticmethod
    def checkPass(password: str)-> int:
        '''
        if length of password < 8 return token -1
        else return 0 
        '''
        if len(password) < 8:
            return -1

        return 0
        


    
