import time

print("Enter the source file name:")
source_file_name = input()

print("Enter the destination file name:")
destination_file_name = input()

source_file = open(source_file_name, "r")
destination_file = open(destination_file_name, "w")

for line in source_file:
    destination_file.write(line)
time.sleep(3)
print("File copied successfully!")
