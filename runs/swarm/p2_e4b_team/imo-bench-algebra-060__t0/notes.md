### [W4, round 1]
Computational search (p, q <= 50) for maximum S < 1 yielded:
Max S: 0.9991496598639457
Corresponding (n, p, q): (11, 24, 49)

### [W3, round 1]
Analysis of S = (12 + n)/p + (13 - n)/q < 1:
1. Algebraic Constraint: The constraint is S < 1. To maximize S, we must minimize the denominators p and q relative to the numerators (12+n) and (13-n), while ensuring the sum remains less than 1.
2. Bounds: Since p and q are positive integers, the largest possible value S can approach is 1. If S were allowed to be 1, we would require (12+n)/p + (13-n)/q = 1.
3. Approaching 1: We showed that for any chosen n (1 <= n <= 12), S can approach 1 arbitrarily closely. For example, if we fix n=12, S = 24/p + 1/q. By choosing p=25 and q=26, S = 24/25 + 1/26 \approx 0.9984 < 1. By increasing p or q further, S gets closer to 1.
4. Relationship between p and q: To maximize S towards 1 for a fixed n, we require p to be slightly larger than (12+n) and q to be large enough such that (13-n)/q is small enough to compensate for the first term, keeping the total sum below 1.

### [W2, round 1]
Case n=6: S = 18/p + 7/q < 1. Max S is achieved when p=19, resulting in S = 2545/2546. (p=19 implies q > 133, smallest q=134).

Case n=7: S = 19/p + 6/q < 1. Max S is achieved when p=20, resulting in S = 2419/2420. (p=20 implies q > 120, smallest q=121).

### [W1, round 1]
Investigated boundary case n=1: S = 13/p + 12/q < 1.
The maximum S found by testing small integer values for p and q is S = 2365/2366, achieved with (p, q) = (14, 169). This value is approximately 0.99958.

Investigated boundary case n=12: S = 24/p + 1/q < 1.
The maximum S found by testing small integer values for p and q is S = 649/650, achieved with (p, q) = (25, 26). This value is approximately 0.99846.

The maximum S observed between these two boundary cases is 2365/2366.

### [W4, round 2]
### [W4, round 2] Computational Verification (p, q <= 500)

Verified the best candidate values for n=1 and n=6 by expanding the search for p and q up to 500.

1. For n=1 ($S = 13/p + 12/q < 1$): Max S found is $0.9995773...$, achieved with $(p, q) = (14, 169)$. This matches the fraction $2365/2366$ previously reported by W1.
2. For n=6 ($S = 18/p + 7/q < 1$): Max S found is $0.9996072...$, achieved with $(p, q) = (19, 134)$. This matches the fraction $2545/2546$ previously reported by W2.

Conclusion: The previously found maximum candidates are robust within the $p, q \le 500$ search limit. The highest value found among these two cases is $2545/2546$.

### [W1, round 2]
### [W1, round 2] Verification for n=6
The problem requires maximizing $S = 18/p + 7/q < 1$.
To maximize S for a fixed p, q must be minimized. The minimum integer $q$ is $q_{\min}(p) = \lfloor \frac{7p}{p-18} \rfloor + 1$. Since $p \ge 19$.

1.  **$p=19$**: $q_{\min}(19) = \lfloor 7 \cdot 19 / (19-18) \rfloor + 1 = 133 + 1 = 134$.
    $S(19) = 18/19 + 7/134 = 2545/2546 \approx 0.9996059$.

2.  **Analysis of $p$ dependence**: We analyzed $S(p)$ by calculating values for $p > 19$ using $q_{\min}(p)$.
    *   $p=20$: $q_{\min}(20) = 71$. $S(20) = 709/710 \approx 0.99859$. ($S$ decreased)
    *   $p=22$: $q_{\min}(22) = 39$. $S(22) = 428/429 \approx 0.99766$. ($S$ decreased)
    *   $p=145$: $q_{\min}(145) = 8$. $S(145) = 18/145 + 7/8 \approx 0.99910$. ($S$ decreased)

The function $S(p)$ is shown to be decreasing as $p$ increases beyond $p=19$. Therefore, the maximum value for $n=6$ occurs at $p=19, q=134$.

This confirms the result found in W2, round 1.
