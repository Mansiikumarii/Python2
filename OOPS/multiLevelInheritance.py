class Car:
    @staticmethod
    def start():
        print("Car started")
    def stop():
        print("Car stopped")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class UrbanCruiserHyryder(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = UrbanCruiserHyryder("Hybrid")
car2 = UrbanCruiserHyryder("Petrol")
print(car1.type)
print(car2.type)
car1.start()