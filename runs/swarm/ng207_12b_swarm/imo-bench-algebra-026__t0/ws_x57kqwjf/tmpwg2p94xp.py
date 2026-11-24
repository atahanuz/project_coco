from fractions import Fraction
from collections import deque

def solve():
    x0 = Fraction(11, 3)
    targets = [
        Fraction(7, 3),
        Fraction(11, 4),
        Fraction(2024, 5),
        Fraction(109, 11),
        Fraction(3, 71),
        Fraction(5, 204)
    ]

    def get_neighbors(r):
        neighbors = []
        # T1(r) = -r
        if r != 0:
            neighbors.append(-r)
        # T2(r) = 1-r
        if r != Fraction(1, 2):
            neighbors.append(1 - r)
        # T3(r) = 1/r
        if r != 0 and r != 1 and r != -1:
            neighbors.append(1 / r)
        
        # Special cases for the edges mentioned in the problem
        # r + r' = 0 => r' = -r. Distinct means r != -r => r != 0.
        # r + r' = 1 => r' = 1-r. Distinct means r != 1-r => r != 1/2.
        # r * r' = 1 => r' = 1/r. Distinct means r != 1/r => r != 1, -1.
        
        # Let's re-check the special cases more carefully.
        # The condition is: f(r) + f(r') = 1 for all distinct r, r' satisfying
        # r + r' = 0 OR r + r' = 1 OR r * r' = 1.
        
        # For r = 0:
        # r + r' = 0 => r' = 0 (not distinct)
        # r + r' = 1 => r' = 1 (distinct)
        # r * r' = 1 => no solution
        # So 0 ~ 1.
        
        # For r = 1/2:
        # r + r' = 0 => r' = -1/2 (distinct)
        # r + r' = 1 => r' = 1/2 (not distinct)
        # r * r' = 1 => r' = 2 (distinct)
        # So 1/2 ~ -1/2 and 1/2 ~ 2.
        
        # For r = 1:
        # r + r' = 0 => r' = -1 (distinct)
        # r + r' = 1 => r' = 0 (distinct)
        # r * r' = 1 => r' = 1 (not distinct)
        # So 1 ~ -1 and 1 ~ 0.
        
        # For r = -1:
        # r + r' = 0 => r' = 1 (distinct)
        # r + r' = 1 => r' = 2 (distinct)
        # r * r' = 1 => r' = -1 (not distinct)
        # So -1 ~ 1 and -1 ~ 2.
        
        # The neighbors are indeed:
        # r -> -r if r != 0
        # r -> 1-r if r != 1/2
        # r -> 1/r if r != 1, -1
        # and r=0 -> 1, r=1/2 -> -1/2, 2, r=1 -> -1, 0, r=-1 -> 1, 2.
        # My current neighbors list handles all of these.
        # Let's check:
        # if r=0: neighbors = [1-0] = [1]. Correct.
        # if r=1/2: neighbors = [-1/2, 1/(1/2)] = [-1/2, 2]. Correct.
        # if r=1: neighbors = [-1, 1-1] = [-1, 0]. Correct.
        # if r=-1: neighbors = [1, 1-(-1)] = [1, 2]. Correct.
        
        # Wait, I should make sure I haven't missed anything.
        # The problem says r+r'=0 or r+r'=1 or rr'=1.
        # This is exactly what I used.
        
        return list(set(neighbors))

    # BFS
    distances = {x0: 0}
    queue = deque([x0])
    
    while queue:
        u = queue.popleft()
        d = distances[u]
        for v in get_neighbors(u):
            if v not in distances:
                distances[v] = d + 1
                queue.append(v)
                
    results = []
    for target in targets:
        if target in distances:
            dist = distances[target]
            f_val = (1 + dist) % 2
            results.append(f_val)
        else:
            results.append(None)
            
    print(f"Distances: {distances}")
    print(f"Results: {results}")
    print(f"Sum: {sum(results)}")

solve()
