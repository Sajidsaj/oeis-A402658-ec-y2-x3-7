# OEIS A402658: points of y² = x³ + 7 over GF(p) when the count is prime

Supporting material for the OEIS sequence [A402658](https://oeis.org/A402658) by Sajid Khan Hussain (companion to [A399358](https://oeis.org/A399358)).

**a(n)** = number of points (including the point at infinity) of the elliptic curve
E: y² = x³ + 7 over GF(p), where p = A399358(n) runs through the primes p ≠ 7 for which this number is prime.

```
7, 31, 61, 79, 67, 79, 127, 139, 199, 313, 397, 397, 547, 613, 691, 829, 967, 907, ...
```

## Contents

| Path | What it is |
|---|---|
| `OEIS_ENTRY.txt` | The text of OEIS A402658 as submitted (name, data, comments, formulas, programs) |
| `CITATION.cff` | Citation metadata |
| `data/b-file.txt` | b-file, n = 1..5670 (A399358(n) < 2·10⁶) |
| `docs/PROOFS.md` | Proofs of all structural claims, including the amicable criterion |
| `RESULTS.md` | One-page summary: what is proved and what is computed |
| `code/verify.py` | Recomputes the b-file and checks every numerical claim in the entry |
| `code/verify_amicable_criterion.py` | Finite table check used in the proof of the amicable criterion |
| `code/check_secp256k1.py` | The secp256k1 prime is a term (prime order, cofactor 1) |
| `code/a_n.gp`, `code/a_n.py` | The PARI/GP and Python programs from the entry |

## Reproduce

```bash
pip install -r requirements.txt   # sympy
python3 code/verify.py 300000     # quick check (about a minute)
python3 code/verify.py            # full check up to 2·10^6 incl. b-file (several minutes)
python3 code/verify_amicable_criterion.py   # amicable criterion table (about a minute)
python3 code/check_secp256k1.py
python3 code/a_n.py               # first 47 terms
gp -q code/a_n.gp                 # same, with PARI/GP
```

## What is proved and what is computed

See `RESULTS.md`. In short: the structural claims and the mod-84 amicable criterion are proved (the latter from cubic and quadratic reciprocity plus a finite table); counts below 2·10⁶ are computed.

## References

* K. Ireland, M. Rosen, *A Classical Introduction to Modern Number Theory*, GTM 84, Ch. 18, §3.
* J. H. Silverman, K. E. Stange, *Amicable pairs and aliquot cycles for elliptic curves*, Exp. Math. 20 (2011), 329–357, [arXiv:0912.1831](https://arxiv.org/abs/0912.1831).

## License

Code: MIT (see `LICENSE`). OEIS text and data: under the OEIS End-User License, i.e. Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0), see https://oeis.org/LICENSE.
