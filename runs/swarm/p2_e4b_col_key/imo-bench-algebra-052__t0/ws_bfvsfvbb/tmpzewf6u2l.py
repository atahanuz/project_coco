import numpy as np
import itertools

TARGET = 1810
N = 20
MAX_X = 100
SIMULATIONS = 1000
THRESHOLD = 90

def generate_sequence():
    """Generates a sequence X of length N such that 0 <= x_i <= 100 and sum(X) >= TARGET."""
    while True:
        X = np.random.randint(0, MAX_X + 1, size=N)
        S = np.sum(X)
        if S >= TARGET:
            return X
        else:
            # Adjust elements to meet the target sum without exceeding 100
            needed = TARGET - S
            # Randomly distribute the needed amount among available elements (those < 100)
            # This ensures we don't drastically change the random distribution while meeting the constraint.
            
            # Find indices that can take the needed amount
            modifiable_indices = np.where(X < MAX_X)[0]
            
            if len(modifiable_indices) == 0:
                # This should not happen if MAX_X is large enough relative to TARGET/N
                # But if it does, we must restart or fail.
                continue 
            
            # Greedily add the needed amount, capped at the remaining capacity of the chosen elements
            remaining_needed = needed
            
            # Select a few indices to increment to meet the target
            indices_to_modify = np.random.choice(modifiable_indices, size=min(len(modifiable_indices), 5), replace=False)
            
            X_new = X.copy()
            
            for i in indices_to_modify:
                capacity = MAX_X - X_new[i]
                increment = min(remaining_needed, capacity)
                X_new[i] += increment
                remaining_needed -= increment
                if remaining_needed <= 0:
                    break
            
            if remaining_needed <= 0:
                return X_new
            # If remaining_needed > 0, it means we couldn't reach TARGET even by maxing out 5 elements.
            # Since TARGET/N is 90.5, and we generated random values, this case is highly unlikely 
            # unless the initial random draw was extremely low across many elements. We restart the loop.

def calculate_min_gap(X):
    """Calculates the minimum gap |subset_sum - TARGET| for non-trivial subsets."""
    min_gap = float('inf')
    
    # Iterate through all 2^N subsets (represented by integers 0 to 2^N - 1)
    # We skip subset 0 (empty set) and subset 2^N - 1 (full set) as per standard interpretation.
    num_subsets = 1 << N
    
    for i in range(1, num_subsets - 1):
        current_sum = 0
        for j in range(N):
            if (i >> j) & 1:
                current_sum += X[j]
        
        gap = abs(current_sum - TARGET)
        min_gap = min(min_gap, gap)
        
    return min_gap

def run_simulation():
    gaps_greater_than_90 = 0
    for _ in range(SIMULATIONS):
        X = generate_sequence()
        min_gap = calculate_min_gap(X)
        
        if min_gap > THRESHOLD:
            gaps_greater_than_90 += 1
            
    print(f"Simulation complete for {SIMULATIONS} sequences (N={N}, Target={TARGET}, Threshold={THRESHOLD}).")
    print(f"Number of sequences where minimum gap > 90: {gaps_greater_than_90}")
    print(f"Percentage of sequences where minimum gap > 90: {gaps_greater_than_90 / SIMULATIONS * 100:.2f}%")

run_simulation()