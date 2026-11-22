#!/usr/bin/env python3
"""
Independent verification of the sequence and of every numerical claim made in
OEIS_ENTRY.txt.   E: y^2 = x^3 + 7.

Usage:  python3 code/verify.py [LIMIT]      (default LIMIT = 2000000, a few minutes)
Needs:  sympy   (pip install sympy)

Method: for a prime p = 1 (mod 6), write p = a^2 + 3 b^2 (Cornacchia).  The six
possible Frobenius traces of the curves y^2 = x^3 + c over GF(p) are
+-2a, +-(a+3b), +-(a-3b).  The true one is the unique candidate N = p+1-t that
annihilates several random points of E(GF(p)); the (rare) ambiguous cases for
small p are settled by brute-force point counting.
"""
import sys, math, random, os
from collections import Counter
from sympy import primerange, isprime, sqrt_mod

LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
HERE = os.path.dirname(os.path.abspath(__file__))

def brute(p):
    c = 1
    for x in range(p):
        r = (x**3 + 7) % p
        c += 1 if r == 0 else (2 if pow(r, (p-1)//2, p) == 1 else 0)
    return c

def cornacchia(p):                     # p = a^2 + 3 b^2
    r = sqrt_mod(-3, p)
    a, b = p, (r if r <= p//2 else p - r)
    while b*b > p: a, b = b, a % b
    s = p - b*b; c = math.isqrt(s//3); assert 3*c*c == s
    return b, c

def add(P, Q, p):
    if P is None: return Q
    if Q is None: return P
    (x1, y1), (x2, y2) = P, Q
    if x1 == x2:
        if (y1+y2) % p == 0: return None
        l = 3*x1*x1*pow(2*y1, -1, p) % p
    else:
        l = (y2-y1)*pow(x2-x1, -1, p) % p
    x3 = (l*l - x1 - x2) % p
    return (x3, (l*(x1-x3) - y1) % p)

def mul(k, P, p):
    R = None
    while k:
        if k & 1: R = add(R, P, p)
        P = add(P, P, p); k >>= 1
    return R

def rand_point(p):
    while True:
        x = random.randrange(p); r = (x**3 + 7) % p
        if r and pow(r, (p-1)//2, p) == 1: return (x, sqrt_mod(r, p))

def order(p):                          # #E(GF(p)), p = 1 mod 6, p != 7
    a, b = cornacchia(p)
    ts = {2*a, -2*a, a+3*b, -(a+3*b), a-3*b, -(a-3*b)}
    cand = [p+1-t for t in ts]
    for k in (4, 40):
        pts = [rand_point(p) for _ in range(k)]
        cand = [n for n in cand if all(mul(n, P, p) is None for P in pts)]
        if len(cand) == 1: return cand[0]
    return brute(p)

for p in primerange(13, 800):
    if p % 6 == 1: assert order(p) == brute(p), p
print("fast point counting validated against brute force (p < 800)")

# p = 2 (mod 3): supersingular, #E = p+1 even and > 2, never prime.  p = 2, 3, 7: singular.
P, Q = [], []
for p in primerange(5, LIMIT):
    if p % 6 != 1 or p == 7: continue
    n = order(p)
    if isprime(n): P.append(p); Q.append(n)
print(f"terms with A399358(n) < {LIMIT}: {len(Q)}")

def check(name, ok):
    print(("PASS  " if ok else "FAIL  ") + name); assert ok

bf = os.path.join(HERE, "..", "data", "b-file.txt")
if os.path.exists(bf) and LIMIT == 2_000_000:
    rows = [tuple(map(int, l.split())) for l in open(bf)]
    check("b-file matches (n = 1..%d)" % len(rows), rows == list(zip(range(1, len(Q)+1), Q)))
data47 = [7,31,61,79,67,79,127,139,199,313,397,397,547,613,691,829,967,907,1009,1093,1279,1303,1249,1663,1753,2143,2089,2341,2203,2557,2677,2647,2689,3373,3391,3433,3469,3709,3793,3853,3739,4021,4243,4159,4447,4597,4597]
check("Data section (47 terms)", Q[:47] == data47)
check("programs' bound 4550 gives exactly 47 terms", P[46] <= 4550 < P[47])
check("all terms prime and == 1 (mod 6)", all(isprime(q) and q % 6 == 1 for q in Q))
check("t = p+1-a(n) == 1 (mod 6) for all n", all((p+1-q) % 6 == 1 for p, q in zip(P, Q)))
check("|a(n)-p-1| < 2 sqrt(p)", all(abs(q-p-1) < 2*math.sqrt(p) for p, q in zip(P, Q)))
cnt = Counter(Q)
check("each value occurs at most twice", max(cnt.values()) == 2)
idx = lambda v: [i+1 for i, x in enumerate(Q) if x == v]
check("79=a(4)=a(6), 397=a(11)=a(12), 4597=a(46)=a(47)", idx(79) == [4,6] and idx(397) == [11,12] and idx(4597) == [46,47])
check("first repeated values are 79, 397, 4597", sorted(v for v, c in cnt.items() if c == 2)[:3] == [79, 397, 4597])
an = [p for p, q in zip(P, Q) if p == q]
check("anomalous primes 61,127,397,547,4447,6211,...", an[:6] == [61,127,397,547,4447,6211])
Pq = dict(zip(P, Q))
pairs = {frozenset((p, q)) for p, q in zip(P, Q) if p != q and Pq.get(q) == p}
if LIMIT == 2_000_000:
    check("5670 terms, 32 anomalous, 738 pairs, 1476 terms in pairs",
          len(Q) == 5670 and len(an) == 32 and len(pairs) == 738 and sum(len(s) for s in pairs) == 1476)
check("smallest pairs (67,79),(907,967),(1249,1303)", sorted(tuple(sorted(s)) for s in pairs)[:3] == [(67,79),(907,967),(1249,1303)])
allowed = {(43,43),(43,67),(43,73),(61,61),(67,43),(67,79),(73,43),(79,67),(79,79)}
yes = {(p % 84, q % 84) for p, q in zip(P, Q) if 13 < p and q < LIMIT and Pq.get(q) == p}
no  = {(p % 84, q % 84) for p, q in zip(P, Q) if 13 < p and q < LIMIT and Pq.get(q) != p}  # q < LIMIT: a(q) is known
check("residue table: every amicable class is in the proved list, no listed class is non-amicable", yes <= allowed and not (no & allowed))
if LIMIT >= 300_000:
    check("all nine classes of the criterion actually occur", yes == allowed)
print("\nAll checks passed.")
