import base64

# Hex string
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Convert hex string to bytes
binary_data = bytes.fromhex(hex_string)

# Encode bytes to Base64
base64_encoded = base64.b64encode(binary_data).decode('utf-8')

# Print the Base64 encoded string
print(base64_encoded)