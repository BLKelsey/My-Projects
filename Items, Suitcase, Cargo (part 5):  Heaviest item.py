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

    def __str__(self):
        count = len(self.__items)
        total_weight = self.weight()
        if count == 1:
            return f"{count} item ({total_weight} lb)"
        else:
            return f"{count} items ({total_weight} lbs)"


# ---- Test code ----
book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

suitcase = Suitcase(10)
suitcase.add_item(book)
suitcase.add_item(phone)
suitcase.add_item(brick)

heaviest = suitcase.heaviest_item()
print(f"The heaviest item: {heaviest}")
