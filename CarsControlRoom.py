import sqlite3
from tkinter import*
import time
class Cars_Control_Room(Tk):
    def __init__(self, DB_filepath):
        Tk.__init__(self)
        self.geometry('500x500')
        self.title("Cars Control Room")
        self.DB_filepath = DB_filepath
        self.conn = sqlite3.connect(self.DB_filepath) #connecting to the DB
        self.c = self.conn.cursor()
        self.limit = 10
        self.check_cars()
        self.mainloop()
    def Dropped_Off_Passenger(self, Status, Ride_ID, ID_Num):
        #Function responsible to check if the passenger is dropped off and change cars' statuses accordingly

        if Status == 'Done':
            # Go to CarsLinkedToUsersDB and change the ride status to 'Done' and then go to CarsDB and put Car status as 'Available'

            self.c.execute('UPDATE CarsLinkedToUsers SET STATUS = ? WHERE RIDE_ID = ?' ("Done", Ride_ID))
            self.c.execute('UPDATE Cars SET STATUS = ? WHERE ID_NUM = ?', ("Available", ID_Num))
            self.conn.commit()

        else:
            pass

    def Send_Car_To_Maintenance_Gasoline(self, Notification, CarID):
        #Function reponsible to simulate the deplacement of cars to certain places depending on its status on fuel and mechanics
        if Notification == 2: #Notification 2 is for both mechanic and fuel needs
            Cars(CarID).GoTo_Maitenance_Gasoline('Garage then Gas Station') #Send car to both garage and gas station
        elif Notification == 1: #Notification 1 is for mechanic needs
            Cars(CarID).GoTo_Maitenance_Gasoline('Garage')
        elif Notification == 0: #Notification 0 is for fuel needs
            Cars(CarID).GoTo_Maitenance_Gasoline('Gas Station')
        else:
            pass

    def check_cars(self):
        #Function responsible to handle pending requests and timeouts and changing the cars' statuses in accordance
        self.c.execute('SELECT * FROM CarsLinkedToUsers WHERE STATUS = ?' , ('Pending',))
        car = self.c.fetchall()
        if len(car) == 0:
            self.after(5000, self.check_cars)
        else:
            for temp in car:
                if time.time() - temp[7] >= self.limit:
                    self.c.execute("DELETE FROM CarsLinkedToUsers WHERE CAR_ID_NUM = ? AND STATUS = ?" , (temp[1], 'Pending')) #Delete request if timeout occured
                    self.conn.commit()
                    self.c.execute('UPDATE Cars SET STATUS = ? WHERE ID_NUM = ?', ("Available", temp[1])) #Replace Pending by Available
                    self.conn.commit()

            self.after(5000, self.check_cars)

Cars_Control_Room('/home/abed/Desktop/DataBase.db')
