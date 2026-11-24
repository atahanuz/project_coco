import itertools

def are_close(p, q):
    for x, y in zip(p, q):
        if abs(x - y) > 1:
            return False
    return True

def solve_fast(n):
    perms = list(itertools.permutations(range(1, n + 1)))
    adj = [set() for _ in range(len(perms))]
    for i in range(len(perms)):
        for j in range(i + 1, len(perms)):
            if are_close(perms[i], perms[j]):
                adj[i].add(j)
                adj[j].add(i)
    
    # Max Independent Set of a graph
    # A graph can be decomposed into connected components.
    # The max independent set is the sum of the max independent sets of its components.
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
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            
            # Find MIS of this component
            comp_adj = {u: [v for v in adj[u] if v in component] for u in component}
            comp_nodes = sorted(component, key=lambda x: len(comp_adj[x]))
            
            memo = {}
            def get_mis(nodes_tuple):
                if not nodes_tuple:
                    return 0
                if nodes_tuple in memo:
                    return memo[nodes_tuple]
                
                v = nodes_tuple[0]
                # Include v
                nodes_include = tuple(n for n in nodes_tuple[1:] if n not in comp_adj[v])
                res1 = 1 + get_mis(nodes_include)
                
                # Exclude v
                nodes_exclude = nodes_tuple[1:]
                res2 = get_mis(nodes_exclude)
                
                res = max(res1, res2)
                memo[nodes_tuple] = res
                return res
            
            total_max_is += get_mis(tuple(comp_nodes))
            
    return total_max_is

for n in range(1, 6):
    print(f"N({n}) = {solve_fast(n)}")
