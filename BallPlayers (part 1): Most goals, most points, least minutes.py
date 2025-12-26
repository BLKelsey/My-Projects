class BallPlayer:
    def __init__(self, name, shirt_number, goals, assists, minutes):
        self.name = name
        self.shirt_number = shirt_number
        self.goals = goals
        self.assists = assists
        self.minutes = minutes

    def __str__(self):
        return f"{self.name}: shirt number: ({self.shirt_number}) with only {self.minutes} minutes play time"


def least_minutes(players):
    min_player = players[0]
    min_minutes = min_player.minutes

    for player in players:
        if player.minutes < min_minutes:
            min_player = player
            min_minutes = player.minutes
    return min_player


# ---------- TEST PROGRAM ----------
if __name__ == "__main__":
    player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
    player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
    player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
    player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
    player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)

    team = [player1, player2, player3, player4, player5]
    print(least_minutes(team))
