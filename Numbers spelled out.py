# Please write a function named dict_of_numbers(), which returns a new dictionary.
# The dictionary should have the numbers from 0 to 99 as its keys.
# The value attached to each key should be the number spelled out in words.

from num2words import num2words           # Import the num2words function from the num2words library
                                          # This allows converting numbers into their English word form

def dict_of_numbers():
    spelled = {}                         # Create an empty dictionary to hold the results
    for key in range(100):               # Loop through numbers from 0 up to 99
        spelled[key] = num2words(key)    # Convert the number into words using num2words and store it in the dictionary (key = number, value = word)

    return spelled                       # Return the completed dictionary

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print()
    print('2 spelled is: ',numbers[2])
    print('11 spelled is: ',numbers[11])
    print('45 spelled is: ',numbers[45])
    print('99 spelled is: ',numbers[99])
    print('0 spelled is: ',numbers[0])









