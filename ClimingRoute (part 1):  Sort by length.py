class ClimbingRoute:
    def __init__(self, name, length, grade):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length: {self.length}ft, grade: {self.grade}"

def sort_by_length(routes: list):
        sorted_list = sorted(routes, key=lambda item: item.length)
        return sorted_list

r1 = ClimbingRoute("Edge", 38, "6A+")
r2 = ClimbingRoute("Smooth operator", 11, "7A")
r3 = ClimbingRoute("Synchro", 14, "8C+")
r4 = ClimbingRoute("Small steps", 12, "6A+")

routes = [r1, r2, r3, r4]
print()
for route in sort_by_length(routes):
     print(route)