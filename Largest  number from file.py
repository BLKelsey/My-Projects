# Please write a function named largest, which reads the file and returns the largest number in the file.
#
# Notice that the function does not take any arguments. The file you are working with is always named numbers.txt.

def largest():
    with open("numbers.txt", encoding="utf-8-sig") as new_file:   # encoding="utf-8-sig" ensures any hidden BOM marker at the start is ignored
        numbers = []                         # create an empty list to store numbers from the file
        for line in new_file:
            line = line.strip()              # remove leading/trailing spaces and newline characters
            if line:                         #  check that the line is not empty (skip blank lines)
                numbers.append(int(line))    # convert the cleaned line to an int and add it to the list
    return max(numbers)

if __name__ == "__main__":
    print()
    print('The largest number in the file =',largest())                 # call the function and print the largest number in the file




