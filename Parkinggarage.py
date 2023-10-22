class ParkingGarage:
    def __init__(self, tickets, parking_spaces):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = {}

    def takeTicket(self):
        self.tickets -= 1
        self.parking_spaces -= 1

    def payForParking(self):
        payment = input("Please enter your payment: ")
        if payment:
            print("Your ticket has been paid and you have 15 mins to leave.")
            self.current_ticket["paid"] = True

    def leaveGarage(self):
        if self.current_ticket.get("paid"):
            print("Thank You, have a nice day.")
        else:
            self.payForParking()
            print("Thank You, have a nice day!")
        self.parking_spaces += 1
        self.tickets += 1
        
garage = ParkingGarage(10, 10)