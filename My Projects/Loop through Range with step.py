print("Enter a starting number: ")          # Ask the user where counting should begin
start_number = int(input())                 # Read input and convert it from text to a number

print("Enter a stopping number: ")          # Ask the user where counting should stop
stop_number = int(input())                  # Read input and convert it to a number

print("Enter an increment or decrement step: ")  # Ask how much to increase or decrease each time
step_number = int(input())                       # Read input and convert it to a number

print()

for i in range(start_number, stop_number, step_number):  # Loop through numbers using the step
    print(i)                                            # Display the current number in the loop
