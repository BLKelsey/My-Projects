line_count = 0

print("Enter the file name:")
file_name = input()                     # GET FILE_NAME

file = open(file_name, "r")             # OPEN FILE_NAME for reading

for line in file:
    line_count += 1

file.close()                            # CLOSE the file

print("Number of lines:", line_count)  # DISPLAY result

