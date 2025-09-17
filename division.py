# Task
# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines:
#   1. The result of integer division a // b
#   2. The result of float division a / b
# No rounding or formatting is necessary.

if __name__ == '__main__':
    # Read first integer from input
    a = int(input())
    # Read second integer from input
    b = int(input())

    # Print the result of integer division (quotient without remainder)
    print(a // b)

    # Print the result of float division (regular division with decimals)
    print(a / b)
