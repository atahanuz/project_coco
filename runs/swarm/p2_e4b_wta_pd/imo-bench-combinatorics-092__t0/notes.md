### [W1, round 1]
Cycle count results for x -> 3x mod m (m not divisible by 3) for m in [4, 30]:
M=4: 2
M=5: 1
M=7: 1
M=8: 4
M=10: 3
M=11: 2
M=13: 4
M=14: 3
M=16: 6
M=17: 1
M=19: 1
M=20: 6
M=22: 5
M=23: 2
M=25: 2
M=26: 9
M=28: 6
M=29: 1

Goal: Find the second largest integer m < 200 such that the number of cycles is odd.

### [W3, round 1]
Initial investigation of the permutation pi(x) = 3x mod m on S = {1, ..., m-1} when gcd(x, m) > 1.

Observation: If gcd(x, m) = d > 1, then d divides x. Since pi(x) = 3x - km (for some integer k), d divides 3x and d divides km, thus d divides pi(x). This means that the set of non-unit elements is closed under the mapping pi.

Consequence: The non-unit elements partition into disjoint cycles among themselves, independent of the cycles formed by the unit elements.

Example m=10: Non-units are {2, 4, 5, 6, 8}. The cycles are (2 6 8 4) and (5). These form a closed system separate from the unit cycle (1 3 9 7).

Conclusion: The non-unit elements can be easily partitioned into independent cycles because the mapping keeps the elements within the set of non-units. This property holds generally when gcd(x, m) > 1.
