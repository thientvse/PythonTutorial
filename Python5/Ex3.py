class Vehicle:


    def __init__(self, price, color):
        self.price, self.color = price, color


class Bike(Vehicle):
    def printDetails(self):
        print("Price Bike: "+str(self.price))

class Car(Vehicle):
    def printDetails(self):
        print("Price Car: "+str(self.price))

class Bus(Vehicle):
    def printDetails(self):
        print("Price Bus: "+str(self.price))

bike = Bike(100, "Xanh")
bike.printDetails()

car = Car(200, "Do")
car.printDetails()

bus = Bus(30, "Vang")
bus.printDetails()