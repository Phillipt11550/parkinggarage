class ParkingGarage:
    def __init__(self, tickets, parking_spaces):
        self.tickets = list(range(1, tickets + 1))
        self.parking_spaces = parking_spaces
        self.current_ticket = {}

    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            self.current_ticket[ticket] = False
            print(f"Ticket number {ticket} has been issued.")
        else:
            print("No more tickets available.")

    def payForParking(self, ticket):
        payment = input("Please enter your payment: ")
        if payment:
            print("Your ticket has been paid and you have 15 mins to leave.")
            self.current_ticket[ticket] = True

    def leaveGarage(self, ticket):
        if self.current_ticket.get(ticket):
            print("Thank You, have a nice day.")
            del self.current_ticket[ticket]
            self.tickets.append(ticket)
            self.tickets.sort()
        else:
            print("Please pay for your parking before leaving.")

def run_parking_garage():
    garage = ParkingGarage(10, 10)
    while True:
        action = input("What would you like to do? (take/pay/leave/quit): ")
        if action.lower() == "take":
            garage.takeTicket()
        elif action.lower() == "pay":
            ticket = int(input("Please enter your ticket number: "))
            garage.payForParking(ticket)
        elif action.lower() == "leave":
            ticket = int(input("Please enter your ticket number: "))
            garage.leaveGarage(ticket)
        elif action.lower() == "quit":
            break
        else:
            print("Invalid action. Please try again.")

run_parking_garage()