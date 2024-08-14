def pattern(n):
    m = n * 2
    mid = n

    # Top of Pyramid
    for i in range(mid):
        for j in range(mid - i):
            print(" ", end="")

        for j in range(n - i, n + i + 1):
            if (j == n - i) or (j == n + i):
                print("+", end="")
            else:
                print(" ", end="")

        print()

    # Middle line 
    for j in range(0, n * 2 + 1):
        if (j == 0) or (j == n * 2):
            print("+", end="")
        elif j == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

    # Bottom Pattern 
    for i in range(mid + 1, m):
        for j in range(i - mid):
            print(" ", end="")
        for j in range(i - n, m - (i - n) + 1):
            if j == i - n or j == m - (i - n):
                print("-", end="")
            else:
                print(" ", end="")
        print()

    # Bottom line
    for j in range(0, n * 2 + 1):
        if j == n:
            print("-", end="")
        else:
            print(" ", end="")
    print()

    return ""

def print_pattern(length):
    if length <= 0:
        return "Enter a positive number"

    if not float(length).is_integer():
        return "Enter a positive integer"
    
    # Convert length to integer
    length = int(length)

    # Adjust the pattern to match the desired output
    pattern(length)

    return ""

# Test the function with the given example
print(print_pattern(1))  # Output with 3+ at top and 1- at bottom
print(print_pattern(2))  # Output with 5+ at top and 3- at bottom
print(print_pattern(3))  # Output with 7+ at top and 5- at bottom

