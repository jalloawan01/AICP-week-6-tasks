#AICP week 6 tasks

class WildlifePark:
    def __init__(self):
        self.one_day_prices = {
            "Adult": 20.00,
            "Child": 12.00,
            "Senior": 16.00,
            "Family": 60.00,
            "Group": 15.00
        }

        self.two_day_prices = {
            "Adult": 30.00,
            "Child": 18.00,
            "Senior": 24.00,
            "Family": 90.00,
            "Group": 22.50
        }

        self.extra_attraction_prices = {
            "Lion Feeding": 2.50,
            "Penguin Feeding": 2.00,
            "Evening Barbecue": 5.00
        }

        self.available_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        self.bookings = {}
        self.booking_counter = 1

    def display_ticket_options(self):
        print("Available Tickets for One-Day Entry:")
        self._display_ticket_prices(self.one_day_prices)

        print("\nAvailable Tickets for Two-Day Entry:")
        self._display_ticket_prices(self.two_day_prices)

        print("\nExtra Attractions:")
        for attraction, price in self.extra_attraction_prices.items():
            print(f"{attraction}: ${price:.2f}")

        print("\nAvailable Booking Days:")
        print(", ".join(self.available_days))

    def _display_ticket_prices(self, prices):
        for ticket_type, price in prices.items():
            print(f"{ticket_type}: ${price:.2f}")

    def process_booking(self, booking_day, ticket_type, num_tickets, selected_attractions=None):
        total_cost = 0

        if ticket_type not in self.one_day_prices and ticket_type not in self.two_day_prices:
            print("Invalid ticket type.")
            return

        if booking_day not in self.available_days:
            print("Invalid booking day.")
            return

        if ticket_type in self.one_day_prices:
            total_cost += self.one_day_prices[ticket_type]
        else:
            total_cost += self.two_day_prices[ticket_type]

        total_cost *= num_tickets

        if selected_attractions:
            for attraction in selected_attractions:
                if attraction in self.extra_attraction_prices:
                    total_cost += self.extra_attraction_prices[attraction] * num_tickets
                else:
                    print(f"Invalid attraction: {attraction}")

        booking_number = self.booking_counter
        self.booking_counter += 1
        self.bookings[booking_number] = {"Booking Day": booking_day, "Ticket Type": ticket_type, "Number of Tickets": num_tickets, "Total Cost": total_cost}

        print(f"Booking Details:")
        print(f"Booking Number: {booking_number}")
        print(f"Booking Day: {booking_day}")
        print(f"Ticket Type: {ticket_type}")
        print(f"Number of Tickets: {num_tickets}")
        print(f"Total Cost: ${total_cost:.2f}")

    def check_best_value(self, num_tickets, ticket_type):
        if ticket_type == "Group" and num_tickets >= 6:
            return True
        elif ticket_type == "Family" and num_tickets >= 3:
            return True
        else:
            return False


def main():
    park = WildlifePark()

    # Display ticket options, attractions, and available days
    park.display_ticket_options()

    # Process a booking
    booking_day = input("\nEnter booking day: ")
    ticket_type = input("Enter ticket type: ")
    num_tickets = int(input("Enter number of tickets: "))
    selected_attractions = input("Enter attractions (comma-separated): ").split(",") if input("Are there any attractions? (y/n): ").lower() == 'y' else None

    park.process_booking(booking_day, ticket_type, num_tickets, selected_attractions)

    # Check for best value options
    if not park.check_best_value(num_tickets, ticket_type):
        print("For better value, consider alternative booking options.")


if __name__ == "__main__":
    main()

