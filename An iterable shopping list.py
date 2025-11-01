class ShoppingList:
    def __init__(self):
        # Initialize an empty list that will hold tuples (item_name, amount)
        self.shopping_list = []

    def add(self, item, amount):
        # Add a new (item, amount) tuple to the shopping list
        self.shopping_list.append((item, amount))

    def __iter__(self):
        # Prepare the object to be iterable by setting a counter
        self.num = 0
        return self  # Return the iterator object itself

    def __next__(self):
        # Called automatically when looping through the object
        if self.num < len(self.shopping_list):
            product = self.shopping_list[self.num]  # Get the next tuple
            self.num += 1  # Move to the next index for the next iteration
            return product  # Return the current (item, amount) tuple
        else:
            # If we've reached the end of the list, stop iteration
            raise StopIteration

# Test program
shopping_list = ShoppingList()  # Create a ShoppingList object
print()  # Blank line (optional, for spacing)

# Add items to the list
shopping_list.add("bananas", 10)
shopping_list.add("apples", 5)
shopping_list.add("pineapple", 1)

# Iterate over the list using a for loop
# Each loop returns one (item, amount) tuple from __next__()
for item, amount in shopping_list:
    print(f"{item}: {amount} units")  # Nicely formatted output
