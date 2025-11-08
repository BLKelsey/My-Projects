class ClimbingRoute:
    def __init__(self, name, length, grade):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} feet, grade {self.grade}"

class ClimbingArea:
    def __init__(self, name):
        self.name = name
        self.routes = []  # holds ClimbingRoute objects

    def add_route(self, route):
        self.routes.append(route)

    def routes_count(self):
        # returns the number of routes in this climbing area
        return len(self.routes)

    def __str__(self):
         # find the longest route and summarize
         longest = max(self.routes, key=lambda route: route.length)
         return f"{self.name}, {len(self.routes)} routes, longest {longest.length} feet"

def sort_by_length(routes: list):
    # Sort routes by their length
    sorted_routes = sorted(routes, key=lambda route: route.length, reverse=True)
    return sorted_routes

r1 = ClimbingRoute("Edge", 38, "6A+")
r2 = ClimbingRoute("Smooth operator", 11, "7A")
r3 = ClimbingRoute("Synchro", 14, "8C+")
r4 = ClimbingRoute("Small steps", 12, "6A+")

routes = [r1, r2, r3, r4]
print()
for route in sort_by_length(routes):
    print(route)
