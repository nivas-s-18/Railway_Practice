class Train:
    def __init__(self, name,sleeper_fare,first_classac_fare,second_classac_fare,total_sleeper_seats,total_first_classac_seats,total_second_classac_seats):
        self.name = name
        self.sleeper_fare = sleeper_fare
        self.first_classac_fare = first_classac_fare
        self.second_classac_fare = second_classac_fare
        self.total_sleeper_seats = total_sleeper_seats
        self.total_first_class_seats = total_first_classac_seats
        self.total_second_class_seats = total_second_classac_seats

        self.available_first_classac_seats = set(range(1, total_first_classac_seats + 1))
        self.available_second_classac_seats = set(range(1, total_second_classac_seats + 1))
        self.available_sleeper_seats = set(range(1, total_sleeper_seats + 1))

        self.booked_sleeper_seats = set()
        self.booked_first_classac_seats = set()
        self.booked_second_classac_seats = set()

    def getstatus(self):
        print("......................")
        print(f"Train Name: {self.name}")
        print(f"First_Class_AC_seats: {self.total_first_class_seats}-{self.available_first_classac_seats}")
        print(f"Second_Class_AC_seats: {self.total_second_class_seats}-{self.available_second_classac_seats}")
        print(f"Sleeper_seats: {self.total_sleeper_seats}-{self.available_sleeper_seats}")
        print("......................")

    def fareinfo(self,ticket_class):
        if ticket_class=="sleeper":
            print(f"Sleeper_class_ticket_price= RS.{self.sleeper_fare}")
        elif ticket_class=="first_class":
            print(f"First_class_Ac_ticket_price= RS.{self.first_classac_fare}")
        elif ticket_class=="second_class":
            print(f"Second_class_Ac_ticket_price= RS.{self.second_classac_fare}")
        else :
            print(f"Invalid_input!!!!")
            print("......................")
    def bookticket(self,seat_number,ticket_class):
        if ticket_class == "sleeper":
            print("Thanks For Booking")
            print(f"Seat number{seat_number}Has been Booked for you")
            available_seats=self.available_sleeper_seats
            booked_seats=self.booked_sleeper_seats
        elif ticket_class == "first_class":
            print(f"Seat number{seat_number}Has been Booked for you")
            available_seats = self.available_first_classac_seats
            booked_seats = self.booked_first_classac_seats
        elif ticket_class == "second_class":
            print(f"Seat number{seat_number}Has been Booked for you")
            available_seats = self.available_second_classac_seats
            booked_seats = self.booked_second_classac_seats
        else:
            print("OOPS!!")
            print("Invalid ticket class")

    def cancelticket(self, seat_number,ticket_class):
        if ticket_class == "sleeper":
            available_seats = self.available_sleeper_seats
            booked_seats = self.booked_sleeper_seats
        elif ticket_class == "first_class":
            available_seats = self.available_first_classac_seats
            booked_seats = self.booked_first_classac_seats
        elif ticket_class == "second_class":
            available_seats = self.available_second_classac_seats
            booked_seats = self.booked_second_classac_seats
        else :
            print("OOPS!!")
            print("Invalid ticket class")

        if seat_number in booked_seats:
            print(f"Ticket for seat {seat_number}in{ticket_class}Has been canceled")
            available_seats.add(seat_number)
            booked_seats.remove(seat_number)
        else:
            print(f"Invalid seat number:{seat_number}in{ticket_class}")

 #Usage
intercity = Train("Chennai Express :: 1808",110,330,220,50,25,25)
intercity.getstatus()

ticket_class=input("Enter the Class(sleeper/first_class/second_class):").lower()
seat_to_book=int(input("Enter the seat number you want to book:"))
intercity.fareinfo(ticket_class)
intercity.bookticket(seat_to_book,ticket_class)

cancel_option = input("Do you want to cancel a ticket? (yes/no): ").lower()
if cancel_option == 'yes':
    seat_to_cancel = int(input("Enter the seat number you want to cancel: "))
    intercity.cancelticket(seat_to_cancel,ticket_class)
    intercity.getstatus()
