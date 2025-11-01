# Please write a program which works as a simply diary. The diary entries should be saved in the file diary.txt.
# When the program is executed, it should first read any entries already in the file.


while True:
    print()
    print("1 - add an entry, 2 - read entries, 0 - quit")
    choice = input("Function: ")

    if choice == "1":
        entry = input("Diary entry: ")
        with open("diary.txt", "a", encoding="utf-8") as diary:  # append entry
            diary.write(entry + "\n")
        print("Diary saved\n")

    elif choice == "2":
        print("Entries:")
        with open("diary.txt", "r", encoding="utf-8") as diary:
            for line in diary:
                print(line.strip())
        print()

    elif choice == "0":
        print("Bye now!")
        break

    else:
        print("Invalid choice, try again.\n")
