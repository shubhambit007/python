

def changecase(text, style):
    if style == '-c' or style == '-C':
        return capital(text)
    elif style == '-s'or style == '-S':
        return small(text)
    elif style == '-r'or style == '-R':
        return reverse(text)
    elif style == '-u'or style == '-U':
        return ulter(text)
    else:
        return "Invalid style option"

def ulter(text):
    if not text:
        return text

    first_char = text[0]
    result = first_char
    toggle = first_char.islower()

    for i, char in enumerate(text[1:], start=1):
        if toggle:
            if 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            else:
                result += char
        else:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char
        toggle = not toggle

    return result

def reverse(text):
    if len(text) == 0:
        return text
    char = text[-1]
    if 'a' <= char <= 'z':
        char = chr(ord(char) - 32)
    elif 'A' <= char <= 'Z':
        char = chr(ord(char) + 32)
    return char + reverse(text[:-1])

def small(text):
    result = ''
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def capital(text):
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

print(changecase("HelloWorlD", "-u"))
