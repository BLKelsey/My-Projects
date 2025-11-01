class ShoppingList:
    def __init__(self):
        # A list of tuples (item_name, amount)
        self._items = []

    def add_item(self, name, amount):
        self._items.append((name, amount))

    # Method 1: returns number of items
    def number_of_items(self):
        return len(self._items)

    # Method 2: returns the name of the nth item (1-indexed)
    def item(self, n):
        if 1 <= n <= len(self._items):
            return self._items[n - 1][0]
        else:
            return None

    # Method 3: returns the amount of the nth item (1-indexed)
    def amount(self, n):
        if 1 <= n <= len(self._items):
            return self._items[n - 1][1]
        else:
            return None


# Example usage:
shopping_list = ShoppingList()
shopping_list.add_item("Bananas", 4)
shopping_list.add_item("Milk", 1)

print(shopping_list.number_of_items())
print(shopping_list.item(1))
print(shopping_list.amount(1))
print(shopping_list.item(2))
print(shopping_list.amount(2))
