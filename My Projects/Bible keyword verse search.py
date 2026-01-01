from openpyxl import load_workbook
import random
import os

print(os.path.abspath("RefAndScripture.xlsx"))



# Load the Excel file
workbook = load_workbook("RefAndScripture.xlsx")
sheet = workbook.active
print("Sheet name:", sheet.title)

# Ask the user for a keyword
keyword = input("Enter a keyword to search for: ").lower()

matches = []

# Collect matching verses
for row in sheet.iter_rows(min_row=2, values_only=True):
    reference, verse = row

    # Skip empty verse cells
    if verse is None:
        continue

    words = verse.lower().split()

    if keyword in words:
        matches.append(f"{reference} - {verse}")

print("\nSearch results:\n")

# Limit to 10 random verses
if len(matches) > 10:
    matches = random.sample(matches, 10)

# Print results
for result in matches:
    print(result)

print(f"\nTotal verses found: {len(matches)}")
