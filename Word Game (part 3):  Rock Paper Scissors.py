import random

class WordGame:
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds + 1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            result = self.round_winner(answer1, answer2)

            if result == 1:
                self.wins1 += 1
                print("player 1 won")
            elif result == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                print("TIE")

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class RockPaperScissors(WordGame):                       # Define a subclass that inherits from WordGame
    def __init__(self, rounds: int):                     # Constructor takes number of rounds
        super().__init__(rounds)                         # Call the parent (WordGame) constructor to initialize attributes

    def round_winner(self, player1_word: str, player2_word: str):  # Method to decide who wins the round
        move1 = player1_word.lower()                     # Convert player 1’s input to lowercase for consistency
        move2 = player2_word.lower()                     # Convert player 2’s input to lowercase for consistency

        valid_moves = ["rock", "paper", "scissors"]      # Define the only valid inputs allowed

        # invalid moves
        if move1 not in valid_moves and move2 not in valid_moves:  # If both moves are invalid
            return 0                                    # It's a tie (no valid move)
        elif move1 not in valid_moves:                  # If only player 1’s move is invalid
            return 2                                    # Player 2 automatically wins
        elif move2 not in valid_moves:                  # If only player 2’s move is invalid
            return 1                                    # Player 1 automatically wins

        # same move
        if move1 == move2:                              # If both players chose the same move
            return 0                                    # It's a tie

        # rock-paper-scissors logic
        # rock-paper-scissors logic
        # Rock beats scissors, Scissors beats paper, Paper beats rock
        if (move1 == "rock" and move2 == "scissors") or \
                (move1 == "scissors" and move2 == "paper") or \
                (move1 == "paper" and move2 == "rock"):
            return 1
        else:
            return 2


# Run the game
if __name__ == "__main__":
    p = RockPaperScissors(3)
    p.play()
