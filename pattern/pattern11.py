def pyramid_pattern(n):
    m = n * 2
    mid = n 

    # Top of Pyramid
    for i in range(mid):
        for j in range(mid - i):
            print(" ", end="")

        for j in range(n - i, n + i + 1):
            if j == n - i or j == n + i:
                print("*", end="")
            else:
                print(" ", end="")

        print()

    # Middle line 
    for j in range(0, n * 2 + 1):
        if j == 0 or j == n * 2 - 1:
            print("*", end="")
        elif j == n:
            print(f"{n}", end="")
        else:
            print(" ", end="")

    print()

    # Bottom Pattern 
    for i in range(mid + 1, m):
        for j in range(i - mid):
            print(" ", end="")
        for j in range(i - n, m - (i - n) + 1):
            if j == i - n or j == m - (i - n):
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Bottom n lines
    for i in range(n):
        for j in range(m + 1):
            print("*", end="")

        print()

# Function to get user input and print the pattern
def print_pattern():
    try:
        n = int(input("Enter a number (1, 2, or 3): "))
        if n in [1, 2, 3]:
            print(f"Pattern for n = {n}:\n")
            pyramid_pattern(n)
        else:
            print("Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


print_pattern()

