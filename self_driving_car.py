import sqlite3
import time
class SelfDrivingCar:
    def __init__(self, ID_Num, Ride_ID, from_location, to_location, reach_passenger_time, fees, DB_filepath):
        self.conn = sqlite3.connect(DB_filepath)
        self.c = self.conn.cursor()
        self.ID_Num = int(ID_Num)
        self.Ride_ID = Ride_ID
        self.from_location = from_location
        self.to_location = to_location
        self.reach_passenger_time = reach_passenger_time
        self.reach_destination_time = fees

    def approach_passenger(self):
        if self.reach_passenger_time >= 0:
            mins, secs = divmod(self.reach_passenger_time, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs)
            #timer = '00:0' + str(self.reach_passenger_time)
            self.reach_passenger_time -= 1
            return str(timer)
        return "reached"

    def approach_destination(self):
        if self.reach_destination_time >= 0:
            mins, secs = divmod(self.reach_destination_time, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.reach_destination_time -= 1
            return str(timer)
        return "reached"

    def reached(self):
            print(self.ID_Num)
            self.c.execute("DELETE FROM CarsLinkedToUsers WHERE CAR_ID_NUM = ? AND STATUS = ?" , (self.ID_Num, 'OnTrack'))
            self.conn.commit()
            self.c.execute("UPDATE Cars SET STATUS = ? WHERE ID_NUM = ?", ('Available', int(self.ID_Num)))
            self.conn.commit()

    def Passenger_GotOutOf_Car(self, DropOff_Location):
        #if self.Current_Location == DropOff_Location or Car_Status!='Good' :
           # occupancy--
           # return 'Done'
        #else:
        pass

    def Passenger_GotInto_Car(self, Pickup_Location):
       # occupancy++
        #return 'Picked up passenger'
        pass
    
    def Emergency_DropOff(self):
        if Car_Status!= 'Good':
            #pullover to the nearest rest stop
            #warn passenger to get out of car
            #send signal to cars control room
            if SelfDriving_Car.Passenger_GotOutOf_Car()=='Done':
                if occupancy==0:
                    return 'Car is empty'

    def Seatbelt(self):
        return 'Passenger put their seatbelt on'
    
    def GoTo_Maitenance_Gasoline(self, WhereToGo):
        # Go to WhereToGo
        return 'Car with ID_Num ' + str(self.ID_Num) + ' is going to ' + str(WhereToGo)

    def Need_Maintenance_Gasoline(self):
       # if Maintenance_Status != 'Good' and GasolineLeft <= 40:
        #    return 2  # 2 = need both maintenance and gasoline
        #else if Maintenance_Status != 'Good':
         #   return 1  # 1 = need only maintenance
        #else if GasolineLeft <= 40:
         #   return 0  # 0 = need only gasoline
        #else:
        pass

    def ReturnID_Num(self):
        return self.ID_Num

    def ReturnRide_ID(self):
        return self.Ride_ID

    def get_destination(self):
        return self.to_location
