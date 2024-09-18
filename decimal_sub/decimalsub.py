def str_to_int(s):
    
    is_negative = False
    if s[0] == '-':
        is_negative = True
        s = s[1:]  
    
    result = 0
    
    for char in s:
        
        digit = ord(char) - ord('0')  
        result = result * 10 + digit  
    
    return -result if is_negative else result

def decimal_subtraction(a_str, b_str):
    
    a_int = str_to_int(a_str)
    b_int = str_to_int(b_str)
    
    
    return a_int - b_int


a = "200"  
b = "73"   
result = decimal_subtraction(a, b)
print(f"Result of {a} - {b} is: {result}")

