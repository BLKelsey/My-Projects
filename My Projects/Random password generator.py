import random

# from Lengths import lengths

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%&+^"

all_letters = letters + numbers + symbols

length = input("Enter the desired length of your password: ")
length = int(length)
password = ""

for i in range(length):
    password += random.choice(all_letters)

print(password)