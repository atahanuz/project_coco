### [W1, round 1]
Total number of unique pairs of 40 teams: \binom{40}{2} = 780.

### [W3, round 1]
Analysis for the guarantee condition:
Let $N=40$ be the number of teams.
The total number of unique pairings (games) possible is $E_{total} = \binom{40}{2} = 780$.
After $a$ rounds, $E_a = 20a$ distinct games have been played (since no team pair has played twice yet).
Round $a+1$ requires $E_{a+1} = 20$ pairings.

A repeat pairing is guaranteed in round $a+1$ if the number of available unplayed pairings remaining, $E_{total} - E_a$, is strictly less than the number of pairings required in the next round, $E_{a+1}$.

Condition for guaranteed repeat pairing:
$E_{total} - E_a < E_{a+1}$
$780 - 20a < 20$
