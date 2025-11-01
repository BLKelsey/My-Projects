import random                                         # Import random module for random number generation

class WordGame:                                       # Define a base class for the word game
    def __init__(self, rounds: int):                  # Constructor takes number of rounds
        self.wins1 = 0                                # Track wins for player 1
        self.wins2 = 0                                # Track wins for player 2
        self.rounds = rounds                          # Store how many rounds to play

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)                   # Randomly pick either player 1 or 2 as winner

    def play(self):                                   # Main method to play the game
        print("Word game:")
        for i in range(1, self.rounds + 1):           # Loop through all rounds
            print(f"round {i}")
            answer1 = input("player1: ")              # Ask player 1 for a word
            answer2 = input("player2: ")              # Ask player 2 for a word

            result = self.round_winner(answer1, answer2)  # <--- Call the round_winner method once

            if result == 1:                           # If player 1 wins
                self.wins1 += 1                       # Add one to player 1’s wins
                print("player 1 won")
            elif result == 2:                         # If player 2 wins
                self.wins2 += 1                       # Add one to player 2’s wins
                print("player 2 won")
            else:                                     # If result = 0 (tie)
                print("TIE")                          # Print tie once

        print("game over, wins:")                     # After all rounds, display final results
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):                          # Define subclass inheriting from WordGame
    def __init__(self, rounds: int):                  # Constructor for LongestWord
        super().__init__(rounds)                      # Call parent constructor
        self.wins1 = 0                                # Initialize player 1 wins
        self.wins2 = 0                                # Initialize player 2 wins

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):     # If player 1’s word is longer
            return 1
        elif len(player1_word) < len(player2_word):   # If player 2’s word is longer
            return 2
        else:                                         # If both words are same length
            return 0

p = LongestWord(3)                                   # Create a LongestWord game with 3 rounds
p.play()                                             # Start the game
