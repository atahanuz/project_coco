def check(n):
    d = 2 * n - 1
    if d == 0: return False
    d = abs(d)
    if d == 1: return True
    
    res = 1
    for i in range(1, n + 3):
        res = (res * i) % d
    
    return (3 * (res + 1)) % d == 0

# Checking n from 0 to 100000
solutions = []
for n in range(100000):
    if check(n):
        solutions.append(n)
print(solutions)
