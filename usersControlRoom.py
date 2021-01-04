from Profile import Profile
import sqlite3

class UsersControlRoom: #this class is expected to simulate CRUD APIs controller
    def __init__ (self, DB_filepath):
        self.DB_filepath = DB_filepath

    def put_profile(self, prof: Profile):

        self.conn = sqlite3.connect(self.DB_filepath)
        self.c = self.conn.cursor()

        self.c.execute("INSERT INTO Users (USERNAME, PASSWORD, FIRSTNAME, LASTNAME, BALANCE) VALUES (?, ?, ?, ?, ?)",
                        (prof.get_user_name(), prof.get_password(), prof.get_first_name(), prof.get_last_name(), prof.get_balance()))

        self.conn.commit()

        return True

    def get_profile(self, username, password)->(Profile, int):
        # check if user name exists, check the password
        # if the password is correct, parse data into a profile object and return it
        # a tuple of a profile and a token is returned
        # if user does'nt exists, set token = -1
        # if password is incorrect, set token = -2
        # if username and password are correct, return token = 0
        # In case the login is invalid, set the expected profile object to be returned to "None"

        self.conn = sqlite3.connect(self.DB_filepath)
        self.c = self.conn.cursor()

        self.c.execute("SELECT * FROM Users WHERE USERNAME = ?", (username,))

        Username = self.c.fetchall()
        if len(Username) == 0:
            self.conn.commit()
            return (None, -1)
        if username == Username[0][0]:
            self.c.execute("SELECT PASSWORD From Users WHERE USERNAME = ?" , (username,))
            Password = self.c.fetchall()
            if password == Password[0][0]:
                self.c.execute("SELECT * From Users WHERE USERNAME = ?" , (username,))
                for attributes in self.c.fetchall():
                    USERNAME = attributes[0]
                    PASSWORD = attributes[1]
                    FIRSTNAME = attributes[2]
                    LASTNAME = attributes[3]
                    BALANCE = attributes[4]
                self.conn.commit()
                return(Profile(FIRSTNAME, LASTNAME, USERNAME, PASSWORD, BALANCE), 0)
            else:
                self.conn.commit()
                return(None, -2)

    def Check_Username(self, username):
        self.conn = sqlite3.connect(self.DB_filepath)
        self.c = self.conn.cursor()

        self.c.execute("SELECT * FROM Users WHERE USERNAME = ?", (username,))

        Username = self.c.fetchall()
        if len(Username) == 0:
            self.conn.commit()
            return True
        else:
            self.conn.commit()
            return False

    def Add_To_Balance(self, username, amount):
        self.conn = sqlite3.connect(self.DB_filepath)
        self.c = self.conn.cursor()

        self.c.execute("SELECT BALANCE FROM Users WHERE USERNAME = ?", (username,))

        Current_Balance = self.c.fetchall()[0][0]
        New_Balance = Current_Balance + amount

        self.c.execute("UPDATE Users SET BALANCE = ? WHERE USERNAME = ?", (New_Balance, username))
        self.conn.commit()