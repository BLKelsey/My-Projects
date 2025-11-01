class Person:
    def __init__(self, name, age, height, weight, unit="imperial"):
        self.name = name

        # Only store height/weight when using imperial units.
        # (Note: if unit != "imperial", height/weight won't be set.)
        if unit == "imperial":
            self.height = height   # inches
            self.weight = weight   # pounds

# A "service" class that can weigh a Person
class BabyCenter:
    def weigh(self, person: Person):
        return person.weight

babycenter = BabyCenter()

# Create two people. Default unit is "imperial", so height is in inches and weight in pounds.
eric = Person("Eric", 1, 26, 20)          # 26 in, 20 lb
peter = Person("Peter", 33, 72, 175)      # 72 in, 175 lb

print()
# Use BabyCenter.weigh() to read each person's weight and print it
print(f"{eric.name} weighs {babycenter.weigh(eric)} lbs")
print(f"{peter.name} weighs {babycenter.weigh(peter)} lbs")
