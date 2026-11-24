def solve():
    solutions = []
    for m in range(1, 340000):
        digits_m = []
        temp_m = m
        while temp_m > 0:
            digits_m.append(temp_m % 7)
            temp_m //= 7
        digits_m.reverse()
        S = set(digits_m)
        
        a_values = {}
        m_str = "".join(map(str, digits_m))
        for d in S:
            possible_a = set()
            for j in range(len(m_str)):
                if int(m_str[j]) == d:
                    new_str = m_str[:j] + m_str[j+1:]
                    if new_str == "":
                        possible_a.add(0)
                    else:
                        val = int(new_str, 7)
                        possible_a.add(val)
            if len(possible_a) == 1:
                a_values[d] = list(possible_a)[0]
            else:
                a_values[d] = None
        
        if None in a_values.values():
            continue
            
        max_a = max(a_values.values()) if a_values else 0
        limit = m * max_a + 1
        
        for n in range(1, limit):
            b = []
            temp_n = n
            for _ in range(m + 1):
                b.append(temp_n % 7)
                temp_n //= 7
            b.reverse()
            
            valid = True
            for i in range(1, m + 1):
                if b[i] not in S:
                    valid = False
                    break
            if not valid:
                continue
            
            current_sum = 0
            for i in range(1, m + 1):
                current_sum += a_values[b[i]]
            
            if n == current_sum:
                solutions.append((n, m))
                
    return solutions

results = solve()
print(results)
