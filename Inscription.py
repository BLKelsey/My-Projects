# Please write a program which asks for the name of the user and then creates an "inscription" in a file specified by the user.


# Ask user for their name and file location
print()
name = input("Who  should I sign this to? ")
location = input("Where shall it be saved? ")

# Open the file with the user-specified name
with open(location, "w") as file:
    file.write(f"Hi {name}, we hope you enoy learing Python with us!\n")   # write the name into the file

# Print greeting using the variable value
print(f"Hi, {name}, we hope you enjoy learning Python with us was written to Inscription.txt!")


