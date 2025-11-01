class ComputerGame:
    def __init__(self, name, publisher, year):
        self.name = name
        self.publisher = publisher
        self.year = year

class GameWarehouse:
    def __init__(self):
        self.games = []                          # a list to store ComputerGame objects

    def add_game(self, game):
        self.games.append(game)                  # add the game object to the list

    def list_games(self):
        return self.games                        # return all stored games

class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()                       # call parent constructor (creates self.games)

    def list_games(self):
        old_games = []                           # hold only games before 1990
        for game in self.games:
            if game.year < 1990:
                old_games.append(game)
        return old_games

if __name__ == "__main__":
    museum = GameMuseum()                        # instantiate correctly (with parentheses)
    museum.add_game(ComputerGame("Pacman", "Namco", 1980))
    museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
    museum.add_game(ComputerGame("Unreal Tournament", "Taito", 1989))

    for game in museum.list_games():
        print(game.name)
