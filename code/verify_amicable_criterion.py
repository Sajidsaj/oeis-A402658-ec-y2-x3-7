"""Finite verification of the amicable criterion for E: y^2 = x^3 + 7 (needs only sympy).

Notation: p = 1 (mod 3) prime, p = pi*conj(pi) in Z[w] with pi primary (pi == 2 mod 3),
z(pi) = (28/pi)_6, sigma_p = -conj(z)*pi (Frobenius), #E(GF(p)) = Norm(1 - sigma_p).

Theory (docs/PROOFS.md, Section 5): by quadratic and cubic reciprocity, z(pi) depends only on
pi modulo 84.  Hence it suffices to know z on the 432 primary classes mod 84.
Steps:
 (1) tabulate z on all 432 classes from primes p < 400000 (every class occurs; consistency is checked);
 (2) for each class decide whether #E(GF(q)) = p, where q = #E(GF(p));
 (3) list the resulting pairs (p mod 84, q mod 84) and compare with the criterion in the OEIS entry.
Run time: about one minute.
"""
from math import gcd, isqrt
from sympy import primerange
M = 84
UNITS = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1)]          # a + b*w, w^2 = -1 - w
mul = lambda x, y: (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0] - x[1]*y[1])
conj = lambda x: (x[0] - x[1], -x[1])
norm = lambda x: x[0]*x[0] - x[0]*x[1] + x[1]*x[1]
red = lambda x: (x[0] % M, x[1] % M)
neg = lambda x: (-x[0], -x[1])

def primary_assoc(x):
    for u in UNITS:
        r = mul(u, x)
        if r[0] % 3 == 2 and r[1] % 3 == 0:
            return red(r), u
    raise ValueError(x)

def eisenstein_rep(p):                      # a + b*w with a^2 - a*b + b^2 = p, primary
    for b in range(-isqrt(4*p//3) - 1, isqrt(4*p//3) + 2):
        D = 4*p - 3*b*b
        if D < 0: continue
        s = isqrt(D)
        if s*s != D or (b + s) % 2: continue
        x = ((b + s)//2, b)
        if norm(x) == p:
            for u in UNITS:
                r = mul(u, x)
                if r[0] % 3 == 2 and r[1] % 3 == 0: return r

# ---- (1) learn z on classes mod 84 from primes
F, bad = {}, 0
for p in primerange(13, 400000):
    if p % 3 != 1: continue
    pi = eisenstein_rep(p); a, b = pi
    r = (-a*pow(b, -1, p)) % p              # image of w in GF(p) with pi -> 0
    t = pow(28, (p-1)//6, p)
    z = [u for u in UNITS if (u[0] + u[1]*r) % p == t][0]
    k = (a % M, b % M)
    if F.setdefault(k, z) != z: bad += 1
print("primary classes mod 84 seen: %d (expected 432); inconsistencies: %d" % (len(F), bad))
assert len(F) == 432 and bad == 0
# character property
import random; random.seed(1); ks = list(F)
for _ in range(20000):
    c1, c2 = random.choice(ks), random.choice(ks)
    pc, _ = primary_assoc(mul(c1, c2))
    assert F[pc] == mul(F[c1], F[c2]) or red(F[pc]) == red(mul(F[c1], F[c2]))
print("character property: 20000 random products OK")

# ---- (2),(3) class-level table
pairs, adm, amic = {}, 0, 0
for pi, zp in F.items():
    sigma = neg(mul(conj(zp), pi)); rho = red((1 - sigma[0], -sigma[1]))
    p_, q_ = norm(pi) % M, norm(rho) % M
    if gcd(p_, 84) != 1 or gcd(q_, 84) != 1: continue
    adm += 1
    pq, u = primary_assoc(rho); v = conj(u)                  # rho = v * pi_q
    zq = F[pq]
    am = (zq == neg(conj(v)))                                 # z_q = -v^{-1}
    pairs.setdefault((p_, q_), set()).add(am); amic += am
print("admissible classes: %d, amicable classes: %d" % (adm, amic))
assert all(len(s) == 1 for s in pairs.values())
GOOD = {(43,43),(43,67),(43,73),(61,61),(67,43),(67,79),(73,43),(79,67),(79,79)}
T = {k for k, s in pairs.items() if True in s}
print("amicable (p mod 84, q mod 84) pairs:", sorted(T)); assert T == GOOD
print("matches the criterion in the sequence comment")
