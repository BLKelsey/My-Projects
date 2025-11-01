import random

def roll(die: str):
    if die == "A":
        sides = [3, 3, 3, 4, 3, 6]
    elif die == "B":
        sides = [1, 2, 2, 5, 5, 5]
    elif die == "C":
        sides = [1, 4, 4, 7, 4, 4]
    
    return random.choice(sides)   # pick one face at random

# run
print()
for i in range(20):
    print(roll("A"), " ", end="")
print()
for i in range(20):
    print(roll("B"), " ", end="")
print()
for i in range(20):
    print(roll("C"), " ", end="")


