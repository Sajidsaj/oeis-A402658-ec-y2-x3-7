# Python + sympy (primes only): the 47 terms with A399358(n) <= 4550.
from sympy import primerange, isprime
def N(p):
    e = (p-1)//2
    return 1 + sum(1 if (r := (x**3+7) % p) == 0 else (2 if pow(r, e, p) == 1 else 0) for x in range(p))
print([n for p in primerange(5, 4551) if p != 7 and isprime(n := N(p))])
