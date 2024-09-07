def binary_subtraction(a, b):
    # Convert binary strings to lists of integers (bit by bit)
    a = list(a)
    b = list(b)

    # Make both lists the same length by prepending zeros to the shorter one
    while len(a) < len(b):
        a.insert(0, '0')
    while len(b) < len(a):
        b.insert(0, '0')

    # Initialize variables
    result = []
    borrow = 0

    # Perform subtraction from right to left
    for i in range(len(a) - 1, -1, -1):
        bit_a = int(a[i])
        bit_b = int(b[i])

        # Subtract considering borrow
        sub = (bit_a - borrow) - bit_b

        if sub == 0:
            result.append('0')
            borrow = 0
        elif sub == 1:
            result.append('1')
            borrow = 0
        elif sub == -1:
            result.append('1')
            borrow = 1
        elif sub == -2:
            result.append('0')
            borrow = 1

    # Remove leading zeros
    while len(result) > 1 and result[-1] == '0':
        result.pop()

    # Reverse the result and convert it to a string
    return ''.join(reversed(result))

# Example usage:
a = "1100"  # Binary for 13
b = "1010"  # Binary for 10

print("Result of binary subtraction:", binary_subtraction(a, b))  # Output should be 0011 (3 in binary)

