import os                                   # Allows interaction with the operating system (files & folders)


def clean_input():                          # Tool 1: Cleans messy user text
    print("\n--- Input Cleaner ---")        # Section header
    text = input("Paste your messy text here:\n")  # Get raw text from user

    cleaned = " ".join(text.split())        # Remove extra spaces and newlines
    print("\nCleaned text:")
    print(cleaned)                          # Display cleaned result


def make_banner():                                          # Tool 2: Generates ASCII text banner
    print("\n--- Program Banner Generator ---")
    text = input("Enter text for banner: ").upper()         # Convert text to uppercase

    banner = {                                              # Dictionary mapping letters to ASCII art
        'A': "  AA   \n A  A  \nAAAAA  \nA   A  \nA   A  ",
        'B': "BBB   \nB  B  \nBBB   \nB  B  \nBBB   ",
        'C': " CCC  \nC     \nC     \nC     \n CCC  ",
        'D': "DDD   \nD  D  \nD  D  \nD  D  \nDDD   ",
        'E': "EEEEE \nE     \nEEE   \nE     \nEEEEE ",
        'F': "FFFFF \nF     \nFFF   \nF     \nF     ",
        'G': " GGG  \nG     \nG  GG \nG   G \n GGG  ",
        'H': "H   H \nH   H \nHHHHH \nH   H \nH   H ",
        'I': "IIIII \n  I   \n  I   \n  I   \nIIIII ",
        'J': "  JJJ \n   J  \n   J  \nJ  J  \n JJ   ",
        'K': "K  K  \nK K   \nKK    \nK K   \nK  K  ",
        'L': "L     \nL     \nL     \nL     \nLLLLL ",
        'M': "M   M \nMM MM \nM M M \nM   M \nM   M ",
        'N': "N   N \nNN  N \nN N N \nN  NN \nN   N ",
        'O': " OOO  \nO   O \nO   O \nO   O \n OOO  ",
        'P': "PPP   \nP  P  \nPPP   \nP     \nP     ",
        'Q': " QQQ  \nQ   Q \nQ   Q \nQ  Q  \n QQQQ ",
        'R': "RRR   \nR  R  \nRRR   \nR R   \nR  R  ",
        'S': " SSS  \nS     \n SSS  \n    S \nSSS   ",
        'T': "TTTTT \n  T   \n  T   \n  T   \n  T   ",
        'U': "U   U \nU   U \nU   U \nU   U \n UUU  ",
        'V': "V   V \nV   V \nV   V \n V V  \n  V   ",
        'W': "W   W \nW   W \nW W W \nWW WW \nW   W ",
        'X': "X   X \n X X  \n  X   \n X X  \nX   X ",
        'Y': "Y   Y \n Y Y  \n  Y   \n  Y   \n  Y   ",
        'Z': "ZZZZZ \n   Z  \n  Z   \n Z    \nZZZZZ ",
        ' ': "      \n      \n      \n      \n      ",
    }

    lines = [""] * 5                        # Prepare 5 output lines (banner height)

    for char in text:                       # Process each character in input
        if char in banner:                  # If character has ASCII art
            art_lines = banner[char].split('\n')
            for i in range(5):
                lines[i] += art_lines[i] + "  "  # Append each row of the letter
        else:
            for i in range(5):
                lines[i] += "      " + "  "      # Placeholder for unknown characters

    print("\nYour Banner:")
    for line in lines:
        print(line)                         # Print final banner line by line


def check_file():                           # Tool 3: Checks if file or folder exists
    print("\n--- File Existence Checker ---")
    path = input("Enter file or folder path: ")

    if os.path.exists(path):                # Check if path exists
        if os.path.isfile(path):            # Check if it is a file
            print("✓ File exists!")
        else:
            print("✓ Directory exists!")
    else:
        print("✗ Path does not exist.")


def number_converter():                    # Tool 4: Converts numbers
    print("\n--- Number Converter (Decimal ↔ Binary) ---")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    choice = input("Choose (1 or 2): ")

    if choice == "1":
        num = int(input("Enter decimal number: "))
        print("Binary:", bin(num)[2:])      # Convert decimal to binary
    elif choice == "2":
        binary = input("Enter binary number: ")
        print("Decimal:", int(binary, 2))   # Convert binary to decimal


def even_odd_checker():                    # Tool 5: Checks even or odd
    print("\n--- Even or Odd Checker ---")
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")


# Main Menu Loop
while True:
    print("\n" + "=" * 40)                  # Menu divider
    print("     BEGINNER TOOLKIT APP")
    print("=" * 40)
    print("1. Input Cleaner")
    print("2. Program Banner Generator")
    print("3. File Existence Checker")
    print("4. Number Converter")
    print("5. Even/Odd Checker")
    print("6. Exit")

    choice = input("\nChoose a tool (1-6): ")  # Get user choice

    if choice == "1":
        clean_input()                      # Run Input Cleaner
    elif choice == "2":
        make_banner()                     # Run Banner Generator
    elif choice == "3":
        check_file()                      # Run File Checker
    elif choice == "4":
        number_converter()                # Run Number Converter
    elif choice == "5":
        even_odd_checker()                # Run Even/Odd Checker
    elif choice == "6":
        print("Goodbye! Keep coding! 🚀") # Exit message
        break                             # Stop the loop and program
    else:
        print(" X - Invalid choice. Try again.")  # Handle invalid input


