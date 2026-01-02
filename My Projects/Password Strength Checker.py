password = input("Enter a password to check: ").strip()

strength_score = 0

# Length check
if len(password) >= 8:
    strength_score += 1

# Lowercase letter check
for char in password:
    if char.islower():
        strength_score += 1
        break

# Uppercase letter check
for char in password:
    if char.isupper():
        strength_score += 1
        break

# Number check
for char in password:
    if char.isdigit():
        strength_score += 1
        break

# Special character check
for char in password:
    if not char.isalnum():
        strength_score += 1
        break

# Strength evaluation
if strength_score == 5:
    print("Password is Strong!")

elif strength_score >= 3:
    print("Password is Medium!")

else:
    print("Password is Weak!")
