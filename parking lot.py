import datetime

class Car:
    def __init__(self, brand, plate_number):
        self.brand = brand
        self.plate_number = plate_number

    def __str__(self):
        return f"{self.brand} ({self.plate_number})"


class Ticket:
    def __init__(self, car, entry_time):
        self.car = car
        self.entry_time = entry_time


class ParkingLot:
    def __init__(self, capacity, rate_per_hour=1000):
        self.capacity = capacity
        self.rate_per_hour = rate_per_hour
        self.occupied = {}  # plate_number -> Ticket

    def park(self, car):
        if len(self.occupied) < self.capacity:
            entry_time = datetime.datetime.now()
            ticket = Ticket(car, entry_time)
            self.occupied[car.plate_number] = ticket
            print(f"Car {car} parked at {entry_time.strftime('%H:%M:%S')}")
            return ticket
        else:
            print("Parking Lot is Full!")
            return None

    def exit(self, ticket, exit_time):
        if ticket.car.plate_number in self.occupied:
            duration = (exit_time - ticket.entry_time).seconds // 3600 + 1
            fee = duration * self.rate_per_hour
            del self.occupied[ticket.car.plate_number]
            print(f"Car {ticket.car} exited. Duration: {duration} hr(s). Fee: UGX {fee}")
            return fee
        else:
            print("Car not found in lot!")
            return 0

    def status(self):
        free = self.capacity - len(self.occupied)
        print(f"Available spots: {free}/{self.capacity}")
        if self.occupied:
            print("Currently parked cars:")
            for t in self.occupied.values():
                print(f" - {t.car}")
        else:
            print("No cars parked.")
# Create Parking Lot with 2 spots
lot = ParkingLot(2, rate_per_hour=2000)

# Create cars
car1 = Car("Subaru Forester ", "UAA123X")
car2 = Car("Range Rover", "UBB456Y")
car3 = Car("Mercedes-Benz GLE-Class Coupe:", "UCC789Z")

# Park cars
ticket1 = lot.park(car1)
ticket2 = lot.park(car2)
lot.status()

# Try to park another car (lot is full)
ticket3 = lot.park(car3)

# Exit car1 after some time
exit_time = datetime.datetime.now() + datetime.timedelta(hours=3)
lot.exit(ticket1, exit_time)

# Park car3 after car1 leaves
ticket3 = lot.park(car3)
lot.status()
