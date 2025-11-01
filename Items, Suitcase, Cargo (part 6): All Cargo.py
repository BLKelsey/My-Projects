class Item:  # Class to represent a single item with a name and weight
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} lbs)"

class Suitcase:  # Class to represent a suitcase with a weight limit
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.__items = []

    def add_item(self, item):
        current_weight = sum(i.weight() for i in self.__items)
        if current_weight + item.weight() <= self.__max_weight:
            self.__items.append(item)

    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        return sum(i.weight() for i in self.__items)

    def heaviest_item(self):
        if not self.__items:  # suitcase empty
            return None

        heaviest = self.__items[0]  # start with the first item
        for item in self.__items:
            if item.weight() > heaviest.weight():
                heaviest = item
        return heaviest

class CargoHold:
    def __init__(self, max_weight):                     # constructor, takes maximum weight as argument
        self.max_weight = max_weight                    # store the maximum weight capacity
        self.suitcases = []                             # start with an empty list of suitcases

    def add_suitcase(self, suitcase):                             # method to add a suitcase
        current_weight = sum(s.weight() for s in self.suitcases)  # calculate current total weight of all suitcases
        if current_weight + suitcase.weight() <= self.max_weight: # only add if it doesn’t exceed cargo hold max
            self.suitcases.append(suitcase)                       # add the suitcase to the list

    def __str__(self):                                              # method to print a human-readable string
        number_of_suitcases = len(self.suitcases)                   # how many suitcases currently in the cargo hold
        current_weight = sum(s.weight() for s in self.suitcases)    # total weight of all suitcases
        remaining_space = self.max_weight - current_weight          # space left before reaching capacity
        return f"{number_of_suitcases} suitcases, space for {remaining_space} lbs"

# ---- Test code ----
cargo_hold = CargoHold(1000)                            # create a CargoHold with max 1000 lbs
print()
print(cargo_hold)                                       # should print "0 suitcases, space for 1000 lbs"

book = Item("ABC Book", 2)                  # create items with weights
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

adas_suitcase = Suitcase(10)                            # suitcase for Ada with 10 lbs capacity
adas_suitcase.add_item(book)                            # add book (2 lbs)
adas_suitcase.add_item(phone)                           # add phone (1 lb) → suitcase total = 3 lbs

peters_suitcase = Suitcase(10)                          # suitcase for Peter
peters_suitcase.add_item(brick)                         # add brick (4 lbs)

cargo_hold.add_suitcase(adas_suitcase)                  # add Ada’s suitcase (3 lbs total)
print("Adas: ", cargo_hold)                             # should show 1 suitcase, 997 lbs space left
cargo_hold.add_suitcase(peters_suitcase)                # add Peter’s suitcase (4 lbs total)
print("Peter's: ", cargo_hold)                          # should show 2 suitcases, 993 lbs space left
