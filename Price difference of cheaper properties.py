class RealProperty:
    def __init__(self, rooms: int, square_foot: int, price_per_sq_ft: int, description):
        self.rooms = rooms
        self.square_foot = square_foot
        self.price_per_sq_ft = price_per_sq_ft
        self.description = description

    @property
    def price(self):  # defines a read-only property called 'price'
               return self.square_foot * self.price_per_sq_ft    # calculates total price by multiplying size by price per square foot


def cheaper_properties(properties: list, reference: RealProperty):  # creates a list of tuples (property, price difference)
    return [(property, reference.price - property.price)
            for property in properties if property.price < reference.price]  # for all properties cheaper than the reference property


a1 = RealProperty(1, 16, 5500, "Central studio")
a2 = RealProperty(2, 38, 4200, "Two bedrooms downtown")
a3 = RealProperty(3, 78, 2500, "Three bedrooms in the suburbs")
a4 = RealProperty(6, 215, 500, "Farm in the middle of nowhere")
a5 = RealProperty(4, 105, 1700, "Loft in a small town")
a6 = RealProperty(25, 1200, 2500, "Countryside mansion")

properties = [a1, a2, a3, a4, a5, a6]
print()
print(f"cheaper options when compared to {a3.description} @ {a3.price_per_sq_ft * a3.square_foot} dollars:")
print()
for item in cheaper_properties(properties, a3):
    print(f"{item[0].description:35} price difference {item[1]} dollars")
