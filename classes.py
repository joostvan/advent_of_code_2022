# write a python program to create a vehicle class wiht max_speed and mileage instance attributes

class Vehicle:
    # instance variables
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    # instance method
    def seating_capacity(self, capacity):
        return f"the seating capacity is {capacity} passangers"

modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)
# the class is a user-defined data structure that binds the data members and methods into a single unit
# class is a blueprint or code template for object creation
# an object is an instance of the class

# write a ptyhon class without any variables and methods

class Car:
    pass

#Bus = Vehicle()

# CREATE A CLASS BUS THAT WILL INHERIT ALL THE VARIABLES AND THE METHODS OF THE VEHICLE CLASS

#For example, suppose we have a class that is not implemented yet, 
#but we want to implement it in the future, and they cannot have an empty body because 
# the interpreter gives an error. So use the pass statement to construct a body that does nothing.

class Bus(Vehicle):
    pass


school_bus = Bus(180, 12)
print(school_bus.max_speed, school_bus.mileage)

# CREATE A LIMO CLASS THAT INHERITS FROM THE VEHICLE CLASS
class Limo(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

limo = Limo(120,20)
print(limo.seating_capacity())


