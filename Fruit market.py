# Please write a function named read_fruits, which reads the file and returns a dictionary based on the contents.
# In the dictionary, the name of the fruit should be the key, and the value should be its price. Prices should be of type float

def read_fruits():
    with open("fruits.txt", encoding="utf-8-sig") as new_file:
        fruits = {}    # create empty dictionary to hold fruit names as keys and their prices as values
        for line in new_file:
            line = line.strip()    # remove leading/trailing spaces and newline characters
            if not line:   # skip empty lines
                continue

            parts = line.split(",")    # use comma as separator
            key = parts[0].strip()           # take the first part (fruit name), remove extra spaces, and save it as the dictionary key
            value = float(parts[1].strip())  # take the second part (price), remove extra spaces, convert it to a float, and save it as the dictionary value
            fruits[key] = value      # add a new entry to the dictionary, using the fruit name as the key and the price as the value
    return fruits


if __name__ == "__main__":
    print()
    print(read_fruits())

