votes = {}                                           # Creates an empty dictionary to store candidate names and vote counts

while True:                                          # Starts a loop that keeps accepting votes
    name = input("Enter candidate name (or q to stop): ")  # Prompts the user to enter a candidate name or quit

    if name == 'q':                                  # Checks if the user wants to stop voting
        break                                       # Exits the loop

    if name in votes:                               # Checks if the candidate already has votes
        votes[name] += 1                            # Increases the existing vote count by one
    else:
        votes[name] = 1                             # Adds the candidate to the dictionary with one vote

print()                                             # Prints a blank line for readability
print("Voting results: ")                           # Displays a header for the results

for name in votes:                                  # Loops through each candidate in the dictionary
    print(name, ":", votes[name])                   # Prints the candidate name and their total votes
