import itertools

def solve_m(m):
    cap = m + 1
    v = []
    for k in range(1, m):
        vec = [1] * k + [-1] * (m - k)
        v.append(tuple(vec))
        
    states = list(itertools.product(range(1, cap + 1), repeat=m))
    
    # For each state and each k, we have two moves.
    # Each move is represented by a tuple (is_out_of_bounds, y_prime_capped)
    moves_per_k = {}
    for y in states:
        moves_per_k[y] = []
        for vec in v:
            k_moves = []
            for s in [1, -1]:
                y_prime = tuple(y[i] + s * vec[i] for i in range(m))
                is_out = any(y_prime[i] < 1 for i in range(m))
                y_prime_capped = tuple(min(y_prime[i], cap) for i in range(m))
                k_moves.append((is_out, y_prime_capped))
            moves_per_k[y].append(k_moves)
    
    losing = set()
    while True:
        new_losing = set()
        for y in states:
            is_losing_state = False
            for k_moves in moves_per_k[y]:
                # For this k, are both moves bad?
                all_s_bad = True
                for is_out, y_prime_capped in k_moves:
                    bad = False
                    if is_out:
                        bad = True
                    elif y_prime_capped in losing:
                        bad = True
                    
                    if not bad:
                        all_s_bad = False
                        break
                
                if all_s_bad:
                    is_losing_state = True
                    break
            
            if is_losing_state:
                new_losing.add(y)
        
        if new_losing == losing:
            break
        losing = new_losing
        
    min_n = float('inf')
    for y in states:
        if y not in losing:
            min_n = min(min_n, sum(y))
    return min_n

for m in range(2, 8):
    print(f"m={m}, n={solve_m(m)}")
