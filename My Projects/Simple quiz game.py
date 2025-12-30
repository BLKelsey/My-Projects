score = 0                                               # Initializes the score counter to track correct answers

questions = [                                           # List containing all quiz questions
    "Which freezes faster, cold or hot water?",
    "How many stars are on the American flag?",
    "What is the capital of France?",
    "What's the world's largest living bird?",
    "The pyramids, Sphinx and Nile River can all be found in what country?",
    "Which ocean separates North America and Europe?",
    "What civil rights activist refused to give up her seat on a Montgomery bus?",
    "Which ship sank in 1912?",
    "What is the main ingredient in guacamole?",
    "What sign did God show Noah to promise he would never again flood the world?",
    "Whose wife was turned into a pillar of salt after she turned to look back at the destruction of Sodom?",
    "Romeo and Juliet was written by who?"
]

answers = [                                             # List containing the correct answers in the same order as the questions
    "hot",
    "50",
    "Paris",
    "ostrich",
    "Egypt",
    "Atlantic",
    "Rosa Parks",
    "Titanic",
    "avocado",
    "rainbow",
    "Lot",
    "Shakespeare"
]

for i in range(len(questions)):                         # Loops through each question using its index
    print(questions[i])                                 # Displays the current question
    user_guess = input("What's your guess? ").lower()   # Gets the user’s answer and converts it to lowercase

    if user_guess == answers[i]:                        # Checks if the user’s answer matches the correct answer
        score += 1                                      # Increases the score for a correct answer
        print("Congratulations, you got it!\n")         # Confirms the correct response
    else:
        print("Sorry, that's incorrect.\n")             # Informs the user the answer was wrong

print("You completed the quiz!")                        # Indicates the quiz has ended
print("Your score was:", score)
