# trainbooking.py
# Train Ticket Booking System (CLI App)

# Initial ticket availability
tickets = {
    1: {"route": "Mumbai to Goa", "available": 10},
    2: {"route": "Mumbai to Pune", "available": 10},
    3: {"route": "Chennai to Bhopal", "available": 10}
}

password = "kdb"

def show_menu():
    print("\n----- TRAIN TICKET BOOKING SYSTEM -----")
    print("1. Select journey & book ticket")
    print("2. View available tickets")
    print("3. Add more seats (Manager only)")
    print("4. Exit")

def show_journeys():
    for key in tickets:
        print(f"{key}. {tickets[key]['route']}")

while True:
    show_menu()
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # BOOK TICKET
    if choice == 1:
        show_journeys()
        journey = int(input("Select journey number: "))

        if journey in tickets:
            book = int(input("Press 1 to book ticket, 2 to cancel: "))

            if book == 1:
                tic = int(input("How many tickets do you want to book? "))

                if tickets[journey]["available"] >= tic:
                    tickets[journey]["available"] -= tic
                    print("✅ Tickets booked successfully. Happy Journey!")
                else:
                    print("❌ Sorry, not enough tickets available.")
            else:
                print("Booking cancelled.")
        else:
            print("Invalid journey selection.")

    # VIEW AVAILABLE TICKETS
    elif choice == 2:
        print("\n--- Available Tickets ---")
        for key in tickets:
            print(f"{tickets[key]['route']}: {tickets[key]['available']} seats")

    # ADD TICKETS (MANAGER)
    elif choice == 3:
        pas = input("Enter manager password: ")

        if pas == password:
            show_journeys()
            journey = int(input("Select journey number: "))
            add = int(input("How many tickets do you want to add? "))

            if journey in tickets:
                tickets[journey]["available"] += add
                print("✅ Tickets added successfully.")
            else:
                print("Invalid journey.")
        else:
            print("❌ Wrong password.")

    # EXIT
    elif choice == 4:
        print("Thank you for using the Train Ticket Booking App 🚆")
        break

    else:
        print("Please select a valid option.")
