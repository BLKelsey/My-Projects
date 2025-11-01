class Computer:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed

class LaptopComputer(Computer):                   # Define a subclass that inherits from Computer
    def __init__(self, model, speed, weight):     # Constructor with three parameters
        super().__init__(model, speed)            # Call parent class constructor for model & speed
        self.weight = weight                      # Add a new attribute specific to LaptopComputer

    def __str__(self):                                                # Define how the object is displayed as a string
        return f"{self.model}, {self.speed} MHz, {self.weight} lbs"   # Format for print output


if __name__ == "__main__":
    laptop = LaptopComputer("Lenovo V14", 3400, 3)
    print()
    print(laptop)
