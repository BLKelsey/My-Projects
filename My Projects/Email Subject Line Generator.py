import random

greetings = [
    "Quick question",
    "Friendly reminder",
    "Just checking in",
    "Important update",
    "Following up"
]

topics = [
    "your recent request",
    "our last conversation",
    "the upcoming meeting",
    "your account",
    "this week's update"
]

endings = [
    "please read",
    "thanks",
    "action needed",
    "for your review",
    "when you have time"
]

greeting = random.choice(greetings)   # pick one random greeting from the greetings list
topic = random.choice(topics)         # pick one random topic from the topics list
ending = random.choice(endings)       # pick one random ending from the endings list

print(f"{greeting}: {topic} — {ending}")  # print the final email subject line

