class BallPlayer:
    def __init__(self, name, shirt_number, goals, assists, minutes):
        self.name = name
        self.shirt_number = shirt_number
        self.goals = goals
        self.assists = assists
        self.minutes = minutes

    def total_points(self):
        return self.goals + self.assists

    def most_goals(self, players):
        top_player = players[0]
        for player in players:
            if player.goals > top_player.goals:
                top_player = player
        return top_player

    def most_points(self, players):
        top_player = players[0]
        top_points = players[0].total_points()
        for player in players:
            current_points = player.total_points()
            if current_points > top_points:
                top_player = player
                top_points = current_points
        return top_player

    # Used for "Most Goals:"
    def __str__(self):
        return f"Top Player: {self.name} with {self.goals} goals"

    # Used for "Most Points:"
    def points_str(self):
        total = self.total_points()
        return f"({self.name} {total} points: {self.goals} goals + {self.assists} assists)"

# ---------- TEST PROGRAM ----------

p1 = BallPlayer("Alice", 10, 8, 3, 900)
p2 = BallPlayer("Bob", 7, 12, 4, 1100)
p3 = BallPlayer("Charlie", 9, 5, 6, 800)

players = [p1, p2, p3]

# Most goals (uses __str__)
top_goal_player = p1.most_goals(players)
print("Most Goals:", top_goal_player)

# Most points (uses points_str)
top_point_player = p1.most_points(players)
print("Most Points:", top_point_player.points_str())
