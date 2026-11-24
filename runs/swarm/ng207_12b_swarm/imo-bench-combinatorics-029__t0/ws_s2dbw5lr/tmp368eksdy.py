def solve():
    shapes = [
        [(0, 1), (0, 2), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (1, 1), (1, 2)],
        [(0, 0), (1, 0), (1, 1), (2, 1)],
        [(0, 1), (1, 0), (1, 1), (2, 0)]
    ]
    dominoes = [
        [(0, 0), (0, 1)],
        [(0, 0), (1, 0)]
    ]
    
    all_shapes = []
    for s in shapes + dominoes:
        min_c = min(c for r, c in s)
        min_r_at_min_c = min(r for r, c in s if c == min_c)
        offsets = sorted([(r - min_r_at_min_c, c - min_c) for r, c in s])
        all_shapes.append(offsets)

    def solve_backtrack(H, W):
        memo = {}
        def backtrack(mask):
            if mask == (1 << (H * W)) - 1:
                return 0
            if mask in memo:
                return memo[mask]
            
            first_empty = 0
            while (mask & (1 << first_empty)):
                first_empty += 1
            
            r = first_empty % H
            c = first_empty // H
            
            res = float('inf')
            for i, shape in enumerate(all_shapes):
                can_place = True
                new_mask = mask
                for dr, dc in shape:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < H and 0 <= nc < W):
                        can_place = False
                        break
                    pos = nc * H + nr
                    if new_mask & (1 << pos):
                        can_place = False
                        break
                    new_mask |= (1 << pos)
                
                if can_place:
                    cost = 1 if i >= len(shapes) else 0
                    res = min(res, cost + backtrack(new_mask))
            
            memo[mask] = res
            return res

        return backtrack(0)

    for H in [4, 12, 20, 28, 36, 44, 52, 60]:
        print(f"N_D({H}, 6) = {solve_backtrack(H, 6)}")

solve()
