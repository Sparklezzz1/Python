class Vehicle:

    def __init__(self,_max_speed,__mileage):
        self._max_speed = _max_speed
        self.__mileage = __mileage

    def display_info(self):
        print(f"MaxSpeed: {self._max_speed}")
        print(f"Mileage: {self.__mileage}")

class Bus(Vehicle):

    def __init__(self, _max_speed, __mileage, passenger_capacity):
        super().__init__(_max_speed,__mileage)
        self.passenger_capacity = passenger_capacity

    def display_info(self):
        super().display_info()
        print(f"PassengerCapacity: {self.passenger_capacity}")

bus = Bus(180, 10000, 50)
bus.display_info()