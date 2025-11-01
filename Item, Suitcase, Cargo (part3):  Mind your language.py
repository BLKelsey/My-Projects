class Item:  # Class to represent a single item with a name and weight
    def __init__(self, name, weight):
        self.__name = name     # private variable: name of the item
        self.__weight = weight # private variable: weight of the item

    def name(self):
        return self.__name     # getter for name

    def weight(self):
        return self.__weight   # getter for weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} lbs)"  # readable string when printing an item


class Suitcase:  # Class to represent a suitcase with a weight limit
    def __init__(self, max_weight):
        self.__max_weight = max_weight  # maximum weight suitcase can carry
        self.__items = []               # list to hold all items added to suitcase

    def add_item(self, item):
        current_weight = 0              # track current total weight
        for i in self.__items:          # loop through items already inside
            current_weight += i.weight()

        if current_weight + item.weight() <= self.__max_weight:
            self.__items.append(item)   # add item if weight limit not exceeded
        else:
            pass                        # ignore item if too heavy (no feedback here)

    def __str__(self):
        count = len(self.__items)
        total_weight = sum(i.weight() for i in self.__items)

        # check if count is 1 to use singular "item"
        if count == 1:
            return f"{count} item ({total_weight} lb)"
        else:
            return f"{count} items ({total_weight} lbs)"



# ---- Test code ----
book = Item("ABC Book", 2)    # create an item: book weighs 2 lbs
phone = Item("Nokia 3210", 1) # create an item: phone weighs 1 lb
brick = Item("Brick", 4)      # create an item: brick weighs 4 lbs

suitcase = Suitcase(5)        # suitcase with max capacity of 5 lbs
print(suitcase)               # no items yet → "0 items (0 lbs)"

suitcase.add_item(book)
print(suitcase)               # book added → "1 items (2 lbs)"

suitcase.add_item(phone)
print(suitcase)               # phone added → "2 items (3 lbs)"

suitcase.add_item(brick)      # too heavy, ignored
print(suitcase)               # still "2 items (3 lbs)"
