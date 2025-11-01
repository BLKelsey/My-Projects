# Please write a program which asks the user for a positive integer N.
# The program then prints out all numbers between -N and N inclusive, but leaves out the number 0.
# Each number should be printed on a separate line.

num = int(input("Enter a positive integer: "))

for i in range(-num + 1, num):  # Loop starts at -num+1 so that -num is excluded, and stops at num so that +num is excluded too.
    if i == 0:
        continue
    print(i)


