class Flight:
    def __init__(self, flight_id, origin, destination, price):
        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.price = price

    def __repr__(self):
        return f"Flight({self.flight_id}, {self.origin}, {self.destination}, {self.price})"


def search_flights(flights, option):
    if option == 1:
        city = input("Enter the city of origin: ")
        return [flight for flight in flights if flight.origin == city]
    elif option == 2:
        city = input("Enter the destination city: ")
        return [flight for flight in flights if flight.destination == city]
    elif option == 3:
        origin_city = input("Enter the origin city: ")
        dest_city = input("Enter the destination city: ")
        return [flight for flight in flights if flight.origin == origin_city and flight.destination == dest_city]
    else:
        print("Invalid option")


if __name__ == "__main__":
    flights = [
        Flight("AI161E90", "BLR", "BOM", 5600),
        Flight("BR161F91", "BOM", "BBI", 6750),
        Flight("AI161F99", "BBI", "BLR", 8210),
        Flight("VS171E20", "JLR", "BBI", 5500),
        Flight("AS171G30", "HYD", "JLR", 4400),
        Flight("AI131F49", "HYD", "BOM", 3499),
    ]

    search_option = int(input("Enter the search option (1, 2, or 3): "))

    filtered_flights = search_flights(flights, search_option)

    if filtered_flights:
        print(filtered_flights)
    else:
        print("No flights found.")