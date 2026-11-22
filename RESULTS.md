# Summary of results

Scope: the sequence a(n) = #E(GF(A399358(n))) for E: y² = x³ + 7. Each statement is labelled **proved**
(argument in `docs/PROOFS.md`, relying on quoted textbook theorems) or **computed** (reproducible with the scripts in `code/`).

| Statement | Status |
|---|---|
| Every term of A399358 is a prime p ≡ 1 (mod 3) with 7 a quadratic nonresidue mod p, so p ≡ 13, 43, 61, 67, 73, 79 (mod 84); the point count N satisfies N ≡ 1 (mod 6) | Proved; checked on all 5670 terms below 2·10⁶ |
| a(n) = p + 1 − t with t ≡ 1 (mod 6), t² + 3u² = 4p, u ≠ 0 | Proved |
| For primes q ≡ 1 (mod 6), q > 7, at most two of the six orders of y² = x³ + b over GF(q) are prime (two are even, two are odd multiples of 3) | Proved |
| Duality: A399358(n) is one of the six orders over GF(a(n)); hence each value of a(n) occurs at most twice (76 values occur twice below 2·10⁶; the first are 79, 397, 4597) | Proved; checked |
| a(n) = A399358(n) iff A399358(n) is an anomalous prime (32 below 2·10⁶, the first being 61, 127, 397, 547, 4447, 6211) | Definition; computed |
| Amicable criterion: #E(GF(q)) = p iff (p mod 84, q mod 84) is one of (43,43), (43,67), (43,73), (61,61), (67,43), (67,79), (73,43), (79,67), (79,79) | Proved from cubic and quadratic reciprocity (quoted) plus a finite table over the 432 primary classes mod 84 (`code/verify_amicable_criterion.py`) |
| Below 2·10⁶: 5670 terms, 738 amicable pairs (1476 primes); smallest pairs (67,79), (907,967), (1249,1303) | Computed |
| secp256k1: p = 2²⁵⁶ − 2³² − 977 is a term of A399358; #E(GF(p)) is the prime group order n | Computed (`code/check_secp256k1.py`) |

## Not claimed
* No statement is made about the infinitude of A399358 or its asymptotic density.
* Reciprocity laws and Ireland–Rosen's point-count formula are used as published theorems and are not re-proved.
