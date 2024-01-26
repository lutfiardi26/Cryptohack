# Define the given values
KEY1 = int("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313", 16)
KEY2_XOR_KEY1 = int("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e", 16)
KEY2_XOR_KEY3 = int("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1", 16)
FLAG_XOR_KEYS = int("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf", 16)

# Use properties of XOR to obtain the flag
FLAG = FLAG_XOR_KEYS ^ KEY1 ^ KEY2_XOR_KEY3 ^ KEY2_XOR_KEY1

# Convert the flag from integer to bytes
flag_bytes = FLAG.to_bytes((FLAG.bit_length() + 7) // 8, 'big')

print("Flag (raw bytes):", flag_bytes)
