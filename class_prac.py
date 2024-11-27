# in this module we are going to prac the python programs related to class

# to define class syntax: class Class_name:


class Car:
    wheels = 4  # this is a class variable which will be available for all the instances and will be same for all unless explicitly changed
    Total_cars=0

    def __init__(
        self, name, color, year
    ):  # this is a constructor which will be called automatically when an instance of the class is created
        # in this we get "self" and been used to make the attributes for the instance of the class and other than self are the parameters we can supply for the instance of the class to create
        self.name = name
        self.color = color
        self.year = year
        Car.Total_cars +=1 # by thi we can keep track of the total number of cars with the help of class variable made with same class
    
    def drive(self):
        print(f"{self.name} is started")
    
    def stop(self):
        print(f"{self.name} has stopped")
        
car1 = Car("Hyundai", "blue", "2024")
car2 = Car("BMW", "black", "2025")
car3 = Car("Charvollete", "white", "2022")
print(car1.name)
print(car1.color)
print(car1.year)
print(car1.wheels)
print(car1.Total_cars)
car1.drive()
car1.stop()