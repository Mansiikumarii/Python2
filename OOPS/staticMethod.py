class Car:
    color= "white"
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
    
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Innova Crysta")
print(car1.name)
print(car2.name)
car1.start()
car2.stop()
print(car1.color)
print(car2.color)
car1.color = "red"
print(car1.color)
print(car2.color)  # This will still print "white" since car2.color is not set
print(Car.color)  # This will print "white" since it's the class variable   
print(ToyotaCar.color)  # This will also print "white" since it's inherited from Car