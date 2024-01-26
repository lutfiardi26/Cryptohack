encoded_hex =  bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for key in range(256):
    decoded_bytes = [chr(n^key) for n in encoded_hex]
    flag = "".join(decoded_bytes)
    # print(flag)
    if flag.startswith("ap"):
        print(flag)
        print(key)  # So we'll know the magic "single byte"

