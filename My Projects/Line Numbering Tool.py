line_number = 1
with open("Line numbers.txt", "r") as file:
    title = file.readline().strip()     # Read the first line as the title
    print()
    print(title)                        # Print title without a number
    print()

    for line in file:                             # Start numbering the remaining lines
        print(line_number, ":", line.strip())     # Print the line number and the text, removing extra newline spaces
        line_number += 1                          # Increase the line count by 1 each time
