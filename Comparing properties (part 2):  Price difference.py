class RealProperty:
    def __init__(self, rooms: int, square_foot: int, price_per_sq_ft: int):
        self.rooms = rooms
        self.square_foot = square_foot
        self.price_per_sq_ft = price_per_sq_ft

    def price_difference(self, compared_to):
       total_price_self = self.square_foot * self.price_per_sq_ft
       total_price_other = compared_to.square_foot * compared_to.price_per_sq_ft
       difference = abs(total_price_self - total_price_other)
       return difference

central_studio = RealProperty(1, 16, 5500)
downtown_two_bedroom = RealProperty(2, 38, 4200)
suburbs_three_bedroom = RealProperty(3, 78, 2500)

print()
print(central_studio.price_difference(downtown_two_bedroom))
    # (16*5500) = 88,000 - price of central studio
    # (38*4200) = 159,600 - price of suburbs three bedroom
    # ABS(88,000 - 159,600) = 71,600 - difference in price
print(suburbs_three_bedroom.price_difference(downtown_two_bedroom))
    # (78*2500) = 195,000 - price of suburbs three bedroom
    # (38*4200) = 159,600 - price of central studio
    # ABS(195,000 - 159,600) = 35,400 - difference in price


