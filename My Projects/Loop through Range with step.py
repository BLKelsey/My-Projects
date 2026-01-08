print("Enter a starting number: ")
start_number = int(input())

print("Enter a stopping number: ")
stop_number = int(input())

print("Enter an increment or decrement step: ")
step_number = int(input())

for i in range(start_number, stop_number, step_number):
    print(i)