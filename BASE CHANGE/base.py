def base_conversion(text, text_base, output_base):
    # Convert text from the text_base to a decimal (base 10) integer
    decimal_value = int(text, text_base)
    
    # Convert the decimal value to the desired output_base
    if output_base == 10:
        return str(decimal_value)
    
    output_value = ''
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    while decimal_value > 0:
        remainder = decimal_value % output_base
        output_value = digits[remainder] + output_value
        decimal_value //= output_base
    
    return output_value or '0'

# Example usage:
print(base_conversion("1010", 2, 10))  # Output: "10" (binary "1010" to decimal)
print(base_conversion("A", 16, 2))     # Output: "1010" (hex "A" to binary)
print(base_conversion("10", 10, 16))   # Output: "A" (decimal "10" to hex)

           
