f = [0] * 2021
f[0] = 0
f[1] = 1

memo_g = {}

def get_g(m, k):
    if (m, k) in memo_g:
        return memo_g[(m, k)]
    
    res = float('inf')
    can_move = False
    
    # Bob moves on board m
    for j in range(1, m):
        can_move = True
        res = min(res, f[j-1] + f[m-j-1] + f[k])
    
    # Bob moves on board k
    for j in range(1, k):
        can_move = True
        res = min(res, f[m] + f[j-1] + f[k-j-1])
        
    if not can_move:
        res = f[m] + f[k]
        
    memo_g[(m, k)] = res
    return res

for n in range(2, 2021):
    best_val = -1
    for i in range(1, n):
        val = get_g(i-1, n-i-1)
        if val > best_val:
            best_val = val
    f[n] = best_val

print(f[2020])
