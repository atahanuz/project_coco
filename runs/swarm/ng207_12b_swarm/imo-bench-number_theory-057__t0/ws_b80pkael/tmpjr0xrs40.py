def solve_with_rule_3_extended(max_m):
    solutions = []
    for m in range(1, max_m + 1):
        temp_m = m
        m_base7 = []
        while temp_m > 0:
            m_base7.append(temp_m % 7)
            temp_m //= 7
        m_base7.reverse()
        m_str = "".join(map(str, m_base7))
        S = set(map(int, list(m_str)))
        
        # n < m^2/7 is a good bound
        # For m=1, m^2/7 = 0.14. For m=400, m^2/7 = 22857.
        # Let's use n < m^2 to be safe.
        # However, we also need to check if n can have more digits than m.
        # But n = sum(a_i) and a_i < m, so n < m^2.
        # Also n = sum(b_i 7^i). If b_m is the highest non-zero digit, 7^m <= n < m^2.
        # This only happens for small m.
        # If b_m = 0, then n < 7^m.
        # The condition n < m^2 is always sufficient.
        
        for n in range(1, m*m + 1):
            n_base7 = []
            temp_n = n
            # The representation is b_m b_{m-1} ... b_0
            # So there are m+1 digits.
            for _ in range(m + 1):
                n_base7.append(temp_n % 7)
                temp_n //= 7
            n_base7.reverse()
            
            current_sum = 0
            possible = True
            for i in range(m):
                bi = n_base7[m-i]
                if bi in S:
                    s_list = list(m_str)
                    s_list.remove(str(bi))
                    a_i_str = "".join(s_list)
                    a_i = int(a_i_str, 7) if a_i_str else 0
                else:
                    possible = False
                    break
                current_sum += a_i
            
            if possible and current_sum == n:
                solutions.append((n, m, n_base7, m_str))
    return solutions

print(solve_with_rule_3_extended(400))
