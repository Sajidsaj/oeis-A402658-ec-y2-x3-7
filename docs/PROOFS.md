# Proofs of the structural claims

Throughout, $E_b : y^2 = x^3 + b$, and $E = E_7$. Let $p \ge 5$ be a prime, $p \ne 7$, and
$N_b(p) = \#E_b(\mathbb{F}_p)$ (point at infinity included). Put $\omega = e^{2\pi i/3}$.

Everything in Sections 1–4 is a proof. Section 5 lists observations that are **only verified by computer**.

## 0. Standard input (Ireland–Rosen, Ch. 18, §3)

**Fact 0.** If $p \equiv 2 \pmod 3$ then $N_b(p) = p+1$. If $p \equiv 1 \pmod 3$, write $p = \pi\bar\pi$ in $\mathbb{Z}[\omega]$
with $\pi \equiv 2 \pmod 3$. Then
$$N_b(p) = p + 1 + \overline{\left(\tfrac{4b}{\pi}\right)_6}\,\pi + \left(\tfrac{4b}{\pi}\right)_6\bar\pi ,$$
and as $b$ runs through $\mathbb{F}_p^*$ the sextic symbol takes each of the six values $\zeta^k$ (sixth roots of unity) equally often.
Hence the six isomorphism classes of curves $E_b$ over $\mathbb{F}_p$ have $N = p+1-t$ with
$t \in \{\operatorname{Tr}(\zeta\pi) : \zeta^6 = 1\}$, a set of six traces.

Write $\pi = x + y\omega$ ($x,y\in\mathbb{Z}$, $p = x^2 - xy + y^2$). Using $\operatorname{Tr}(\omega)=\operatorname{Tr}(\omega^2) = -1$:
$$\operatorname{Tr}(\pi)=2x-y,\quad \operatorname{Tr}(\omega\pi) = -x-y,\quad \operatorname{Tr}(\omega^2\pi) = -x+2y,$$
and the six traces are $\pm t_1, \pm t_2, \pm t_3$ with these three values; $t_1+t_2+t_3 = 0$.

**Lemma 1 (all solutions of $t^2+3u^2 = 4q$ are traces).** For a prime $q\equiv 1 \pmod 3$, every integer solution of $t^2 + 3u^2 = 4q$
has $t \equiv u \pmod 2$, so $(t + u\sqrt{-3})/2 \in \mathbb{Z}[\omega]$ has norm $q$, i.e. it is a unit times $\pi_q$ or $\bar\pi_q$. Therefore $t$ is one of the six traces above.
(Conversely each trace has such a representation: $4q = t^2+3u^2$ is the norm identity for $\zeta\pi_q$.) $\square$

## 1. $t \equiv 1 \pmod 6$ and $a(n) \equiv 1 \pmod 6$

Let $p \equiv 1 \pmod 6$, $N = p+1-t$ prime, $N>3$.

* *Mod 2.* $p+1$ is even, so $N$ odd $\iff$ $t$ odd.
* *Mod 3.* From the formulas, $t_1 \equiv t_2 \equiv t_3 \equiv -(x+y) \pmod 3$ (since $2 \equiv -1$). If $x+y \equiv 0$ then $p = x^2-xy+y^2 \equiv 3x^2 \equiv 0 \pmod 3$, impossible. So all six traces are $\equiv \pm c$ with $c \not\equiv 0 \pmod 3$: three are $\equiv 1$, three are $\equiv 2$. Since $N \equiv 2 - t \pmod 3$, $3 \mid N$ exactly for the three traces $\equiv 2$.

If $N$ is prime ($>3$) then $t$ is odd and $t\equiv 1 \pmod 3$, i.e. $t \equiv 1 \pmod 6$, and $N = p+1-t \equiv 1+1-1 \equiv 1 \pmod 6$. Also $t^2+3u^2 = 4p$ forces $u \ne 0$ ($4p$ is not a square), and Hasse gives $|t| < 2\sqrt p$ (strict since $4p$ is not a square). Thus every term of the sequence is a prime $\equiv 1 \pmod 6$, and the second formula of the entry holds. $\square$

## 2. Among the six twists over $\mathbb{F}_q$, at most two orders are prime ($q>7$)

Let $q \equiv 1 \pmod 6$ be prime, $q > 7$, and let $N_1,\dots,N_6 = q+1-t$ be the six orders (Section 0).

* *Parity.* $(t_1,t_2,t_3) \equiv (y,\ x+y,\ x) \pmod 2$. Since $q = x^2-xy+y^2$ is odd, $x,y$ are not both even, so exactly **two** of $x,y,x+y$ are odd and one is even. So exactly one pair $\pm t_i$ is even: **two** of the six orders are even. They exceed 2 because $N \ge q+1-2\sqrt q > 2$.
* *Mod 3.* Three orders are divisible by 3 (Section 1). The even trace $t_i$ and $-t_i$ are $\equiv c$ and $-c$, so exactly one of the two even orders is divisible by 3 (hence by 6). Therefore the three multiples of 3 consist of that one even order and **two odd multiples of 3**; these are $>3$ since $N \ge q+1-2\sqrt q > 3$ for $q \ge 13$.

So 4 of the 6 orders are composite (2 even, 2 odd multiples of 3) and at most two can be prime. $\square$

## 3. Each value occurs at most twice

