def solve_tiling(H, W):
    shapes = [
        ([(0, 1), (0, 2), (1, 0), (1, 1)], 0),
        ([(0, 0), (0, 1), (1, 1), (1, 2)], 0),
        ([(0, 0), (1, 0), (1, 1), (2, 1)], 0),
        ([(0, 1), (1, 0), (1, 1), (2, 0)], 0),
        ([(0, 0), (0, 1)], 1),
        ([(0, 0), (1, 0)], 1)
    ]
    processed_shapes = []
    for coords, cost in shapes:
        best_r = float('inf')
        best_c = float('inf')
        for r, c in coords:
            if r < best_r:
                best_r = r
                best_c = c
            elif r == best_r:
                if c < best_c:
                    best_c = c
        normalized = tuple(sorted((r - best_r, c - best_c) for r, c in coords))
        processed_shapes.append((normalized, cost))
    unique_shapes = list(set(processed_shapes))
    memo = {}
    def solve(grid_mask):
        if grid_mask == (1 << (H * W)) - 1:
            return 0
        if grid_mask in memo:
            return memo[grid_mask]
        idx = 0
        while (grid_mask >> idx) & 1:
            idx += 1
        r, c = divmod(idx, W)
        res = float('inf')
        for coords, cost in unique_shapes:
            possible = True
            new_mask = grid_mask
            for dr, dc in coords:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W:
                    n_idx = nr * W + nc
                    if not ((grid_mask >> n_idx) & 1):
                        new_mask |= (1 << n_idx)
                    else:
                        possible = False
                        break
                else:
                    possible = False
                    break
            if possible:
                res = min(res, cost + solve(new_mask))
        memo[grid_mask] = res
        return res
    return solve(0)

for h in [4, 8, 12, 16, 20]:
    for w in [6, 10, 14]:
        print(f"N_D({h}, {w}) = {solve_tiling(h, w)}")
