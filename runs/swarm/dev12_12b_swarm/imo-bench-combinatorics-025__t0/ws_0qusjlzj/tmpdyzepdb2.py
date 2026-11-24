def solve():
    # The previous script was slow because it recalculated get_m for each n.
    # Let's use a single memo dictionary and iterate through n.
    memo = {}

    def get_m(boards, is_alice):
        boards = tuple(sorted([b for b in boards if b > 1], reverse=True))
        if not boards:
            return 0
        
        state = (boards, is_alice)
        if state in memo:
            return memo[state]
        
        if is_alice:
            best_m = float('inf')
            for i, b in enumerate(boards):
                for k in range((b-2)//2 + 1):
                    new_boards = list(boards[:i] + boards[i+1:])
                    new_boards.append(k)
                    new_boards.append(b - k - 2)
                    res = 1 + get_m(tuple(new_boards), False)
                    if res < best_m:
                        best_m = res
            memo[state] = best_m
            return best_m
        else:
            best_m = float('-inf')
            for i, b in enumerate(boards):
                for k in range((b-2)//2 + 1):
                    new_boards = list(boards[:i] + boards[i+1:])
                    new_boards.append(k)
                    new_boards.append(b - k - 2)
                    res = 1 + get_m(tuple(new_boards), True)
                    if res > best_m:
                        best_m = res
            memo[state] = best_m
            return best_m

    results = []
    for n in range(1, 101):
        m_n = get_m((n,), True)
        results.append((n, m_n, n - 2*m_n))
    return results

res = solve()
for r in res:
    print(r)
