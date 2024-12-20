class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        return f"Ride costs {self.fare}$, toghether we drove {self.distance}"


def main():
    ride1 = TaxiRide(rate_per_km=5)
    ride1.calculate_fare(30)

    print(f'First ride costs, {ride1.print_receipt()}')

if __name__ == "__main__":
    main()
