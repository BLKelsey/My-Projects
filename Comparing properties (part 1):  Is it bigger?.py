class RealProperty:
    def __init__(self, rooms: int, square_foot: int, price_per_sq_ft: int):
        self.rooms = rooms
        self.square_foot = square_foot
        self.price_per_sq_ft = price_per_sq_ft

    def bigger(self,compared_to):
         if self.square_foot > compared_to.square_foot:
             return True
         else:
             return False

central_studio = RealProperty(1, 172, 550)         # 172 square feet
downtown_two_bedroom = RealProperty(2, 410, 420)   # 410 square feet
suburbs_three_bedroom = RealProperty(3, 840, 250)  # 840 square feet

print()
print('Central studio is bigger? ',central_studio.square_foot,'square foot: ',central_studio.bigger(downtown_two_bedroom))         # compares 172 vs 410 → returns False
print('Suburbs three bedrooms bigger? ' ,suburbs_three_bedroom.square_foot,'square foot: ', suburbs_three_bedroom.bigger(downtown_two_bedroom))  # compares 840 vs 410 → returns True
print('Downtown Two Bedroom bigger? ', downtown_two_bedroom.square_foot, 'square foot: ', downtown_two_bedroom.bigger(downtown_two_bedroom))