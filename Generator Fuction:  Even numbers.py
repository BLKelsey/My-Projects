# Write a generator function named even_numbers(beginning: int, maximum: int) which takes two integers as its arguments.
# The function should produce even numbers starting from beginning and ending with, at most, maximum.


def even_numbers(beginning: int, maximum: int):
    current_num = beginning

    while current_num <= maximum:
        if current_num % 2 == 0:
            yield current_num
        current_num += 1


if __name__ == "__main__":
    result = even_numbers(2, 10)
    for number in result:
        print(number)
   # print(next(result))
   # print(next(result))
   # print(next(result))
   # print(next(result))
