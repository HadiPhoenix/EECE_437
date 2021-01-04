from tkinter import*
from Profile import Profile
from passenger import Passenger
from users_adapter import UsersAdapter
from adapter import *
from self_driving_car import *
#import tkMessageBox
class SignUp_Gui:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title("Registration Form")

        self.label_0 = Label(self.root, text="Sign up",width=20,font=("bold", 20))
        self.label_0.place(x=90,y=53)


        self.label_1 = Label(self.root, text="First Name:",width=20,font=("bold", 10))
        self.label_1.place(x=80,y=130)

        self.var_1 = StringVar(self.root)
        self.entry_1 = Entry(self.root, textvariable=self.var_1)
        self.entry_1.place(x=240,y=130)

        self.label_2 = Label(self.root, text="Last Name:",width=20,font=("bold", 10))
        self.label_2.place(x=80,y=180)

        self.var_2 =  StringVar(self.root)

        self.entry_2 = Entry(self.root,textvariable=self.var_2)
        self.entry_2.place(x=240,y=180)

        self.label_3 = Label(self.root, text="username",width=20,font=("bold", 10))
        self.label_3.place(x=80,y=230)

        self.var_3 =  StringVar(self.root)

        self.entry_3 = Entry(self.root, textvariable=self.var_3)
        self.entry_3.place(x=240,y=230)

        self.label_4 = Label(self.root, text="Password:",width=20,font=("bold", 10))
        self.label_4.place(x=80,y=280)

        self.var_4 =  StringVar(self.root)

        self.entry_4 = Entry(self.root, show="*", textvariable=self.var_4)
        self.entry_4.place(x=240,y=280)

        self.label_5 = Label(self.root, text="Confirm Password:",width=20,font=("bold", 10))
        self.label_5.place(x=80,y=330)

        self.var_5 =  StringVar(self.root)

        self.entry_5 = Entry(self.root, show="*", textvariable=self.var_5)
        self.entry_5.place(x=240,y=330)

        self.label_6 = Label(self.root, text="Initial Balance:",width=20,font=("bold", 10))
        self.label_6.place(x=80,y=380)

        self.var_6 =  StringVar(self.root)

        self.entry_6 = Entry(self.root, textvariable=self.var_6)
        self.entry_6.place(x=240,y=380)

        self.submitButton = Button(self.root, text='Submit',width=16,bg='brown',fg='white', command=self.button_submit).place(x=250,y=430)
        self.backButton = Button(self.root, text='Back',width=16,bg='brown',fg='white', command=self.button_back).place(x=250,y=480)
        # it is use for display the registration form on the window
        self.root.mainloop()

    def button_submit(self):
        adapter = UsersAdapter()
        profile = Profile(self.var_1.get(),self.var_2.get(),self.var_3.get(),self.var_4.get(),self.var_6.get())
        adapter.add_profile(profile)

    def button_back(self):
        self.root.withdraw()
        self.root.destroy()
        main_menu()

class SignIn_Gui:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('300x300')
        self.root.title("Sign In")


        self.label_1 = Label(self.root, text="username:",width=20,font=("bold", 10))
        self.label_1.place(x=0,y=80)

        self.var_1 =  StringVar(self.root)
        self.entry_1 = Entry(self.root, textvariable=self.var_1)
        self.entry_1.place(x=120,y=80)

        self.label_2 = Label(self.root, text="password:",width=20,font=("bold", 10))
        self.label_2.place(x=0,y=130)

        self.var_2 =  StringVar(self.root)
        self.entry_2 = Entry(self.root,show="*", textvariable=self.var_2)
        self.entry_2.place(x=120,y=130)

        self.loginButton = Button(self.root, text='Login',width=16,bg='brown',fg='white', command=self.button_login).place(x=120,y=180)
        self.backButton = Button(self.root, text='Back',width=16,bg='brown',fg='white', command=self.button_back).place(x=120,y=230)


    
    def button_login(self):
        adapter = UsersAdapter()
        (prof, token) = adapter.get_profile(self.var_1.get(), self.var_2.get())
        if token == 0:
            self.root.withdraw()
            self.root.destroy()
            Logged_In(prof)

    def button_back(self):
        self.root.withdraw()
        self.root.destroy()
        main_menu()

