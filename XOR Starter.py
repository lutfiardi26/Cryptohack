def xor_string(input_str, key):
    # Convert each character to its ASCII value, XOR with the key, and convert back to character
    result = ''.join(chr(ord(char) ^ key) for char in input_str)
    return result

# Given string
label = "label"

# XOR each character with the integer 13
result = xor_string(label, 13)

# Print the flag format
print("crypto{" + result + "}")