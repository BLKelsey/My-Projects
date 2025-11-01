
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

def fastest_car(cars: list):
    fastest = cars[0]                              # Start by assuming the first car is the fastest

    for car in cars[1:]:                          # Check every remaining car in the list
        if car.top_speed > fastest.top_speed:     # If this car is faster than the current fastest, update the fastest reference
            fastest = car
    return fastest.make                           # Return the make (brand) of the fastest car found

if __name__ == "__main__":
    # Create a few sample cars: Car(make, top_speed)
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]                # Collect them into a list to pass to the function

    print()
    print('The fastest car is: ', fastest_car(cars))     # Call the function and display the result