Let $a(n) = q$, $p = A399358(n)$, with $t = p + 1 - q$ and $t^2+3u^2 = 4p$. Then
$$4q = 4p + 4 - 4t = (t-2)^2 + 3u^2 ,$$
so by Lemma 1, $t'' = 2 - t$ is one of the six traces over $\mathbb{F}_q$, and $p = q + 1 - t''$ is one of the six orders $N_b(q)$.
By Section 2, at most two of those are prime, and $A399358$ is strictly increasing, so $q$ is attained by at most two indices $n$.
(For $q = 7$: the first term $a(1)=7$ occurs once.) $\square$

## 4. Anomalous primes

$a(n) = A399358(n)$ iff $\#E(\mathbb{F}_p) = p$, by definition (anomalous prime, trace 1). $\square$

## 5. The amicable criterion (reciprocity + a finite computation)

**Theorem.** Let $p = A399358(n) > 13$ and $q = a(n)$ (so $q$ is a prime $\equiv 1 \pmod 6$, $q>7$). Then $\#E(\mathbb{F}_q) = p$ if and only if
$(p \bmod 84,\ q \bmod 84) \in \{(43,43),(43,67),(43,73),(61,61),(67,43),(67,79),(73,43),(79,67),(79,79)\}$.

*Proof.* Notation: $\pi$ primary with $p=\pi\bar\pi$, $z(\pi)=(28/\pi)_6$, $\sigma_p = -\overline{z(\pi)}\,\pi$. By Fact 0,
$\#E(\mathbb{F}_p) = p+1-\operatorname{Tr}\sigma_p = \operatorname{Norm}(1-\sigma_p)$.

**Step A: $z(\pi)$ depends only on $\pi \bmod 84$.** A sixth root of unity $z$ is determined by $z^3$ and $z^2$ (as $z = z^3 \cdot (z^2)^{-1}$), and
* $z^3 = (28/\pi)_2 = \left(\tfrac{28}{p}\right) = \left(\tfrac{7}{p}\right)$, which by quadratic reciprocity depends only on $p \bmod 28$, hence on $\pi \bmod 28$;
* $z^2 = (28/\pi)_3 = (2/\pi)_3^{2}\,(7/\pi)_3$. By cubic reciprocity ($2$ and the two primary primes $\pi_7,\bar\pi_7$ above $7$ being primary), $(2/\pi)_3 = (\pi/2)_3$, which depends only on $\pi \bmod 2$, and $(7/\pi)_3 = (\pi_7/\pi)_3(\bar\pi_7/\pi)_3 = (\pi/\pi_7)_3(\pi/\bar\pi_7)_3$, which depends only on $\pi \bmod 7$.

So $z$ is a function $F$ on primary classes modulo $\operatorname{lcm}(4,28,2,7,3) \mid 84$. (Reciprocity laws are quoted, not re-proved.)

**Step B: the table $F$.** Every one of the 432 primary classes mod 84 contains a prime; computing $z$ from one prime per class determines $F$. `code/verify_amicable_criterion.py` computes it from all primes $p<4\cdot10^5$ and finds no inconsistency (a numerical confirmation of Step A).

**Step C: reformulation.** Let $\rho = 1-\sigma_p$, so $q = \operatorname{Norm}(\rho)$, and note $\operatorname{Norm}(1-\rho)=\operatorname{Norm}(\sigma_p) = p$. Let $\pi_q$ be the primary associate of $\rho$, $\rho = v\pi_q$ ($v$ a unit). The Frobenius over $\mathbb{F}_q$ is $\sigma_q = -\overline{z(\pi_q)}\,\pi_q$, an associate of $\pi_q$, and $\#E(\mathbb{F}_q) = q+1-\operatorname{Tr}\sigma_q$ while $p = \operatorname{Norm}(1-\rho) = q+1-\operatorname{Tr}\rho$. So $\#E(\mathbb{F}_q) = p \iff \operatorname{Tr}\sigma_q = \operatorname{Tr}\rho$. The six associates of $\pi_q$ have pairwise distinct traces ($t_1 = t_2 \Rightarrow x=0$, $t_1=-t_2 \Rightarrow t_3=0 \Rightarrow x=2y$, etc.; each makes $q$ a square or three times a square), so this holds iff $\sigma_q = \rho$, i.e. iff $z(\pi_q) = -\bar v$.

**Step D: finite check.** For each of the 432 classes of $\pi$ mod 84, the script computes $\rho$, $q \bmod 84$, $z(\pi_q)$ from the table, and decides the condition of Step C. It finds that the outcome depends only on $(p \bmod 84, q \bmod 84)$ (among the 100 admissible classes, 26 are amicable) and that the amicable pairs are exactly the nine listed. $\square$

The criterion also agrees with all 5670 terms below $2\cdot10^6$ (`code/verify.py`).

## 6. Verified by computer only

The data, the 5670-term b-file, the counts (32 anomalous primes; 738 amicable pairs, 1476 primes), the list 61, 127, 397, 547, 4447, 6211, and the first few pairs — `code/verify.py`.

## Remark: the "mod 84" comment of the first draft is trivial

Primes $q > 7$ with $q \equiv 1 \pmod 6$ lie in exactly the twelve classes $1,13,19,25,31,37,43,55,61,67,73,79 \pmod{84}$ (the classes $7, 49$ are divisible by 7). That is all the former comment said, so it was removed. (For the *primes* $p = A399358(n)$ themselves only six classes occur, $13,43,61,67,73,79$; this is a statement about A399358: $\#E(\mathbb{F}_p)$ prime forces $7$ to be a quadratic nonresidue mod $p$, otherwise $(0,\pm\sqrt7)$ are points of order 3, and by quadratic reciprocity that selects exactly these six classes.)
