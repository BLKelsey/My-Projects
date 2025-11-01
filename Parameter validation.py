def new_person(name: str, age: int):
    # Check that name is not empty
    if not name.strip():
        raise ValueError("Name cannot be empty")

    # Check that name has at least two words
    if len(name.strip().split()) < 2:
        raise ValueError("Name must contain at least two words")

    # Check that name is not too long
    if len(name) > 40:
        raise ValueError("Name cannot be longer than 40 characters")

    # Check that age is between 0 and 150
    if age < 0 or age >= 150:
        raise ValueError("Age must be between 0 and 100")

    # If all checks pass, return a tuple (name, age)
    return (name, age)

#print(new_person("Paul Paulson", 37))                # valid → ('Paul Paulson', 37)
#print(new_person("A B", 150))                        # would raise ValueError: age over 100
#print(new_person("", 30))                            # would raise ValueError: blank name
print(new_person("Paul", 30))               # would raise ValueError: must contain two words
#print(new_person("John Doe", 200))                   # would raise ValueError: age over 100



