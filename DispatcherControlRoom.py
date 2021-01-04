import sqlite3
from CarsControlRoom import *
from random import randint
import time
from self_driving_car import *
class Dispatcher_Control_Room:
    def __init__ (self, DB_filepath):
        self.DB_filepath = DB_filepath

    def RequestRide(self, Username, Passenger_Location, Intended_Location):
        self.conn = sqlite3.connect(self.DB_filepath)
        self.c = self.conn.cursor()

        self.c.execute('SELECT * FROM Cars WHERE Current_Location = ? AND Status = ?' , (Passenger_Location,'Available'))
        available_cars = self.c.fetchall()
        if(len(available_cars) != 0):
            Car_ID_Num = available_cars[0][0]
            timer = randint(0,5) + 5
            payment = randint(0,5) + 5
            self.c.execute("INSERT INTO CarsLinkedToUsers (CAR_ID_NUM, USERNAME, PASSENGER_LOCATION, INTENDED_LOCATION, STATUS, Fees, Unix, Delay) VALUES (?,?,?,?,?,?,?,?)",
                                    (int(Car_ID_Num), Username, Passenger_Location, Intended_Location, 'Pending', payment, int(time.time()), timer))

            self.c.execute("UPDATE Cars SET STATUS = ? WHERE ID_NUM = ?", ('Busy', Car_ID_Num))
            
            self.conn.commit()

            return (timer, payment)

        return (None, None)
        


    def ConfirmDeclineRide(self, Username, Confirmed):
        self.conn = sqlite3.connect(self.DB_filepath)
        self.c = self.conn.cursor()
        self.c.execute('SELECT * FROM CarsLinkedToUsers WHERE Username = ? AND STATUS = ?' , (Username, 'Pending'))
        car = self.c.fetchall()
        if len(car) == 0:
            return "Request Timed Out"
        if Confirmed:
            Ride_ID = car[0][0]
            ReservedCarID = car[0][1]
            Passenger_Location = car[0][3]
            Intended_Location = car[0][4]
            fees = car[0][6]
            delay = car[0][8]

            self.c.execute("SELECT BALANCE FROM Users WHERE USERNAME = ?", (Username,))
            Current_Balance = self.c.fetchall()[0][0]
            New_Balance = int(float(Current_Balance)) - fees
            self.c.execute("UPDATE Users SET BALANCE = ? WHERE USERNAME = ?", (New_Balance, Username))
            self.conn.commit()

            self.c.execute("UPDATE CarsLinkedToUsers SET STATUS = ? WHERE USERNAME = ?" , ('OnTrack', Username))
            self.conn.commit()

            return SelfDrivingCar(ReservedCarID, Ride_ID, Passenger_Location, Intended_Location, delay,fees, self.DB_filepath)
        if not Confirmed:
            self.c.execute("DELETE FROM CarsLinkedToUsers WHERE USERNAME = ? AND STATUS = ?" , (Username, 'Pending'))
            self.conn.commit()
            self.c.execute("UPDATE Cars SET STATUS = ? WHERE ID_NUM = ?", ('Available', car[0][1]))
            self.conn.commit()
            return "Your ride has been cancelled"

       # elif (int(confirmDate)-int(ReservationDate))>limit: #this needs to be put in the main and not here
            #exceeded the time limit

       #     return "Timed out, please request a ride again"

       # confirmedCarID = ReservedCarID


       # Cars(Car_ID_Num).Dispatch_To(Passenger_Location, Intended_Location, 5)

       # return "Ride confirmed, Car with ID " + str(confirmedCarID) + " is coming your way in 10 seconds and 5$ has been substracted from your balance."

    def SubmitReview(self, rating, comment, ID_Num):

        self.conn = sqlite3.connect(self.DB_filepath)
        self.c = self.conn.cursor()

        if rating<1 or rating>5:
            return "Invalid raiting submitted"

        self.c.execute("SELECT FROM RatingsTable AverageRating, NumRatings ")


        #read into averageRating and numRatings from DB
        #averageRating=self.c.fetchall()[][]
        #numRatings=self.c.fetchall()[][]

        averageRating= ((averageRating * numRatings) + rating)/(numRatings+1)
        self.c.execute("UPDATE RatingsTable SET AverageRating =" , (averageRating, )+ ", NumRatings=" , (numRating+1, ))

        self.c.execute("INSERT INTO ReviewComments (comment, commentDate) VALUES (comment, reviewdate)")