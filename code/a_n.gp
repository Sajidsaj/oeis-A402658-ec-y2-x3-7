\\ PARI/GP: a(n) for A399358(n) <= 4550  (p = 7 excluded: the curve is singular there)
forprime(p=5, 4550, if(p!=7, my(N=ellcard(ellinit([0,7], p))); if(isprime(N), print1(N", "))))
