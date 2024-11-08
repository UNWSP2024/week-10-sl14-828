class Car:
    # write a class named car that has the following data attributes:
    # __year_model (for the car's year model)
    # __make (for the make of the car)
    # __speed (for the car's current speed)
    
    def __init__(self, year_model, make):
        # the car class should have an __init__ method that accepts the car's year model and make as arguments.
        # these values should be assigned to the object's __year_model and __make data attributes.
        # it should also assign 0 to the __speed data attribute.
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0  # initial speed is 0

    # the accelerate method should add 5 to the speed data attribute each time it is called.
    def accelerate(self):
        self.__speed += 5

    # the brake method should subtract 5 from the speed data attribute each time it is called.
    def brake(self):
        self.__speed -= 5

    # the get_speed method should return the current speed.
    def get_speed(self):
        return self.__speed

# next, design a program that creates a car object then calls the accelerate method five times.
# after each call to the accelerate method, get the current speed of the car and display it.
# the call the brake method.
# after each call to the brake method, get the current speed of the car and display it.

# create a car object with year model and make
my_car = Car(2023, 'Toyota')

# accelerate the car 5 times and print the speed after each acceleration
print("accelerating the car:")
for _ in range(5):
    my_car.accelerate()
    print(f"current speed: {my_car.get_speed()} mph")

# brake the car 5 times and print the speed after each brake
print("\nbraking the car:")
for _ in range(5):
    my_car.brake()
    print(f"current speed: {my_car.get_speed()} mph")