class Logged_In:

    def __init__(self, prof: Profile):
        self.adapter = RoomsAdapter()
        self.passenger = Passenger(prof, self.adapter) 
        self.bl = True

        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title("Welcome")  

        self.label_1 = Label(self.root, text="from:",width=10,font=("bold", 15))
        self.label_1.place(x=0,y=150)

        self.locations_list = ["Beirut", "Saida", "Tripoli", "Tyre", "Batroun", "Byblous"]
        self.fromVar = StringVar(self.root)
        self.fromVar.set("Beirut")
        self.om = OptionMenu(self.root, self.fromVar, *self.locations_list)
        self.om.place(x=120, y=150)


        self.label_2 = Label(self.root, text="to:",width=10,font=("bold", 15))
        self.label_2.place(x=0,y=180)


        self.locations_list = ["Beirut", "Saida", "Tripoli", "Tyre", "Batroun", "Byblous"]
        self.toVar = StringVar(self.root)
        self.toVar.set("Beirut")
        self.om = OptionMenu(self.root, self.toVar, *self.locations_list)
        self.om.place(x=120, y=180)

        self.request_ride = Button(self.root, text='Request Ride',width=16,bg='brown', command=self.request_ride_button, fg='white' ).place(x=75,y=250)

        self.label_5 = Label(self.root, text="Add to Balance:",font=("bold", 10)) 
        self.label_5.place(x=0,y=80)
        self.var_1 =  StringVar(self.root)
        self.entry_1 = Entry(self.root, textvariable=self.var_1, width=5)
        self.entry_1.place(x=110,y=80)
        self.add_to_balance = Button(self.root, text='Add to Balance',bg='brown', command=self.add_balance, fg='white' ).place(x=170,y=75)

        self.label_6 = Label(self.root, text="Current Balance: "+ str(self.passenger.get_profile().get_balance()) + "$" ,font=("bold", 15)) 
        self.label_6.place(x=0,y=50)    
        self.label_3 = None
        self.label_4 = None
        #self.root.mainloop()



    def request_ride_button(self):
        if self.fromVar.get() == self.toVar.get():
            return
        (time_arrival,fees) = self.passenger.request_ride(self.fromVar.get(),self.toVar.get())
        if time_arrival is not None:
            time_arrival = int(time_arrival)
            time_arrival = "Time for Car arrival: " + str(time_arrival)
            fees = "Ride fees: " + str(fees) + "$"
            self.label_3 = Label(self.root, text=time_arrival,width=20,font=("bold", 10))
            self.label_3.place(x=75,y=290)

            self.label_4 = Label(self.root, text=fees,width=20,font=("bold", 10))
            self.label_4.place(x=75,y=330)
            self.confirm_ride = Button(self.root, text='Confirm Ride',width=16,bg='brown', command=self.confirm_ride_button, fg='white' ).place(x=75,y=370)
            self.decline_ride = Button(self.root, text='Decline Ride',width=16,bg='brown', command=self.decline_ride_button, fg='white' ).place(x=75,y=390)

        else:
            self.label_3 = Label(self.root, text="Sorry,",width=20,font=("bold", 10))
            self.label_3.place(x=75,y=290)

            self.label_4 = Label(self.root, text="No Available Cars",width=20,font=("bold", 10))
            self.label_4.place(x=75,y=330)            

    def confirm_ride_button(self):
        car = self.passenger.confirm_ride(True)
        self.root.withdraw()
        self.root.destroy()
        Confirmed_Ride(car)

    def decline_ride_button(self):
        print(self.passenger.confirm_ride(False))

    def add_balance(self):
        self.passenger.add_balance(int(self.var_1.get()))
        self.label_6['text'] = "Current Balance: "+ str(self.passenger.get_profile().get_balance()) + "$"
        self.entry_1.delete(0, END)

class Confirmed_Ride(Tk):

    def __init__(self, car: SelfDrivingCar):
        Tk.__init__(self)
        self.geometry('500x500')
        self.title("Track Car")

        self.car = car
        self.label_time_left = Label(self,width=40,font=("bold", 15))
       # self.label_time_left.place(x=30,y=25)
        self.label_time_left.pack()
        self.check_car_reached()
        self.mainloop()

    def check_car_reached(self):
        didReach = self.car.approach_passenger()
        if didReach != "reached":

            left_time = "Time left for the car to reach you: " + didReach
            self.label_time_left["text"] = left_time
            self.after(1000,self.check_car_reached)
        else:
            self.label_time_left["text"] = "Car has reached, Please get in"
            self.ride_button = Button(self, text='Get Into Car',width=16,bg='brown',fg='white', command=self.put_seat_belt)
            self.ride_button.pack()

    def put_seat_belt(self):
         self.label_time_left["text"] = "Please put the seat belt"
         self.ride_button.configure(text = "Put Seatbelt", command=self.move_car)

    def move_car(self):
        didReach = self.car.approach_destination()

        if didReach != "reached":
            self.ride_button.configure(text = "Emergency!", command=self.emergency_stop)

            left_time = "Time left for the car to reach " + str(self.car.get_destination()) + ": " + didReach
            self.label_time_left["text"] = left_time
            self.after(1000,self.move_car)
        else:
            self.label_time_left["text"] = "Car has reached destination"
            self.ride_button.configure(text = 'Get Out the Car', command=self.get_out)


    def emergency_stop(self):
        self.label_time_left["text"] = "You may get out of the car"
        self.ride_button.configure(text = 'Get Out the Car', command=self.get_out)

    def get_out(self):
        self.car.reached()

class main_menu:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('300x300')
        self.root.title("Main Menu")

        self.sign_up = Button(self.root, text='Sign Up',width=16,bg='brown',fg='white', command=self.button_sign_up).place(x=75,y=150)
        self.sign_in = Button(self.root, text='Sign In',width=16,bg='brown',fg='white', command=self.button_sign_in).place(x=75,y=175)
        self.root.mainloop()

    def button_sign_up(self):
        self.root.withdraw()
        self.root.destroy()
        SignUp_Gui()

    def button_sign_in(self):
        self.root.withdraw()
        self.root.destroy()
        SignIn_Gui()

     

main_menu()
#Logged_In()
#Confirmed_Ride()