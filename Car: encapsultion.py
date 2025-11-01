class Car:
    def __init__(self):
        self.__odometer = 0   # private attribute: tracks miles driven
        self.__gas = 0        # private attribute: tracks gas left (gallons)

    def fill_up(self):
        self.__gas = 30       # fill the tank to max (30 gallos)

    def drive(self, mi):
        if self.__gas >= mi:                     # if enough gas for the requested miles
            self.__odometer += mi                # increase odometer by miles driven
            self.__gas -= mi                     # reduce gas by miles driven (1 gal. = 1 mile)
        else:                                    # if not enough gas for full trip
            self.__odometer += self.__gas        # drive only as far as gas allows
            self.__gas = 0                       # tank becomes empty

    def __str__(self):
        # return a formatted string showing odometer + gas left
        return f"Car: Odometer reading: {self.__odometer} miles, Gas remaining: {self.__gas}"


# -- Main Program --
print()
car = Car()
print(car)                                      # odometer 0, gas 0
car.fill_up()
print(car)                                      # odometer 0, gas 30
car.drive(20)
print(car)                                      # odometer 20, gas 10
car.drive(50)
print(car)                                      # odometer 30, gas 0 (could only drive 30 miles)
car.drive(10)
print(car)                                      # still odometer 30, gas 0 (no fuel left)
car.fill_up()
car.fill_up()                                   # still fills to 30, second call just overwrites
print(car)                                      # odometer 30, gas 30
