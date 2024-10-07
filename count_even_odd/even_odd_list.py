def extract_numbers(l):
    numbers = set()  
    for elem in l:
        if isinstance(elem, int):  
            numbers.add(elem)
        elif isinstance(elem, str) and elem.isdigit():  
            numbers.add(int(elem))
        elif isinstance(elem, tuple):  
            numbers.update(extract_numbers(elem))
    return numbers

def count_odd_even(l):
    numbers = extract_numbers(l)  
    
    odd_count = 0
    even_count = 0

    for num in numbers:
        if num % 2 == 0:  # Check if the number is even
            even_count += 1
        else:  # Otherwise, it's odd
            odd_count += 1

    return odd_count, even_count

# Test input
test_list = [10, "5", (1, 2, 3), "100", 20, 30, (40, 50, "60"), "7", (8, "9", 4)]

# Calling the function to count odd and even numbers
odd_count, even_count = count_odd_even(test_list)

# Print the results
print(f"Odd Count: {odd_count}")    
print(f"Even Count: {even_count}")  #

