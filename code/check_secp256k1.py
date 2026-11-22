"""Remark in RESULTS.md: p = 2^256 - 2^32 - 977 (secp256k1) is a term of the sequence A399358.
Checks n*G = infinity for the standard generator G, n prime, n in the Hasse interval; hence #E(GF(p)) = n."""
from math import isqrt
from sympy import isprime
p = 2**256 - 2**32 - 977
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
G = (0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
     0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)
assert (G[1]**2 - G[0]**3 - 7) % p == 0
def add(A, B):
    if A is None: return B
    if B is None: return A
    (x1, y1), (x2, y2) = A, B
    if x1 == x2:
        if (y1 + y2) % p == 0: return None
        l = 3*x1*x1*pow(2*y1, -1, p) % p
    else:
        l = (y2 - y1)*pow(x2 - x1, -1, p) % p
    x3 = (l*l - x1 - x2) % p
    return (x3, (l*(x1 - x3) - y1) % p)
R, B, k = None, G, n
while k:
    if k & 1: R = add(R, B)
    B = add(B, B); k >>= 1
assert isprime(p) and isprime(n) and R is None
assert abs(p + 1 - n) < 2*isqrt(p) + 1     # Hasse
print("OK: p prime, n prime, n*G = infinity, |p+1-n| <= 2 sqrt(p)  =>  #E(GF(p)) = n  (prime, cofactor 1)")
