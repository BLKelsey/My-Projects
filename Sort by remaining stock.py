def sort_by_remaining_stock(items: list):
   sorted_list = sorted(items, key=lambda item: item[2])    # create a new list sorted by the 3rd value (stock amount) in each tuple, lowest first
   return sorted_list


products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]

print()
for product in sort_by_remaining_stock(products):
    print(f"{product[0]} {product[2]} pcs")