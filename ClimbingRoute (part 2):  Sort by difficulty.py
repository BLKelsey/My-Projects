class ClimbingRoute:
    def __init__(self, name, length, grade):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f" Route: {self.name}, length: {self.length}ft, grade: {self.grade}"

def sort_by_difficulty(routes):
    # sorts the routes by each route's 'grade' attribute; 'key=lambda' extracts the grade value for comparison
    # 'reverse=True' arranges them from hardest to easiest (descending order)
    sorted_routes = sorted(routes, key=lambda route: route.grade, reverse=True)
    return sorted_routes

r1 = ClimbingRoute("Edge", 38, "6A+")
r2 = ClimbingRoute("Smooth operator", 11, "7A")
r3 = ClimbingRoute("Synchro", 14, "8C+")
r4 = ClimbingRoute("Small steps", 12, "6A+")

routes = [r1, r2, r3, r4]
for route in sort_by_difficulty(routes):
    print(route)