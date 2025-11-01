class ShoppingList:
    def __init__(self):
        self.items = []  # holds a list of product objects (each with name and amount)

    def add(self, name, amount):

        # type('Product', (), {...}) → Dynamically creates a temporary class named "Product".
        # The empty parentheses () mean it has no parent class.        #
        # The dictionary {'name': name, 'amount': amount} sets the attributes for that class.
        # The trailing () → Instantiates that new class immediately — creates one “Product” object.
        self.items.append(type('Product', (), {'name': name, 'amount': amount})())

    def __iter__(self):
        # allows iteration over the list (so we can use for-loops and list comprehensions)
        return iter(self.items)


def products_in_shopping_list(shopping_list, amount):
    # returns names of products whose amount is greater than or equal to the given number
    return [product.name for product in shopping_list if product.amount >= amount]


my_list = ShoppingList()              # create a new shopping list
my_list.add("bananas", 10)            # add 10 bananas
my_list.add("apples", 5)              # add 5 apples
my_list.add("alcohol free beer", 24)  # add 24 alcohol-free beers
my_list.add("pineapple", 1)           # add 1 pineapple

print()
print("The shopping list contains at least 8 of the following items:")  # header text

# print each product name that meets the filter condition (amount >= 8)
for product in products_in_shopping_list(my_list, 8):
    print(product)
