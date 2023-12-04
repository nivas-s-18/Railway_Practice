class Train:
    def __init__(self, name, fare, total_seats):
        self.name = name
        self.fare = fare
        self.total_seats = total_seats
        self.available_seats = set(range(1, total_seats + 1))
        self.booked_seats = set()

    def getstatus(self):
        print("......................")
        print(f"Train Name: {self.name}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")
        print("......................")

    def fareinfo(self):
        print(f"Ticket Price: Rs{self.fare}")
        print("......................")
    def bookticket(self, seat_number):
        if seat_number in self.available_seats:
            print(f"Ticket has been booked for Seat {seat_number}")
            self.available_seats.remove(seat_number)
            self.booked_seats.add(seat_number)
        else:
            print("OOPS!!")
            print("Seat already booked or invalid seat number.")

    def cancelticket(self, seat_number):
        if seat_number in self.booked_seats:
            print(f"Ticket for Seat {seat_number} has been canceled")
            self.available_seats.add(seat_number)
            self.booked_seats.remove(seat_number)
        else:
            print(f"Invalid Seat Number: {seat_number}")

intercity = Train("Chennai Express :: 1808", 110, 30)
intercity.getstatus()

seat_to_book = int(input("Enter the seat number you want to book: "))
intercity.bookticket(seat_to_book)


cancel_option = input("Do you want to cancel a ticket? (yes/no): ").lower()
if cancel_option == 'yes':
    seat_to_cancel = int(input("Enter the seat number you want to cancel: "))
    intercity.cancelticket(seat_to_cancel)
    intercity.getstatus()
