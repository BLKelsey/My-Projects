class ClimbingRoute:
    def __init__(self, name, length, grade):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

class ClimbingArea:
    def __init__(self, name):
        self.name = name
        self.routes = []  # holds ClimbingRoute objects

    def add_route(self, route):
        self.routes.append(route)

    def routes_count(self):
        # returns the number of routes in this climbing area
        return len(self.routes)

    def hardest_route(self):
        # returns the hardest route (based on grade)
        return max(self.routes, key=lambda route: route.grade)

    def __str__(self):
        # find the hardest route and summarize
        hardest = max(self.routes, key=lambda route: route.grade)
        return f"{self.name}, {len(self.routes)} routes, hardest {hardest.grade}"

ca1 = ClimbingArea("Olhava")
ca1.add_route(ClimbingRoute("Edge", 38, "6A+"))
ca1.add_route(ClimbingRoute("Great cut", 36, "6B"))
ca1.add_route(ClimbingRoute("Swedish route", 42, "5+"))

ca2 = ClimbingArea("Nummi")
ca2.add_route(ClimbingRoute("Synchro", 14, "8C+"))

ca3 = ClimbingArea("Nalkkila slab")
ca3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
ca3.add_route(ClimbingRoute("Smooth operator", 9, "7A"))
ca3.add_route(ClimbingRoute("Piggy not likey", 12, "6B+"))
ca3.add_route(ClimbingRoute("Orchard", 8, "6A"))

print(ca1)
print(ca3.name, ca3.routes_count())
print(ca3.hardest_route())
