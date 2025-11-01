class Present:
    def __init__(self, name, weight):
        self.name, self.weight = name, weight   # one-line assignment

    def __str__(self):
        return f"Present: {self.name} ({self.weight} lb)"

class Box:
    def __init__(self, presents=None):
        self.presents = presents or []         # use default empty list

    def add_present(self, present):
        self.presents.append(present)

    def total_weight(self):
        return sum(p.weight for p in self.presents)  # use sum + generator

book = Present("ABC Book", 2)
cd = Present("Pink Floyd: Dark Side of the Moon", 1)
box = Box()
box.add_present(book)
print(f"The book weighs {box.total_weight()} lbs")
box.add_present(cd)
print(f"The Pink Floyd CD + the book weigh {box.total_weight()} lbs")
