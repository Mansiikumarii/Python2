class Car:
    def __init__(self):
        self.clutch = False
        self.acc= False
        self.brake = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started")
Car1 = Car()
Car1.start()