class Person:
    def __init__(self, name, age, height, weight, unit="imperial"):
        self.name = name
        self.age = age

        if unit == "imperial":
            self.height = height   # inches
            self.weight = weight   # pounds

class BabyCentre:
    def __init__(self):
        self._weigh_count = 0  # total number of times weigh() has been called

    def weigh(self, person: Person) -> int:
        """Return the person's weight and increment the weigh-in counter."""
        self._weigh_count += 1
        return person.weight

    def weigh_ins(self) -> int:
        """Return how many weigh-ins have been performed."""
        return self._weigh_count

if __name__ == "__main__":
    baby_centre = BabyCentre()
    eric = Person("Eric", 1, 31, 30)
    peter = Person("Peter", 33, 72, 175)

    # Show the current total number of weigh-ins (should be 0 at the very start)
    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

    # Weigh Eric twice; each call to weigh() increments the internal counter by 1
    baby_centre.weigh(eric)  # counter → 1
    baby_centre.weigh(eric)  # counter → 2

    # Print the updated total (now 2)
    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

    # Weigh Eric four more times
    baby_centre.weigh(eric)  # counter → 3
    baby_centre.weigh(eric)  # counter → 4
    baby_centre.weigh(eric)  # counter → 5
    baby_centre.weigh(eric)  # counter → 6

    # Print the final total (now 6)
    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")