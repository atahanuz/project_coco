import itertools

def is_all_close(p1, p2):
    for v1, v2 in zip(p1, p2):
        if abs(v1 - v2) > 1:
            return False
    return True

def solve_n(n):
    perms = list(itertools.permutations(range(1, n + 1)))
    adj = [[] for _ in range(len(perms))]
    for i in range(len(perms)):
        for j in range(i + 1, len(perms)):
            if is_all_close(perms[i], perms[j]):
                adj[i].append(j)
                adj[j].append(i)
    
    # Find maximum independent set size using a simple backtracking with pruning
    max_is = 0
    def backtrack(current_set, candidates):
        nonlocal max_is
        if not candidates:
            max_is = max(max_is, len(current_set))
            return
        
        if len(current_set) + len(candidates) <= max_is:
            return
        
        v = candidates[0]
        
        # Option 1: v is in the independent set
        new_candidates = [c for c in candidates[1:] if c not in adj[v]]
        backtrack(current_set + [v], new_candidates)
        
        # Option 2: v is not in the independent set
        backtrack(current_set, candidates[1:])

    # To speed up, we can use a more efficient algorithm for max independent set
    # but for n=6, we can try this or a better one.
    # Actually, let's use a simple recursive one with a bit of greedy pruning.
    
    def get_max_is(nodes):
        if not nodes:
            return 0
        v = max(nodes, key=lambda x: len(adj[x]))
        # Either v is in the max independent set or it's not.
        # But we can use the fact that the graph is small.
        # Let's use a standard max independent set algorithm.
        pass

    # Let's use a simpler approach.
    # The graph is small, let's just use the one from before but optimize it.
    memo = {}
    def max_independent_set_recursive(nodes):
        nodes = tuple(sorted(nodes))
        if not nodes:
            return 0
        if nodes in memo:
            return memo[nodes]
        
        v = nodes[0]
        # Case 1: v is in the independent set
        res1 = 1 + max_independent_set_recursive(tuple(n for n in nodes[1:] if n not in adj[v]))
        # Case 2: v is not in the independent set
        res2 = max_independent_set_recursive(nodes[1:])
        
        res = max(res1, res2)
        memo[nodes] = res
        return res

    return max_independent_set_recursive(tuple(range(len(perms))))

# The recursive one might be slow for n=6. Let's try a more efficient one.
def solve_n_efficient(n):
    perms = list(itertools.permutations(range(1, n + 1)))
    adj = [0] * len(perms)
    for i in range(len(perms)):
        for j in range(i + 1, len(perms)):
            if is_all_close(perms[i], perms[j]):
                adj[i] |= (1 << j)
                adj[j] |= (1 << i)
    
    memo = {}
    def solve(mask):
        if mask == 0:
            return 0
        if mask in memo:
            return memo[mask]
        
        # Find the first set bit
        v = (mask & -mask).bit_length() - 1
        
        # Option 1: v is in the independent set
        # All neighbors of v are removed from the candidates.
        res1 = 1 + solve(mask & ~adj[v] & ~(1 << v))
        
        # Option 2: v is not in the independent set
        res2 = solve(mask & ~(1 << v))
        
        res = max(res1, res2)
        memo[mask] = res
        return res

    # This is still slow for 720 nodes.
    # Let's find the connected components first.
    visited = [False] * len(perms)
    total_max_is = 0
    for i in range(len(perms)):
        if not visited[i]:
            component = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                component.append(u)
                for v in range(len(perms)):
                    if (adj[u] & (1 << v)) and not visited[v]:
                        visited[v] = True
                        stack.append(v)
            
            # Now find max independent set for this component
            # The component size should be small.
            comp_adj = [0] * len(component)
            # Map component indices to 0...len(component)-1
            idx_map = {node: i for i, node in enumerate(component)}
            for idx, node in enumerate(component):
                for neighbor in range(len(perms)):
                    if (adj[node] & (1 << neighbor)) and neighbor in idx_map:
                        comp_adj[idx] |= (1 << idx_map[neighbor])
            
            # Max independent set on this component
            comp_memo = {}
            def solve_comp(mask):
                if mask == 0:
                    return 0
                if mask in comp_memo:
                    return comp_memo[mask]
                v = (mask & -mask).bit_length() - 1
                res = max(1 + solve_comp(mask & ~comp_adj[v] & ~(1 << v)),
                          solve_comp(mask & ~(1 << v)))
                comp_memo[mask] = res
                return res
            
            total_max_is += solve_comp((1 << len(component)) - 1)
    return total_max_is

# Let's try this for n=4, 5, 6.
for n in range(1, 7):
    print(f"N({n}) = {solve_n_efficient(n)}")
