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
    def weigh(self, person):
        return person.weight

    def feed(self, person):
        person.weight += 1

babycenter = BabyCenter()

# Create two people. Default unit is "imperial", so height is in inches and weight in pounds.
eric = Person("Eric", 1, 26, 20)          # 26 in, 20 lb
peter = Person("Peter", 33, 72, 175)      # 72 in, 175 lb

print()
print(f"{eric.name} weighs {babycenter.weigh(eric)} ")
print(f"{peter.name} weighs {babycenter.weigh(peter)}")

print()
babycenter.feed(eric)     # Eric is fed 3xs
babycenter.feed(eric)
babycenter.feed(eric)

print(f"{eric.name} weighs {babycenter.weigh(eric)} ")     #  Use BabyCenter.weigh() to read each person's weight and print it
print(f"{peter.name} weighs {babycenter.weigh(peter)}")
