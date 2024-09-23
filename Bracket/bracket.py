def check_validity(text: str) -> str:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '[', '>': '<'}
    open_brackets = set(bracket_map.values())
    close_brackets = set(bracket_map.keys())
    for char in text:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return f"Invalid: Misplaced or unmatched closing bracket '{char}'"
        elif char not in open_brackets and char not in close_brackets:
            return f"Invalid: Contains non-bracket character '{char}'"

    if stack:
        return "Invalid: Unmatched opening bracket(s)"
    
    return "Valid"

def get_valid_invalid_text_count(texts):
    valid_count = 0
    invalid_count = 0

    for text in texts:
        if isinstance(text, str):  # Check if the object is a string
            result = check_validity(text)
            if result == "Valid":
                valid_count += 1
            else:
                invalid_count += 1

    return (valid_count, invalid_count)

texts = ['[{(', 45, '()', '{1}', ')(', '[()]', '<>', '{[()]}', '(abc)', '<<>>']
print(get_valid_invalid_text_count(texts))

