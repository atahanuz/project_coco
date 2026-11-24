def get_b_list(max_n):
    b = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        if n % 2 == 1:
            b[n] = ((n % 4) - 1) // 2
        else:
            b[n] = b[n // 2]
    return b

def find_u_fast(v, b):
    s = "".join(map(str, b[1:]))
    for u in range(len(s) - 2 * v + 1):
        if s[u : u + v] == s[u + v : u + 2 * v]:
            return u + 1
    return None

max_n = 10000000
b = get_b_list(max_n)
print(f"v=4: {find_u_fast(4, b)}")
print(f"v=2: {find_u_fast(2, b)}")
print(f"v=6: {find_u_fast(6, b)}")
