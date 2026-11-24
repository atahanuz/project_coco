import numpy as np
from scipy.optimize import minimize

def find_min_ratio(y):
    y = sorted(y)
    y1, y2, y3, y4 = y
    r1 = abs(y1/y4 - y2/y3)
    r2 = abs(y1/y3 - y2/y4)
    r3 = abs(y1/y2 - y3/y4)
    return min(r1, r2, r3)

def objective(r):
    x = [1.0]
    for i in range(3):
        x.append(x[-1] * r[i])
    x.append(x[-1] * r[3])
    
    subsets = [
        x[0:4],
        [x[0], x[1], x[2], x[4]],
        [x[0], x[1], x[3], x[4]],
        [x[0], x[2], x[3], x[4]],
        x[1:5]
    ]
    
    min_r = float('inf')
    for s in subsets:
        min_r = min(min_r, find_min_ratio(s))
    return -min_r

# Try more random starts
best_val = 0
best_r = None
for _ in range(230000):
    initial_r = np.random.uniform(1.1, 10.0, 4)
    res = minimize(objective, initial_r, bounds=[(1.01, None)]*4, method='L-BFGS-B')
    if -res.fun > best_val:
        best_val = -res.fun
        best_r = res.x

print(f"Best min ratio: {best_val}")
print(f"Best r: {best_r}")

x = [1.0]
for i in range(3):
    x.append(x[-1] * best_r[i])
x.append(x[-1] * best_r[3])
subsets = [
    x[0:4],
    [x[0], x[1], x[2], x[4]],
    [x[0], x[1], x[3], x[4]],
    [x[0], x[2], x[3], x[4]],
    x[1:5]
]
for i, s in enumerate(subsets):
    print(f"Subset {i}: {find_min_ratio(s)}")
