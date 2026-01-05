import random

proverbs = [
    "Proverbs 1:7  The fear of the Lord is the beginning of knowledge, but fools despise wisdom and instruction.",
    "Proverbs 3:5-6  Trust in the Lord with all your heart and lean not on your own understanding; in all your ways submit to him, and he will make your paths straight.",
    "Proverbs 4:7  The beginning of wisdom is this: GET WISDOM. Though it cost all you have, GET UNDERSTANDING.",
    "Proverbs 8:11  For wisdom is more precious than rubies, and nothing you desire can compare with her.",
    "Proverbs 9:10  The fear of the Lord is the beginning of wisdom, and knowledge of the Holy One is understanding.",
    "Proverbs 10:12  Hatred stirs up conflict, but love covers over all wrongs.",
    "Proverbs 11:25  A generous person will prosper; whoever refreshes others will be refreshed.",
    "Proverbs 12:25  Anxiety weighs down the heart, but a kind word cheers it up.",
    "Proverbs 13:20  Walk with the wise and become wise, for a companion of fools suffers harm.",
    "Proverbs 14:12 There is a way that appears to be right, but in the end it leads to death.",
    "Proverbs 15:1  A gentle answer turns away wrath, but a harsh word stirs up anger.",
    "Proverbs 15:3  A gentle answer turns away wrath, but a harsh word stirs up anger.",
    "Proverbs 16:3  Commit to the Lord whatever you do, and he will establish your plans.",
    "Proverbs 16:9  In their hearts humans plan their course, but the Lord establishes their steps.",
    "Proverbs 16:18  Pride goes before destruction, a haughty spirit before a fall.",
    "Proverbs 18:10 The name of the Lord is a fortified tower; the righteous run to it and are safe.",
    "Proverbs 18:21  The tongue has the power of life and death, and those who love it will eat its fruit.",
    "Proverbs 19:21  Many are the plans in a person’s heart, but it is the Lord’s purpose that prevails.",
    "Proverbs 21:2  A person may think their own ways are right, but the Lord weighs the heart!",
    "Proverbs 21:21  Whoever pursues righteousness and love finds life, prosperity, and honor.",
    "Proverbs 22:6  Start children off on the way they should go, and even when they are old they will not turn from it.",
    "Proverbs 24:16  For though the righteous fall seven times, they rise again, but the wicked stumble when calamity strikes.",
    "Proverbs 25:21-22  If your enemy is hungry, give him food to eat; if he is thirsty, give him water to drink. In doing this, you will heap burning coals on his head, and the Lord will reward you.",
    "Proverbs 27:17  As iron sharpens iron, so one person sharpens another.",
    "Proverbs 28:13  Whoever conceals their sins does not prosper, but the one who confesses and renounces them finds mercy.",
    "Proverbs 31:30  Charm is deceptive, and beauty is fleeting; but a woman who fears the Lord is to be praised."
   ]
user_choice = "yes"                 # Start the loop by assuming the user wants a proverb

while user_choice == "yes":                    # Keep looping as long as the user types "yes"
    total_proverbs = 26                        # Total number of proverbs in the list
    max_index = total_proverbs - 1             # Highest valid index (lists start at 0)
    random_index = random.randint(0, 25)  # Pick a random index between 0 and 25
    print()
    print(proverbs[random_index])              # Print a random proverb from the list

    print("Do you want another proverb? (yes/no:)")  # Ask the user if they want another
    user_choice = input("> ")       # Get the user's answer




