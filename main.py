class Flight:
    def _init_(self, flight_id, from_city, to_city, price):
        self.flight_id = flight_id
        self.from_city = from_city
        self.to_city = to_city
        self.price = price

    def _repr_(self):
        return f"Flight({self.flight_id}, {self.from_city}, {self.to_city}, {self.price})"


def search_flights(flights, search):
    if search == 1:
        city = input("Enter the city: ")
        return [flight for flight in flights if flight.from_city == city]
    elif search == 2:
        city = input("Enter the city: ")
        return [flight for flight in flights if flight.to_city == city]
    elif search == 3:
        city_from = input("Enter the city from: ")
        city_to = input("Enter the city to: ")
        return [flight for flight in flights if flight.from_city == city_from and flight.to_city == city_to]
    else:
        print("ERROR")


if _name_ == "_main_":
    flights = [
        Flight("AI161E90", "BLR", "BOM", 5600),
        Flight("BR161F91", "BOM", "BBI", 6750),
        Flight("AI161F99", "BBI", "BLR", 8210),
        Flight("VS171E20", "JLR", "BBI", 5500),
        Flight("AS171G30", "HYD", "JLR", 4400),
        Flight("AI131F49", "HYD", "BOM", 3499),
    ]

    search = int(input("Enter the search parameter (1, 2, or 3): "))

    filtered_flights = search_flights(flights, search)

    if filtered_flights:
        print(filtered_flights)
    else:
        print("No flights found.")