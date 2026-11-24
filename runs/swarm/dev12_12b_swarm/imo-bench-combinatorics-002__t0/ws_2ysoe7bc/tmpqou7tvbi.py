def solve_backtrack(n):
    if (3*n**2 + n) % 4 != 0:
        return False
    
    available_nums = [True] * (2*n + 1)
    available_diffs = [False] * (n + 1)
    for i in range(1, n + 1): available_diffs[i] = True
    
    def backtrack(count):
        if count == n:
            return True
        
        a = 1
        while a <= 2*n and not available_nums[a]:
            a += 1
        
        if a > 2*n:
            return False
        
        for d in range(1, n + 1):
            if available_diffs[d]:
                b = a + d
                if b <= 2*n and available_nums[b]:
                    available_nums[a] = False
                    available_nums[b] = False
                    available_diffs[d] = False
                    if backtrack(count + 1):
                        return True
                    available_diffs[d] = True
                    available_nums[a] = True
                    available_nums[b] = True
        return False

    return backtrack(0)

# Check some values near the boundaries.
for n in range(98, 103):
    print(f"n={n}: {solve_backtrack(n)}")

for n in range(203, 208):
    print(f"n={n}: {solve_backtrack(n)}")
