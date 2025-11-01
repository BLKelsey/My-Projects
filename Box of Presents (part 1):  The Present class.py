class Present:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Box:
    def __init__(self, presents):
        self.presents = presents

book = Present("ABC Book", 2)

print()
print("The name of the present:", book.name)
print("The weight of the present:", book.weight, 'lbs')
print("Present:", book.name)
