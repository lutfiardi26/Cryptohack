def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        d, x, y = extended_gcd(b, a % b)
        return (d, y, x - y * (a // b))

p = 26513
q = 32321

gcd_pq, u, v = extended_gcd(p, q)

print(f"The integers u and v for p * u + q * v = gcd(p, q) are u = {u}, v = {v}")
print(f"The gcd(p, q) is {gcd_pq}")

# Take the lower of u and v as the flag
flag = min(u, v)
print(f"The flag is {flag}")
