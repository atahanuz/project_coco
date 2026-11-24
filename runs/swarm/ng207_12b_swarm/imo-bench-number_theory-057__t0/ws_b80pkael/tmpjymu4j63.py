def get_base7(n):
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.append(n % 7)
        n //= 7
    return digits[::-1]

def get_a_i(m_digits, b_i):
    results = []
    for idx, digit in enumerate(m_digits):
        if digit == b_i:
            new_digits = m_digits[:idx] + m_digits[idx+1:]
            if not new_digits:
                results.append(0)
            else:
                res = 0
                for d in new_digits:
                    res = res * 7 + d
                results.append(res)
    
    if not results:
        return None
    if len(set(results)) == 1:
        return results[0]
    return None

def solve():
    solutions = []
    for m in range(1, 15): # Try small m
        # n must be in [7^m, 7^{m+1} - 1]
        # But the problem says "the base-7 representation ... for some positive integer m"
        # This means the highest power is 7^m.
        # So n = b_m 7^m + ... + b_0 7^0 with b_m != 0.
        start = 7**m
        end = 7**(m+1)
        
        m_digits = get_base7(m)
        
        for n in range(start, end):
            n_digits = get_base7(n)
            # n_digits = [b_m, b_{m-1}, ..., b_0]
            # Length of n_digits should be m+1.
            if len(n_digits) != m + 1:
                continue
            
            # b_i is the digit at position i from the right (0-indexed)
            # n_digits is [b_m, b_{m-1}, ..., b_0]
            # So b_i = n_digits[m-i]
            
            total_a = 0
            possible = True
            for i in range(m):
                b_i = n_digits[m-i]
                a_i = get_a_i(m_digits, b_i)
                if a_i is None:
                    possible = False
                    break
                total_a += a_i
            
            if possible and total_a == n:
                solutions.append((n, m, n_digits))
                
    return solutions

results = solve()
print(results)
