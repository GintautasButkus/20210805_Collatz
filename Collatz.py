# Write a function named collatz() that has one parameter named number.
# If number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.
# Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.

print('This is a Collatz number sequence')

try:
    user = int(input(print('Please enter the number: ')))
except ValueError:
    print('You must enter an integer ')

try:
    def collatz(number):
        print(number)
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                yield number

            elif number % 2 == 1:
                number = 3 * number + 1
                yield number
    print(list(collatz(user)))
except NameError:
    print('')
