email = input("Enter your email: ")

# Split the email into two parts using the @ symbol
# Everything before @ goes into 'username'
# Everything after @ goes into 'domain'
username, domain = email.split("@")

# Keep the first 2 characters of the username visible
visible_part = username[:2]

# Calculate how many characters need to be hidden
# This is the total length of the username minus the 2 visible characters
hidden_length = len(username) - 2

# Create a string of "*" characters to hide the rest of the username
masked_part = "*" * hidden_length

# Combine everything back into a masked email
# visible letters + stars + @ + domain
masked_email = visible_part + masked_part + "@" + domain

# Display the final masked email to the user
print("Masked email:", masked_email)
