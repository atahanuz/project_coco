from itertools import permutations

def check_m(m):
    # A multiset of m residues
    # We need to find if there exists any multiset R such that
    # sum(R) % m != 0 AND for all permutations sigma,
    # sum(j * r_sigma(j)) % m != 0
    
    # To optimize, we can iterate over multisets of size m
    # But that's too many. Let's try some specific multisets.
    # The notes say m is odd or a power of 2.
    # So we check m=6, 10, 12, 14...
    
    # Let's try a simpler approach: 
    # For a given m, check all multisets of size m
    # and for each, if sum(R) % m != 0, check all permutations.
    pass

def solve_m(m):
    # Using the property that any multiset of m residues can be formed
    # by m distinct integers.
    # The number of multisets of size m from m residues is (m+m-1 choose m)
    # For m=6, this is (11 choose 6) = 462.
    # For m=10, this is (19 choose 10) = 92378.
    
    import itertools
    
    # We want to find if there's any multiset R such that:
    # 1. sum(R) % m != 0
    # 2. for all permutations sigma, sum(j * r_sigma(j)) % m != 0
    
    # Let's just iterate over all multisets
    # A multiset can be represented as a sorted tuple of residues
    # To generate multisets:
    count = 0
    for r in itertools.combinations_with_replacement(range(m), m):
        if sum(r) % m != 0:
            # Check all permutations
            possible = False
            # Use set of permutations to avoid duplicates
            for p in set(itertools.permutations(r)):
                weighted_sum = sum(j * p[j-1] for j in range(1, m+1))
                if weighted_sum % m == 0:
                    possible = True
                    break
            if not possible:
                return False # Found a multiset that fails the condition
    return True

# Check small m
for m in range(2, 11):
    print(f"m={m}: {solve_m(m)}")
