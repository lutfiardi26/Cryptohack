def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

print(gcd(26513,32321))