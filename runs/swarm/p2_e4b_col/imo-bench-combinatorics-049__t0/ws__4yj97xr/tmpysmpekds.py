import numpy as np
import random

# Configuration (Smallest viable size)
N = 8 # Very small grid size
MAX_STEPS = 500

def apply_rules(grid):
    """Applies Rule 1 and Rule 2 simultaneously based on the current grid state."""
    new_grid = grid.copy()
    changed = False
    
    for i in range(N - 1):
        for j in range(N - 1):
            neighborhood = grid[i:i+2, j:j+2]
            infected_count = np.sum(neighborhood)
            
            # Rule 1 (Growth)
            if infected_count == 3:
                sterile_coords = []
                for r in range(2):
                    for c in range(2):
                        if neighborhood[r, c] == 0:
                            sterile_coords.append((r, c))
                
                if sterile_coords:
                    r_global = i + sterile_coords[0][0]
                    c_global = j + sterile_coords[0][1]
                    
                    if new_grid[r_global, c_global] == 0:
                        new_grid[r_global, c_global] = 1
                        changed = True
            
            # Rule 2 (Mutation)
            elif infected_count == 2:
                local_indices = [(0, 0), (0, 1), (1, 0), (1, 1)]
                
                for r_local, c_local in local_indices:
                    r_global = i + r_local
                    c_global = j + c_local
                    
                    # Flip state
                    if new_grid[r_global, c_global] == 1:
                        new_grid[r_global, c_global] = 0
                    else:
                        new_grid[r_global, c_global] = 1
                
                changed = True
                
    return new_grid, changed

def simulate_run(initial_grid):
    """Runs the simulation for a single initial grid."""
    grid = initial_grid.copy()
    
    for step in range(MAX_STEPS):
        if np.sum(grid) == N * N:
            return True 
        
        next_grid, changed = apply_rules(grid)
        
        if not changed:
            return False 
        
        grid = next_grid
        
    return False 

def run_trials(k, num_trials):
    """Runs the simulation for k initial infected cells over many trials."""
    successful_trials = 0
    
    print(f"--- Running {num_trials} trials for k={k} on {N}x{N} grid ---")
    
    for _ in range(num_trials):
        grid = np.zeros((N, N), dtype=int)
        
        all_coords = [(r, c) for r in range(N) for c in range(N)]
        coords = random.sample(all_coords, k)
        for r, c in coords:
            grid[r, c] = 1
            
        if simulate_run(grid):
            successful_trials += 1
            
    failure_rate = (num_trials - successful_trials) / num_trials * 100
    return failure_rate

# --- Execution ---
NUM_TRIALS = 500 

# Run k=16
failure_k16 = run_trials(16, NUM_TRIALS)

# Run k=20
failure_k20 = run_trials(20, NUM_TRIALS)

print("\n=============================================")
print(f"Statistical Outcome (N={N}x{N}, Trials={NUM_TRIALS}):")
print(f"Failure Rate for k=16: {failure_k16:.2f}%")
print(f"Failure Rate for k=20: {failure_k20:.2f}%")
print("=============================================")