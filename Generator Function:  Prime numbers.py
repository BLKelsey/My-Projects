# Write a generator function prime_numbers() which creates a new generator.
# The generator returns prime numbers one at a time, starting from 2.
# The generator never terminates.

def prime_numbers():                        # Define a generator function
    current_num = 2                         # Start checking numbers from 2

    while True:                             # Infinite loop so the generator never ends
        is_prime = True                     # Assume current_num is prime

        for num in range(2, current_num):   # Test divisibility from 2 up to current_num - 1
            if current_num % num == 0:       # If divisible by any number
                is_prime = False             # It is not a prime
                break                        # Stop checking further

        if is_prime:                         # If no divisors were found
            yield current_num                # Yield the prime number and pause execution

        current_num += 1                    # Move to the next number to test

if __name__ == '__main__':                   # Run the code below only if file is executed directly
    prime = prime_numbers()                  # Create a generator object
    for i in range(8):                       # Request the first 8 prime numbers
        print(next(prime))                   # Get and print the next prime number
