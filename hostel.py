class Visitor:
    def __init__(self, name, visitor_id):
        self.name = name
        self.visitor_id = visitor_id

    def __str__(self):
        return f"{self.name} (ID: {self.visitor_id})"


class Resident:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return f"{self.name} [Room: {self.room}]"


class Hostel:
    def __init__(self, name):
        self.name = name
        self.visits = []   # list to store visits

    def record_visit(self, visitor, resident, arrival, departure):
        visit = {
            "visitor": visitor,
            "resident": resident,
            "arrival": arrival,
            "departure": departure
        }
        self.visits.append(visit)
        print(f"\n✅ Visit recorded: {visitor.name} visited {resident.name}")

    def show_visits(self):
        print(f"\n📋 Visit Records for {self.name}:")
        if not self.visits:
            print("No visits recorded yet.")
        else:
            for i, v in enumerate(self.visits, start=1):
                print(f"{i}. Visitor: {v['visitor']} → Resident: {v['resident']}, "
                      f"Arrival: {v['arrival']}, Departure: {v['departure']}")


# -------- Main Program --------
hostel_name = input("Enter hostel name: ")
hostel = Hostel(hostel_name)

while True:
    print("\n--- Hostel Visit Recording System ---")
    print("1. Record a new visit")
    print("2. Show all visits")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        # Get visitor details
        v_name = input("Enter visitor name: ")
        v_id = input("Enter visitor ID: ")
        visitor = Visitor(v_name, v_id)

        # Get resident details
        r_name = input("Enter resident name: ")
        r_room = input("Enter resident room number: ")
        resident = Resident(r_name, r_room)

        # Get visit times
        arrival = input("Enter arrival time: ")
        departure = input("Enter departure time: ")

        # Record visit
        hostel.record_visit(visitor, resident, arrival, departure)

    elif choice == "2":
        hostel.show_visits()

    elif choice == "3":
        print("\n👋 Exiting program. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")
