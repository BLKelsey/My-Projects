import json

def print_persons(filename: str):
    # Open the JSON file
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)  # Parse JSON into a Python list of dictionaries

    # Loop through each person in the list
    for person in data:
        name = person['name']
        age = person['age']
        hobbies = person['hobbies']

        # Build the hobbies text manually
        hobbies_text = ""
        for i in range(len(hobbies)):
            hobbies_text = hobbies_text + hobbies[i]
            # Add comma and space if not the last hobby
            if i < len(hobbies) - 1:
                hobbies_text = hobbies_text + ", "

        # Print the result
        print(name, str(age) + " years", "(" + hobbies_text + ")")


# ✅ Call the function OUTSIDE the function body
print()
print_persons("students.json")
