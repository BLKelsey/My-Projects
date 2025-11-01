class RealProperty:
    def __init__(self, rooms: int, square_foot: int, price_per_sq_ft: int):
        self.rooms = rooms
        self.square_foot = square_foot
        self.price_per_sq_ft = price_per_sq_ft

    def more_expensive(self, compared_to):
       total_price_self = self.square_foot * self.price_per_sq_ft
       total_price_other = compared_to.square_foot * compared_to.price_per_sq_ft
       if total_price_self > total_price_other:
           return True
       else:
           return False

central_studio = RealProperty(1, 16, 5500)
downtown_two_bedroom = RealProperty(2, 38, 4200)
suburbs_three_bedroom = RealProperty(3, 78, 2500)

print()
print('Is central studio more expensive? ',central_studio.more_expensive(downtown_two_bedroom))
print('Is the two bedroom more expensive? ',downtown_two_bedroom.more_expensive(downtown_two_bedroom))
print('Is the three bedrooms more expensive? ',suburbs_three_bedroom.more_expensive(downtown_two_bedroom))
